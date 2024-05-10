import numpy as np
import matplotlib.pyplot as plt
import cv2

COLORS = np.array([
    (255, 204, 204),  # Light Pink
    (204, 255, 204),  # Light Green
    (204, 204, 255),  # Light Blue
    (255, 255, 204),  # Light Yellow
    (255, 204, 255),  # Light Purple
    (204, 255, 255),  # Light Cyan
    (255, 230, 204),  # Light Orange
    (230, 204, 255),  # Light Lavender
    (204, 255, 230),  # Light Mint
    (255, 204, 230)   # Light Coral
])


def get_mask(mask):
    color = np.random.choice(COLORS)
    print(color)
    color = np.array(COLORS[color]) 
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    return mask_image
    
def show_points(coords, labels, ax, marker_size=375):
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)   
    
def show_box(box, ax):
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))    
