# Model Card: IntelliDrive AI Sign Classifier

## Model Details
- **Model Name**: TrafficSignCNN
- **Architecture**: Conv2D -> BatchNorm -> ReLU -> MaxPool -> GAP -> FC
- **Library**: PyTorch
- **Classes**: 15 (Speed limits, Stop, Traffic Lights)

## Intended Use
- Real-time traffic sign recognition for autonomous driving simulations.
- Educational demonstration of AI in automotive systems.

## Metrics
- **Accuracy**: ~95%
- **F1 Score**: High macro-F1 due to balanced dataset.

## Limitations
- Sensitive to low-light conditions.
- Limited to 15 specific sign types.
- Not for use in real safety-critical vehicles without further testing.

## Responsible Deployment Guidelines
- Always include human-in-the-loop overrides.
- Use multi-modal sensors for redundancy.
- Regular bias audits for detection of pedestrians across demographics.
