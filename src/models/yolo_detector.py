from ultralytics import YOLO
import cv2

class YOLODetector:
    def __init__(self, base_model_path='yolov8n.pt'):
        import os
        
        # Base model for general objects (cars, people, traffic lights)
        self.base_model = YOLO(base_model_path)
        self.base_classes = {
            2: 'car', 0: 'person', 9: 'traffic light',
            1: 'bicycle', 3: 'motorcycle', 5: 'bus', 7: 'truck'
        }
        
        # Custom model for traffic signs
        custom_model_path = 'experiments/runs/detect/train2/weights/best.pt'
        self.sign_model = None
        if os.path.exists(custom_model_path):
            self.sign_model = YOLO(custom_model_path)
            self.sign_classes = self.sign_model.names
            print("Dual-model active: Base (Objects) + Custom (Traffic Signs)")
            
        self.history = {} # {track_id: [points]}
        self.sign_id_counter = 10000 # Dummy IDs for signs

    def detect(self, frame):
        detections = []
        
        # 1. Track general objects with base model
        results_base = self.base_model.track(frame, persist=True, verbose=False)[0]
        if results_base.boxes.id is not None:
            boxes = results_base.boxes.xyxy.cpu().numpy()
            track_ids = results_base.boxes.id.int().cpu().numpy()
            class_ids = results_base.boxes.cls.int().cpu().numpy()
            scores = results_base.boxes.conf.cpu().numpy()

            for box, track_id, class_id, score in zip(boxes, track_ids, class_ids, scores):
                if int(class_id) in self.base_classes:
                    x1, y1, x2, y2 = box
                    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                    
                    if track_id not in self.history:
                        self.history[track_id] = []
                    self.history[track_id].append(center)
                    if len(self.history[track_id]) > 30:
                        self.history[track_id].pop(0)

                    detections.append({
                        'bbox': [x1, y1, x2, y2],
                        'score': score,
                        'class': self.base_classes[int(class_id)],
                        'class_id': int(class_id),
                        'track_id': int(track_id),
                        'history': self.history[track_id]
                    })
                    
        # 2. Detect traffic signs with custom model
        if self.sign_model:
            results_sign = self.sign_model.predict(frame, verbose=False)[0]
            if len(results_sign.boxes) > 0:
                s_boxes = results_sign.boxes.xyxy.cpu().numpy()
                s_class_ids = results_sign.boxes.cls.int().cpu().numpy()
                s_scores = results_sign.boxes.conf.cpu().numpy()
                
                for box, class_id, score in zip(s_boxes, s_class_ids, s_scores):
                    x1, y1, x2, y2 = box
                    center = (int((x1 + x2) / 2), int((y1 + y2) / 2))
                    
                    # Generate a loose dummy track ID for the sign
                    simulated_id = self.sign_id_counter
                    self.sign_id_counter += 1
                    
                    detections.append({
                        'bbox': [x1, y1, x2, y2],
                        'score': score,
                        'class': self.sign_classes[int(class_id)],
                        'class_id': int(class_id),
                        'track_id': simulated_id,
                        'history': [center, center] # Dummy history to draw simple box
                    })
                    
        return detections

if __name__ == "__main__":
    detector = YOLODetector()
    print("YOLO Detector initialized.")
