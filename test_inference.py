import cv2
from ultralytics import YOLO
import sys

def test():
    print("Testing custom model...")
    model_path = 'experiments/runs/detect/train2/weights/best.pt'
    custom_model = YOLO(model_path)

    cap = cv2.VideoCapture('data/sample3.mp4')
    # Read a few frames in to avoid a blank start
    for _ in range(30):
        ret, frame = cap.read()
    
    if not ret:
        print("Failed to read sample3.mp4")
        sys.exit(1)
        
    results_custom = custom_model(frame, verbose=False)[0]
    print(f"Custom model ({model_path}): Found {len(results_custom.boxes)} detections")
    if len(results_custom.boxes) > 0:
        print(f"Classes: {[custom_model.names[int(c)] for c in results_custom.boxes.cls.cpu().numpy()]}")

    print("\nTesting base model...")
    base_model = YOLO('yolov8n.pt')
    results_base = base_model(frame, verbose=False)[0]
    print(f"Base model (yolov8n.pt): Found {len(results_base.boxes)} detections")
    if len(results_base.boxes) > 0:
        print(f"Classes: {[base_model.names[int(c)] for c in results_base.boxes.cls.cpu().numpy()]}")

if __name__ == '__main__':
    test()

