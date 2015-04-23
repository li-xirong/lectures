import sys
import os
import math
import numpy as np
from skimage import io, data, img_as_float, img_as_ubyte
import matplotlib.pyplot as plt



def calcHist(gray_im, bins=256):
    hist = [0] * bins
    shift = int(8 - int(math.log(bins,2)))
    h,w = gray_im.shape
    for y in range(h):
        for x in range(w):
            code = gray_im[y,x] >> shift
            hist[code] += 1
            
    return hist
    
    
    
if __name__ == '__main__':
    img = io.imread('landscape.jpg')
    colors = str.split('r g b')
    bins = 256
    
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(13,12))
    
    ax_img = axes[0,0]
    ax_img.imshow(img)
    ax_img.set_axis_off()
    ax_img.set_title('input image')
    
    ax_hist = axes[0,1]
    for i in range(3):
        ax_hist.plot(range(bins), calcHist(img[:,:,i], bins), colors[i])
        ax_hist.set_xlim(0, bins+1)
    ax_hist.set_title('Histogram')
    
    
    for i in range(3):
        ax_img, ax_hist = axes[1+i,:]
        ax_img.imshow(img[:,:,i], cmap=plt.cm.gray)
        ax_img.set_axis_off()
        ax_img.set_title('%s channel' % colors[i])
        ax_hist.plot(range(bins), calcHist(img[:,:,i], bins), colors[i])
        ax_hist.set_xlim(0, bins-1)
        #ax_hist.set_ylim(0, 4000)
    
    ax_hist.set_xlabel('bins')
    
    resfile = '%s.png' % os.path.basename(__file__)
    plt.savefig(resfile, bbox_inches='tight')
 
    
    bins_list = [256, 64, 32, 8]
    fig, axes = plt.subplots(nrows=1, ncols=1+len(bins_list), figsize=(16,2))
    ax_img = axes[0]
    ax_img.imshow(img)
    ax_img.set_axis_off()
    ax_img.set_title('input image')
    
    for i in range(len(bins_list)):
        bins = bins_list[i]
        ax_hist = axes[i+1]
        ax_hist.set_xlim(0, bins-1)
        ax_hist.axes.get_yaxis().set_visible(False)
        ax_hist.set_title('%d bins' % bins)
        for j in range(3):
            ax_hist.plot(range(bins), calcHist(img[:,:,j], bins), colors[j])
        
        
    resfile = '%s-bins.png' % os.path.basename(__file__)
    plt.savefig(resfile, bbox_inches='tight')
            
            
    
    


