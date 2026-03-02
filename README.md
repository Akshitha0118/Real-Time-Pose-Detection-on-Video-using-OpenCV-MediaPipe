# Real-Time Pose Detection on Video using OpenCV & MediaPipe 
This project is based on Computer Vision project where I implemented Human Pose Detection on a video file using OpenCV and MediaPipe in Python 

## ==> What This Project Does:
- Reads an input video
- Detects human body landmarks frame-by-frame
- Draws pose skeleton connections
- Saves the processed output as a new video file
- Displays real-time pose tracking

## ==> Tech Stack Used:
- Python
- OpenCV (Video processing & display)
- MediaPipe Pose (Body landmark detection)

## ==> How It Works (Step-by-Step):
- Capture video using cv2.VideoCapture()
- Convert BGR → RGB (required for MediaPipe processing)
- Process each frame using mp_pose.Pose()
- Draw pose landmarks using drawing utilities
- Save processed frames using cv2.VideoWriter()
- Export final output video 

##  This project helped me understand:
 - Frame-by-frame video processing
 - Landmark detection confidence tuning
 - Performance optimization in OpenCV
 - Real-time computer vision pipelines
