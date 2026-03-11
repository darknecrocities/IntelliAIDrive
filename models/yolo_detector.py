from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
        self.classes = {
            2: 'car',
            0: 'person',
            9: 'traffic light',
            1: 'bicycle',
            3: 'motorcycle',
            5: 'bus',
            7: 'truck'
        }
        self.history = {} # {track_id: [points]}

    def detect(self, frame):
        # Use persist=True for tracking across frames
        results = self.model.track(frame, persist=True, verbose=False)[0]
        detections = []
        
        if results.boxes.id is not None:
            boxes = results.boxes.xyxy.cpu().numpy()
            track_ids = results.boxes.id.int().cpu().numpy()
            class_ids = results.boxes.cls.int().cpu().numpy()
            scores = results.boxes.conf.cpu().numpy()

            for box, track_id, class_id, score in zip(boxes, track_ids, class_ids, scores):
                if int(class_id) in self.classes:
                    x1, y1, x2, y2 = box
                    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                    
                    if track_id not in self.history:
                        self.history[track_id] = []
                    self.history[track_id].append(center)
                    if len(self.history[track_id]) > 30: # Keep last 30 points
                        self.history[track_id].pop(0)

                    detections.append({
                        'bbox': [x1, y1, x2, y2],
                        'score': score,
                        'class': self.classes[int(class_id)],
                        'class_id': int(class_id),
                        'track_id': int(track_id),
                        'history': self.history[track_id]
                    })
        return detections

if __name__ == "__main__":
    detector = YOLODetector()
    print("YOLO Detector initialized.")
