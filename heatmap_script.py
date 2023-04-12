# run heatmap.py
# run bluescale.py
# run merge_images_bluescale.py

import subprocess

# FOR THIS TO WORK, YOU NEED TO HAVE THE FOLLOWING FILES IN THE SAME DIRECTORY AS THIS SCRIPT:
# heatmap.py - this is the script that generates the heatmap to file heatmap.png
# bluescale.py - this is the script that generates the bluescale heatmap from heatmap.png to file bluescale.png
# merge_images_bluescale.py - this is the script that sets blue channel of photo.png to blue channel of bluescale.png
#                             and saves the result to file merged_image_bluescale.png
# photo.png - this is the background image
# rectangles.txt - this is the input file for heatmap.py

subprocess.run(["python", "heatmap.py"])
subprocess.run(["python", "bluescale.py"])
subprocess.run(["python", "merge_images_bluescale.py"])