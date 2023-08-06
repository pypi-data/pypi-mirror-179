import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2
from IPython.display import Image, display
from skimage.filters import threshold_otsu
from rembg import remove
from rembg.session_factory import new_session
import cv2
import time 
from cv2 import COLOR_GRAY2RGB
import os
import sys  

# Function to combine the masks that have been generated
def combine_masks(mask_list, threshold=5):
    
    num_plots = len(mask_list) # intersection, union, avg threshold
    f, initial = plt.subplots(1,num_plots) 
    for i in range(num_plots):
        initial[i].axis('off')
    
    needed_shape = (480, 640) # is hardcoding ok?
    for i, mask in enumerate(mask_list):
        if mask.shape != needed_shape:
            mask = cv2.resize(mask.astype('uint8'), tuple(reversed(needed_shape)))
        mask_list[i] = mask > 0
        initial[i].imshow(mask_list[i])

    num_plots = 3 # intersection, union, avg threshold
    f, results = plt.subplots(1,num_plots) 
    for i in range(num_plots):
        results[i].axis('off')
    
    intersection = np.ones(needed_shape)
    union = np.zeros(needed_shape)
    thresh_avg = np.zeros(needed_shape)

    #threshold = 5 # number of masks which must classify pixel
    count = np.sum(np.array(mask_list), axis=0)
    thresh_avg[count >= threshold] = 1

    for mask in mask_list:
        intersection[~((intersection > 0) & (mask > 0))] = 0
        union[(union > 0) | (mask > 0)] = 1
    
    results[0].imshow(intersection)
    results[0].set_title("intersection")
    results[1].imshow(union)
    results[1].set_title("union")
    results[2].imshow(thresh_avg)
    results[2].set_title("thresh_avg")
    # plt.savefig('jujuBaba.jpg')
    plt.show()

# Function to call the model chosen 
def single_threshold(img, method="kmeans"):
    if method=="kmeans":
        twoDimage = img.reshape((-1,3))
        twoDimage = np.float32(twoDimage)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 2
        attempts=10
        ret,label,center=cv2.kmeans(twoDimage,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)
        center = np.uint8(center)
        res = center[label.flatten()]
        result_image = res.reshape((img.shape))    
        result_image = np.mean(result_image, axis=2)
        result_image = (result_image) < (np.min(result_image) + np.max(result_image))/2
        return result_image
    elif method=="threshold":
        gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        _,thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
        #thresh = thresh > 0
        thresh = (thresh) > (np.min(thresh) + np.max(thresh))/2
        return thresh
    elif method=="otsu":
        img_gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        thresh = threshold_otsu(img_gray)
        img_otsu  = img_gray < thresh
        return img_otsu
    elif method=="u2netp":
        output = remove(img, session=new_session("u2netp"))
        output = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        output = output > 0
        return output

# File path has to be changed below
def time_and_display(file_names, method="u2netp"):
    # print(file_names)
    file_names = file_names[1:]
    print("testing method", method)
    # print(file_names)
    current_directory = os.getcwd()
    images = [cv2.imread(current_directory+"/"+filename) for filename in file_names] #file_names.values()
    # print(images)
    num_plots = len(images) # intersection, union, avg threshold
    f, initial = plt.subplots(1,num_plots) 
    for i in range(num_plots):
        initial[i].axis('off')
        initial[i].imshow(images[i])
    toc1 = time.perf_counter()
    masks = [single_threshold(image[:], method) for image in images]
    combine_masks(masks, threshold=5)
    toc2 = time.perf_counter()
    print(f"all images segment + combine time is {toc2 - toc1:0.4f} seconds")
    toc1 = time.perf_counter()
    single_threshold(images[0][:], method)
    toc2 = time.perf_counter()
    print(f"single image segment time is {toc2 - toc1:0.4f} seconds")

def main(argv=sys.argv):
    time_and_display(argv)
    
if __name__ == "__main__":
    time_and_display(sys.argv)