import cv2
from src.models.yolo_detector import YOLODetector
from src.models.cnn_sign_classifier import TrafficSignCNN
from src.models.nlp_interpreter import NLPInterpreter
import torch
from torchvision import transforms
from PIL import Image

class VideoProcessor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.detector = YOLODetector()
        self.classifier = TrafficSignCNN()
        # Load weights if available, otherwise use dummy
        # self.classifier.load_state_dict(torch.load('models/cnn_weights.pth'))
        self.classifier.eval()
        self.nlp = NLPInterpreter()
        self.transform = transforms.Compose([
            transforms.Resize((32, 32)),
            transforms.ToTensor(),
        ])
        self.classes = ['Green Light', 'Red Light', 'Speed Limit 10', 'Speed Limit 100', 'Speed Limit 110', 'Speed Limit 120', 'Speed Limit 20', 'Speed Limit 30', 'Speed Limit 40', 'Speed Limit 50', 'Speed Limit 60', 'Speed Limit 70', 'Speed Limit 80', 'Speed Limit 90', 'Stop']

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        annotated_frame = frame.copy()
        
        # Color map for classes
        import hashlib
        def get_color(label):
            hash_obj = hashlib.md5(label.encode('utf-8'))
            color = tuple(int(hash_obj.hexdigest()[i:i+2], 16) for i in (0, 2, 4))
            return color

        # Store centers per class for connecting lines
        class_centers = {}

        for det in detections:
            x1, y1, x2, y2 = map(int, det['bbox'])
            label = det['class']
            track_id = det['track_id']
            history = det['history']
            
            color = get_color(label)
            
            # Center of the bounding box
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            if label not in class_centers:
                class_centers[label] = []
            class_centers[label].append((center_x, center_y))
            
            # Draw track lines (history)
            if len(history) > 1:
                for i in range(1, len(history)):
                    cv2.line(annotated_frame, history[i-1], history[i], color, 2)
            
            # Draw bounding box
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(annotated_frame, f"{label} #{track_id}", (x1, y1-10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Draw connecting lines between same objects
        import math
        for label, centers in class_centers.items():
            color = get_color(label)
            if len(centers) > 1:
                # Connect each object of the same class
                for i in range(len(centers)):
                    for j in range(i + 1, len(centers)):
                        pt1 = centers[i]
                        pt2 = centers[j]
                        dist = math.dist(pt1, pt2)
                        
                        # Only draw line if reasonably close, to avoid screen clutter, or just draw all
                        cv2.line(annotated_frame, pt1, pt2, color, 1, cv2.LINE_AA)
                        
                        # Put distance text in the middle
                        mid_x = (pt1[0] + pt2[0]) // 2
                        mid_y = (pt1[1] + pt2[1]) // 2
                        cv2.putText(annotated_frame, f"{int(dist)}px", (mid_x, mid_y), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

        return annotated_frame, detections


if __name__ == "__main__":
    print("Video Processor initialized.")
