# 🚦 IntelliDrive AI
### Traffic Sign Recognition + Reinforcement Learning Driving Agent

IntelliDrive AI is a full-stack autonomous driving simulation platform. It uses Computer Vision to detect signs and objects, NLP to interpret rules, and Reinforcement Learning to navigate safely.

## 🚀 Getting Started

### 1. Unified Run (Backend + Frontend)
```bash
bash run.sh
```

### 2. Standalone Python Detection CLI
Run real-time detection directly in a window:
```bash
python3 src/video_cli.py
```

## 🏗️ Architecture
- **Vision**: CNN (PyTorch) for signs + YOLOv8 for objects.
- **NLP**: Rule-based sign interpreter.
- **RL**: DQN Agent in a custom GridWorld environment.
- **Backend**: FastAPI.
- **Frontend**: React + Tailwind + Framer Motion.

## 📁 Repository Structure
```
intellidrive-ai/
├── src/           # Backend source
├── models/        # ML Models
├── rl/            # RL Logic
├── frontend/      # React App
├── data/          # Dataset
└── docs/          # Documentation
```

## 📄 License
MIT
