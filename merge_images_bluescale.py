import numpy as np
from PIL import Image

photo = 'photo2.png'
heatmap = 'bluescale.png'

# Load the background and foreground files
photo = np.array(Image.open(photo))
heatmap = np.array(Image.open(heatmap))

# get the blue channel of the photo and heatmap arrays
blue_channel_photo = photo[..., 2]
blue_channel_heatmap = heatmap[..., 2]

# add the blue channel of the heatmap to the blue channel of the photo
new_blue_channel = blue_channel_photo + blue_channel_heatmap

# set the values of the new blue channel to a maximum of 255
new_blue_channel[new_blue_channel < blue_channel_heatmap] = 255

# create a copy of the photo array and update the blue channel with the new blue channel values
new_photo_array = photo.copy()
new_photo_array[..., 2] = new_blue_channel

# save the merged image
Image.fromarray(new_photo_array).save('merged_image_bluescale.png')