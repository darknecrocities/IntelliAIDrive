import cv2
import sys
import os

# Add the project root to sys.path to allow imports from models and src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.video_processor import VideoProcessor

def main(video_path="dataset/video.mp4"):
    if not os.path.exists(video_path):
        print(f"Error: {video_path} not found.")
        return

    print(f"Starting real-time detection on {video_path}...")
    print("Press 'q' to exit.")

    processor = VideoProcessor(video_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Create the window explicitly
    window_name = 'IntelliDrive AI - Real-time Detection'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    
    # Try to bring the Python/OpenCV window to the front on macOS
    try:
        os.system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "python3" to true' ''')
    except:
        pass

    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Video ended or failed to read frame. Restarting...")
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        # Process frame
        annotated_frame, detections = processor.process_frame(frame)
        frame_count += 1
        
        if frame_count % 10 == 0:
            print(f"Processed {frame_count} frames...")

        # Show frame
        cv2.imshow(window_name, annotated_frame)

        # Break on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Execution finished.")

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "dataset/sample3.mp4"
    main(path)
