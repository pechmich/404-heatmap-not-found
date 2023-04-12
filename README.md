# 404: heatmap not found
## UnIT project: Error 404: Team Name Not Found
This repository contains scripts that create heatmap from output of previous repository being **rectangles.txt** and **photo.png**. The script **heatmap.py** calculates simple grayscale heatmap from rectangles.txt and puts it into the heatmap.png. The following script is **bluescale.py**, which takes heatmap.png and changes it from shades of gray to shades of blue. In the end, **merge_images_bluescale.py** puts the bluescale heatmap from bluescale.png onto the blue channel of photo.png and exports it to **merged_image_bluescale.png**.

There is also **heatmap_script.py** script, which runs all three of the previous scripts in the correct order.

### Necessary modules for python:
- numpy
- cv2 (OpenCV)
- Image from PIL (Pillow)

### Output example:
![heatmap](https://user-images.githubusercontent.com/105096216/231484151-c8f60af2-0efd-40cc-a3d8-19c769d09f0c.png)
*heatmap.png*
![bluescale](https://user-images.githubusercontent.com/105096216/231484352-3da65f6b-a637-4419-bd56-fbf0823a5fed.png)
*bluescale.png*
![merged_image_bluescale](https://user-images.githubusercontent.com/105096216/231484609-bf1f9049-187d-44ad-9a9d-3d285341dc05.png)
*merged_image_bluescale.png*

*from input:*
[rectangles.txt](https://github.com/pechmich/404-heatmap-not-found/files/11212343/rectangles.txt)
*and*
![photo](https://user-images.githubusercontent.com/105096216/231485095-55ef2cae-7c8d-401a-a6db-6453e5d67639.png)
*photo.png*
