# 🚦 IntelliAIDrive
**Traffic Sign Classification and Reinforcement Learning for Simulated Autonomous Navigation**

IntelliAIDrive is a simulation-based AI project that combines traffic sign classification and reinforcement learning for autonomous navigation research. The system uses a lightweight YOLOv8n classification model to recognize traffic signs, then integrates structured sign information into a reinforcement learning environment for downstream decision-making.

This project was developed as a final requirement for **6INTELSY AY 2025–2026**.

---

## Overview

The goal of IntelliAIDrive is to explore how structured visual recognition can support downstream navigation decisions more effectively than raw image input alone. Instead of forcing the decision-making stage to learn directly from image pixels, the system first performs traffic sign classification and then passes the resulting information into a simulated RL setup.

This modular design makes the pipeline easier to interpret, lighter to train, and more suitable for controlled academic experimentation.

---

## Final Results

The final evaluated model achieved:

- **Accuracy:** 95.08%
- **F1-Score:** 93.38%
- **Precision:** 92.08%
- **Recall:** 95.08%

Additional outputs included:

- YOLO training curves
- Final metrics bar chart
- Confusion matrix
- Precision-recall curves for selected classes

---

## Project Components

- **Traffic Sign Classification:** YOLOv8n classification model trained on a multi-class traffic sign dataset
- **Reinforcement Learning:** PPO-based decision-making in a simulated navigation environment
- **Evaluation:** Accuracy, precision, recall, F1-score, confusion matrix, and class-wise precision-recall analysis
- **Documentation:** Proposal, checkpoint report, final report, ethics statement, and model card

---

## Quick Start

### Run the project

```bash
bash run.sh
```

### Install dependencies manually

```bash
pip install -r requirements.txt
```

---

## Repository Files

- README.md - project overview and quick start
- run.sh - one-command reproduction script
- requirements.txt - environment dependencies
- model_card.md - model details, intended use, and limitations
- ethics_statement.md - risks, mitigations, and responsible-use notes
- data_preprocessing.md - dataset and preprocessing notes
- docs/IntelliAIDrive_Proposal.pdf - proposal
- docs/IntelliAIDrive_Checkpoint_Report.pdf - checkpoint report
- docs/FinalReport.pdf - final report

---

## Documentation

- **Final Report:** docs/FinalReport.pdf
- **Proposal:** docs/IntelliAIDrive_Proposal.pdf
- **Checkpoint Report:** docs/IntelliAIDrive_Checkpoint_Report.pdf
- **Model Card:** model_card.md
- **Ethics Statement:** ethics_statement.md

---

## Team

- Graciella Mhervie D. Jimenez - Project Lead and Integration
- Jenica Sarah B. Tongol - Data and Ethics Lead
- Arron Kian M. Parejas - Modeling Lead
- Jian Kalel D. Marquez - Evaluation and MLOps Lead

---

## Responsible Use

IntelliAIDrive is intended only for:

- academic coursework
- simulation-based experiments
- research demonstrations
- controlled evaluation of hybrid AI pipelines

It is not intended for:

- real-world autonomous driving
- public-road deployment
- safety-critical vehicle control

---

## License

MIT License