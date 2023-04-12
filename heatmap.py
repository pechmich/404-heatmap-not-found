import numpy as np
import cv2
import matplotlib.pyplot as plt

filename = 'rectangles.txt'

height = 720
width = 1280

# read rectangles from input file
rectangles = []
with open(filename, 'r') as f:
    for line in f:
        rect = tuple(map(int, line.strip().split(',')))
        rectangles.append(rect)

# Create an empty image with the same dimensions as the heatmap
heatmap = np.zeros((720, 1280), dtype=np.float32)

for rect in rectangles:
    x1, y1, x2, y2 = rect
    # Add 1 to each pixel in the rectangle
    heatmap[y1:y2, x1:x2] += 1

# for every pixel in the heatmap, decrease its value to 255 if it is greater than 255
heatmap[heatmap > 255] = 255

# Scale the array to the range [0, 255]
arr = heatmap.astype(np.uint8)

# Save the array as an image in shades of gray
cv2.imwrite("heatmap.png", arr)