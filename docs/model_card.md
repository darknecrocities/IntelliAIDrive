# Model Card: IntelliAIDrive (v1.0)

## Model Description
IntelliAIDrive is a simulation-based hybrid autonomous navigation project that combines traffic sign classification and reinforcement learning for academic experimentation. The system uses a lightweight YOLOv8n classification model to recognize traffic signs and integrates structured sign information into a reinforcement learning environment for downstream decision-making.

## Model Details
- **Model Type:** Traffic Sign Classification + Reinforcement Learning
- **Architecture:**
  - **Traffic Sign Classification:** YOLOv8n Classification
  - **Decision Policy:** Proximal Policy Optimization (PPO) in a Gymnasium-based environment
- **Frameworks Used:** Ultralytics, PyTorch, Gymnasium, Stable-Baselines3, Scikit-learn, OpenCV
- **Pre-trained Weights:** YOLOv8n classification checkpoint

## Intended Use
- **Primary Use Cases:** Simulated traffic sign recognition, structured visual input for RL-based decision-making, and academic evaluation of modular AI pipelines
- **Target Users:** Students, researchers, and academic practitioners exploring hybrid computer vision and reinforcement learning systems
- **Out-of-Scope Use:** This model is **not intended for real-world vehicle deployment, safety-critical driving systems, or production autonomous navigation**

## Training Data
- **Dataset Source:** Kaggle Traffic Sign Dataset
- **Number of Classes:** 58
- **Training Images:** 4,170
- **Test Images:** 1,994
- **Image Size:** 64 × 64 pixels
- **Train-Validation Split:** 80:20

## Performance
- **Evaluation Metrics:** Accuracy, F1-score, Precision, Recall, Confusion Matrix, Precision-Recall Curves
- **Final Results:**
  - **Accuracy:** 95.08%
  - **F1-Score:** 93.38%
  - **Precision:** 92.08%
  - **Recall:** 95.08%

## Evaluation Artifacts
- YOLO training results
- Final metrics bar chart
- Confusion matrix
- Precision-recall curves for selected classes

## Limitations
- The model was evaluated only in controlled academic and simulation-based settings
- Strong classification performance does not guarantee safe real-world driving behavior
- Some traffic sign classes may still be confused when visual features are highly similar
- The reinforcement learning environment simplifies real traffic factors such as pedestrians, weather, sensor noise, and multi-vehicle interaction

## Ethical Considerations
- This project must not be used in real vehicles or safety-critical environments
- Results should be interpreted as proof of concept only
- The system is intended for academic use and controlled experimentation
- Future improvements should include stronger robustness testing, broader datasets, and stricter safety evaluation

## Responsible Use Guidance
Use IntelliAIDrive only for:
- academic coursework
- simulation-based experiments
- research demonstrations
- controlled evaluation of hybrid AI pipelines

Do not use IntelliAIDrive for:
- real-world autonomous driving
- driver assistance on public roads
- any deployment involving human safety