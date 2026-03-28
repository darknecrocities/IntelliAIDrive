# Data Preprocessing Notes: IntelliAIDrive

## Overview
This document summarizes the dataset preparation and preprocessing steps used in IntelliAIDrive. The project uses a traffic sign classification dataset for academic experimentation in traffic sign recognition and simulation-based reinforcement learning.

## Dataset Summary
- **Dataset Source:** Kaggle Traffic Sign Dataset
- **Number of Classes:** 58
- **Training Images:** 4,170
- **Test Images:** 1,994
- **Image Size Used for Training:** 64 × 64 pixels

The dataset consists of labeled traffic sign images organized by class. Each class corresponds to a specific traffic sign category.

## Preprocessing Steps

### 1. Image Organization
The dataset was organized by class to support supervised traffic sign classification. Images were grouped into class-specific folders, allowing the model to learn category-level differences across the 58 classes.

### 2. Image Resizing
All images were resized to **64 × 64 pixels** before training. This input resolution was selected to reduce computational cost while preserving the relevant visual structure of traffic sign symbols and shapes.

### 3. Train-Validation Split
For the YOLOv8n classification stage, the training data was split using an approximate **80:20 train-validation ratio**, resulting in:
- **3,313 training images**
- **857 validation images**

This helped monitor learning progress and reduced the risk of evaluating the model only on seen samples.

### 4. Test Set Usage
A separate test set containing **1,994 images** was used for final evaluation. This ensured that the reported performance metrics reflected the model’s behavior on unseen data.

### 5. Data Consistency
The preprocessing pipeline maintained class-level consistency across the dataset. This reduced leakage between splits and supported more reliable evaluation of the classifier’s generalization ability.

## Training-Oriented Preparation
The preprocessed images were used as input to a **YOLOv8n classification model**. Because the project focused on traffic sign classification rather than bounding box localization, the preprocessing pipeline was designed for whole-image classification rather than object detection.

## Notes on Augmentation
Training included built-in augmentation settings available in the training framework, such as standard color and spatial variation. These augmentations were intended to improve generalization and reduce overfitting under controlled academic conditions.

## Summary
The final preprocessing setup supported a lightweight and efficient classification pipeline by:
- organizing images by class
- resizing all inputs to 64 × 64
- maintaining train, validation, and test separation
- supporting reproducible model training and evaluation