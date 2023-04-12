import numpy as np
import cv2
import matplotlib.pyplot as plt

# Generate an array of 100 random rectangles
rectangles = np.random.randint(0, 300, size=(100, 4))

# Ensure that the left-bottom points are less than the right-upper points
rectangles[:, 2:] = np.maximum(rectangles[:, :2], rectangles[:, 2:])

print(rectangles)

# Create an empty image with the same dimensions as the heatmap
heatmap = np.zeros((300, 300), dtype=np.float32)

for rect in rectangles:
    x1, y1, x2, y2 = rect
    # Add 1 to each pixel in the rectangle
    heatmap[y1:y2, x1:x2] += 1

# Create a heatmap plot of the data
fig, ax = plt.subplots()
im = ax.imshow(heatmap, cmap='gray')

# Add a colorbar to show the mapping of values to grayscale colors
cbar = ax.figure.colorbar(im, ax=ax)

# Set the title and axis labels
ax.set_title("Grayscale Heatmap")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Display the plot
plt.show()