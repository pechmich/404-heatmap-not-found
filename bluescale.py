from PIL import Image

# Open the image and convert it to RGB mode
img = Image.open('heatmap.png').convert('RGB')

# Create a new empty image of the same size
blue_img = Image.new('RGB', img.size)

# Loop through each pixel in the image and set the blue channel value
for x in range(img.width):
    for y in range(img.height):
        # get the pixel value
        _, _, b = img.getpixel((x, y))

        # Set the blue channel value to the original grayscale value
        blue_img.putpixel((x, y), (0, 0, b))


# Save the new image as a PNG file
blue_img.save('bluescale.png')