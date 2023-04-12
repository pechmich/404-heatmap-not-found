from PIL import Image

# Load the background and foreground images
photo = Image.open("photo2.png")
heatmap = Image.open("heatmap.png")

# Resize the foreground image to match the size of the background image
heatmap = heatmap.resize(photo.size)

# convert the photo to RGBA
photo = photo.convert("RGBA")

# convert the heatmap to RGBA
heatmap = heatmap.convert("RGBA")

# Create a new image with an alpha channel
merged_image = Image.new("RGBA", photo.size)

# Blend the images using alpha blending
merged_image = Image.blend(photo, heatmap, 0.5)

# Adjust the transparency of the foreground image
merged_image.putalpha(128)

# Save the merged image
merged_image.save("merged_image.png")