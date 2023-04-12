import numpy as np
from PIL import Image

photo = 'photo2.png'
heatmap = 'bluescale.png'

# Load the background and foreground files
photo = np.array(Image.open(photo))
heatmap = np.array(Image.open(heatmap))

# set the blue channel of the photo to the blue channel of the heatmap
photo[..., 2] = heatmap[..., 2]

# save the merged image
Image.fromarray(photo).save('merged_image_bluescale.png')