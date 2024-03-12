# Assignment 3
- Landon Moon
- 1001906270

## Execution instructions
As stated in the assignment description I started with the qtdemo code. This means that pyside2 is required along with its dependency of ffmpeg and python 3.10 or lower. Other than that the only dependencies are scikit-image and scikit-video.

The executable is: qtvideo.py

The GUI will show some extra information that is extracted from the video. Red boxes are candidates. Black dots are inactive candidates. Blue dots/lines are active tracked objects.

## Notes on Implementation
As of writing, the program 'works' and you are able to see tracked objects and a line of where they have been. I still need to do a full pass through the code and consider edge cases.

I am assuming that 'frames_to_skip' implies an iterative solution to update up to a given frame. When I implemented this it can be fairly slow if it is updating every frame. I should optimize it.

During the update step of a kalman filter, I decided to not save the state as a vector as shown in the notes. This is done so position is separated from velocity for the GUI aspect of the program. Secondly, I think I deviated from the exact update equation. Due to not knowing acceleration due to blob noise, I decided to implement an (1-a)*... + (a)*... approach. This still updates with the provided position of the matched point but doesn't assume it is completly correct. Sometimes blobs from the detection stage can join together and cause a matched point to still match but move suddenly. By having an alpha factor, the kalman filter smooths out the acceleration of the object. This gave better results from what I tested but might be worse in some scenarios. Sorry if this deviates from the inteded solution too much.

## Example
![alt text](image.png)

### Hyperparameters
- frame_hysteresis=16
- motion_threshold=10
- distance_threshold=20
- frames_to_skip=4
- max_objects=100
- blob_size=4
- alpha=0.5 described in section above