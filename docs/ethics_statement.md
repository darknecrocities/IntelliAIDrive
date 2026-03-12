# Ethics Statement: IntelliDrive AI

## Purpose
IntelliDrive AI is designed to demonstrate the potential of computer vision and reinforcement learning in autonomous driving. It is intended for research and educational purposes only.

## Safety & Responsibility
- **Simulation Environment**: This system operates primarily in a simulated environment. Real-world deployment is strictly prohibited without rigorous, multi-stage testing in controlled and regulated settings.
- **Human Oversight**: We advocate for a "human-in-the-loop" approach where human operators maintain ultimate control and can intervene to override autonomous decisions.
- **Fail-safe Logic**: The system implements priority-based rules (e.g., STOP signs and Red Lights trigger immediate braking) to provide a layer of safety above purely learned behaviors.

## Data Ethics
- **Provenance**: The models are trained on publicly available datasets from Kaggle:
    - [Traffic Sign Classification](https://www.kaggle.com/datasets/ahemateja19bec1025/traffic-sign-dataset-classification)
    - [Traffic Signs Detection](https://www.kaggle.com/datasets/pkdarabi/cardetection)
- **Privacy**: We confirm that no Personally Identifiable Information (PII) of real-world drivers, pedestrians, or vehicle owners is stored or processed within this project.
- **Transparency**: We are committed to transparency regarding the limitations of our training data and the potential for bias in detection across different environmental conditions.

## Environmental Impact
- **Optimization**: Training workflows were optimized to minimize computational cycles and associated carbon footprint.
- **Efficiency**: The use of lightweight models like YOLOv8n and shallow CNNs ensures energy-efficient inference during deployment.
