# FULL-PROJECT-SUBMISSION SIZE IS 125 MB IS NOT SUPPORTED TO GITHUB SO ONLY( IPYNB FILE) IS UPLOADED
E-Waste-Classification-Project/
Main directory containing the full AI-based e-waste classification system.

php
Copy
Edit
E-Waste-Classification-Project/
├── 📁 data/                         # Dataset folder (train/val/test images)
│
├── 📁 models/                       # Trained model storage
│   └── efficientnetv2b0_e_waste.keras
│
├── 📁 samples/                      # Sample images for VR-like webcam gestures
│   └── sample1.jpg, sample2.png, ...
│
├── 📁 static/                       # Stores prediction logs and captured images
│   ├── images/                     # Saved prediction images
│   └── predictions.csv             # Log file with timestamp, label, cost, recommendation
│
├── 📁 utils/                        # Custom Python utility scripts
│   ├── cost_estimator.py           # Returns estimated recycling cost per item
│   └── recommendation_engine.py    # Gives safe disposal and recycling tips
│
├── 📄 E-Waste Generation Classification.ipynb  # 📌 Main notebook (all-in-one execution)
│                                        • Model training with EfficientNetV2B0  
│                                        • Gradio UI for prediction  
│                                        • Cost estimation and recommendations  
│                                        • Dashboard preview and logging  
│
├── 📄 captured.jpg                  # Sample captured image from webcam (IP/webcam)
├── 📄 requirements.txt              # Dependencies (tensorflow, gradio, opencv, etc.)
│
├── 📁 .gradio/                      # (Auto-created by Gradio)
├── 📁 .ipynb_checkpoints/           # (Jupyter autosave folder)
 Optional Notes for Report:
main notebook: Combine all features in one place (.ipynb)

samples/: Used by VR-gesture script to classify based on hand signals

utils/: Makes code modular, reusable, and readable

static/predictions.csv: Used in dashboard tab to show prediction history
Notebook Contents (Sections)
1.  Library Installation and Imports
tensorflow, gradio, opencv-python-headless, matplotlib, seaborn, etc.

EfficientNetV2B0 used for model backbone.

2.  Data Loading and Preprocessing
Data organized under data/train, data/val, data/test.

Uses ImageDataGenerator for augmentation.

Batch size: 32 | Image size: 224x224

3.  EDA (Exploratory Data Analysis)
Shows sample images from training dataset.

Counts number of images per class using os and collections.Counter.

4.  Model Building (EfficientNetV2B0)
Loads base EfficientNetV2B0 without top layer.

Adds custom classification layers (GlobalAveragePooling2D, Dense).

Final layer: 10 classes with softmax.

5. 🎯 Model Training
Uses EarlyStopping and ModelCheckpoint.

Loss: categorical_crossentropy

Optimizer: adam

Epochs: around 15–25 (assumed from later content)

6. ✅ Model Evaluation
Evaluates using classification_report and confusion_matrix.

Displays confusion matrix using ConfusionMatrixDisplay.

7.  Save Trained Model
Model saved to models/efficientnetv2b0_e_waste.keras.

8.  Gradio-Based Upload + Webcam Prediction
Interactive Gradio UI for:

Uploading an image

Capturing via webcam

Displays:

Predicted class

Estimated cost

Recycling recommendation

Prediction log saved in static/predictions.csv.

9. 📈 Prediction History Logging
Shows prediction history in tabular format using Pandas.

Option to clear logs using Gradio button.

10.  VR Gesture-Based Classifier (OpenCV + MediaPipe)
Uses webcam + MediaPipe to:

Switch sample images using ✋ (5 fingers)

Classify using 👍 (thumb up)

Displays result and recommendation live via OpenCV window.

11.  Final Summary
The notebook concludes with a prediction interface, logging, and full model deployment—all wrapped in one file for ease of demonstration and testing.

