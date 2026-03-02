

import cv2
import mediapipe as mp

# ---------------- INPUT VIDEO ----------------
#input_video = r"C:\Users\Admin\Desktop\MEDIAPIPE\9body_pose_track_input_video\From Main Klickpin CF- Video Pinterest - 5CalUMsit.mp4"
input_video = (r"C:\Users\Admin\Desktop\MEDIAPIPE\9body_pose_track_input_video\From Main Klickpin CF- Video Pinterest - 5CalUMsit.mp4")
# ---------------- OUTPUT VIDEO ----------------
output_video = r"C:\Users\Admin\Desktop\pose_output.mp4"

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(input_video)

# Check if video opened
if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 🔥 Define VideoWriter (Save Output)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        # 🔥 Write processed frame to output video
        out.write(frame)

        cv2.imshow("Pose Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()

print("✅ Processing complete!")
print(f"🎥 Output saved at: {output_video}")


