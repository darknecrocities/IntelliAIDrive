# Model Card: IntelliDrive AI Sign Recognition & Detection

## Model Details
- **Classification Model**: TrafficSignCNN (Custom CNN architecture)
    - **Architecture**: Conv2D -> BatchNorm -> ReLU -> MaxPool -> GAP -> FC
    - **Library**: PyTorch
    - **Input Size**: 32x32 pixels
- **Detection Model**: YOLOv8n (Pre-trained and Fine-tuned)
    - **Library**: Ultralytics YOLO

## Dataset Details
- **Classification Dataset**: [Traffic Sign Dataset Classification](https://www.kaggle.com/datasets/ahemateja19bec1025/traffic-sign-dataset-classification)
    - **Size**: ~58 distinct classes, ~120 images per class.
    - **Total**: ~7,000 images including ~2,000 test samples.
- **Detection Dataset**: [Cardetection / Traffic Signs Detection](https://www.kaggle.com/datasets/pkdarabi/cardetection)
    - **Size**: 4,969 image samples at 640x640 resolution.
    - **Classes**: 55 unique classes categorized into forbidden, informational, mandatory, and warning.

## Intended Use
- Real-time traffic sign recognition and object detection for autonomous driving simulations.
- Educational demonstration of AI in automotive systems.

## Metrics
- **CNN Accuracy**: ~95%
- **Detection Performance**: Real-time inference capability with YOLOv8n.

## Limitations
- Sensitive to low-light and adverse weather conditions.
- Limited to specific sign types contained in the training data.
- Not for use in real-world safety-critical vehicles without extensive validation.

## Responsible Deployment Guidelines
- Always include human-in-the-loop overrides.
- Use multi-modal sensors for redundancy in production environments.
- Regular audits for detection accuracy across diverse environmental contexts.
