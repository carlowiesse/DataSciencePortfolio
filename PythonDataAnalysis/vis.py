import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.font_manager import fontManager


#++++  Functions  ++++#

def print_available_fonts():
    for fn in sorted(set([f.name for f in fontManager.ttflist])): print(fn)

def plot_image(img,save=False):
    fig,ax = plt.subplots(1,1,figsize=(16,9))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
    ax.set(xticks=[], yticks=[], frame_on=False)
    ax.imshow(img, cmap='jet' if img.shape[2:] else 'gray')
    if save: plt.savefig('image.jpg', dpi=40)
    plt.show()
    
def plot_intensity(img):
    x,y,z = zip(*[(i,j,k) for i,row in enumerate(img) for j,k in enumerate(row)])
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x,y,z,c=z,s=5, cmap='gray', depthshade=False)
    plt.show()
    
def visualize_operation(data,skip=2,f=np.mean):
    fig, axs = plt.subplots(3,3,figsize=(16,9))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
    for axrow in axs:
        for ax in axrow:
            ax.set(xticks=[], yticks=[], frame_on=False)
    images = data[:3*skip+1:skip]
    for i in range(1,4):
        result = f(images[:i+1:i],axis=0)
        axs[i-1,0].imshow(images[i], cmap='gray')
        axs[i-1,1].imshow(result, cmap='coolwarm')
        axs[i-1,2].imshow(images[0], cmap='gray')
    plt.tight_layout(pad=-0.3,h_pad=-0.5, w_pad=-0.45)
    plt.show()

