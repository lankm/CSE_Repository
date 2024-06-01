# Assignment 1

Author: Landon Moon
Student ID: 1001906270

## pip list output

 - numpy         1.26.3  
 - opencv-python 4.9.0.80
 - pillow        10.2.0     (https://pillow.readthedocs.io/en/latest/installation.html)
 - pip           23.3.2

I used pillow to read and save images. If there are any problems with installing the library, my img_to_arr() and save_as_img() functions are located in assignment1_lib.py. The implementation is pretty basic so in case that pillow is unable to be used, the functions can be changed accordingly.

## changes of note
 - **color_space_test.py**
   - Some changes to the input range for the first part of the assignment. More information is located at the top of the code file. allowing a modification of -1 allows the saturation to become 0 which would be impossible with the original range.
 - **img_transforms.py**
   - A main function is provided to help with the execution of the required functions. I don't want to implement a naive bash-like shell so the img_transforms.py recieves a filename from the command line and other function arguments are defined in main()
   - All the defined functions within img_transforms.py can accept a tuple as 'size' input instead of just a scalar. More information is located at the top of the code file.
   - I implemented as many of the functions to work on as many types of images (non-square and non-power of 2). Extensive testing is a pain but this isn't for a production system.
   - resize_img() is not vectorized so it will take a while for large images. This wasn't a requirement, just that the other functions are vectorized.
 - **create_img_pyramid**
   - The create_img_pyramid.py function implements a recursive averaging technique instead of '[my] own version of a resize function from the first section'. Its faster and because its calculating means instead of implementing nearest neighbor, so the resulting image is more accurate.
   




Also I'm including a kirby.jpg image in the zip for the fun of it. I used it for testing.
