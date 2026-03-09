# 🌿 Plant Disease Detection using CNN

This project detects plant diseases from leaf images using a **Convolutional Neural Network (CNN)** trained on the **PlantVillage dataset**.  
The model uses **MobileNetV2 (Transfer Learning)** as the base model to improve accuracy and efficiency.

## 📂 Project Structure

```text
project/
│
├── dataset/
│   ├── train/
│   ├── test/
│   └── validation/
│
├── Plant_model_1.ipynb   # Model training notebook
├── plant_app1.py         # Streamlit web app
├── Plant_model.keras     # Trained model
└── README.md
```


## 📊 Dataset

Dataset used: **PlantVillage**

https://www.kaggle.com/datasets/moazeldsokyx/plantvillage

The dataset contains images of **healthy and diseased plant leaves** used to train, validate, and test the model.

## 🧠 Model

- Base Model: **MobileNetV2**
- Technique: **Transfer Learning**
- Framework: **TensorFlow / Keras**

## ⚙️ Required Libraries

numpy
pandas
tensorflow
opencv-python (cv2)
matplotlib
scipy
streamlit
os


Install dependencies : pip install numpy pandas tensorflow opencv-python matplotlib scipy streamlit


## 🚀 Run the Project

1. Train the model using:
Plant_model_1.ipynb


2. Run the Streamlit app:
streamlit run plant_app1.py


3. Upload a plant leaf image to get the **disease prediction**.

## 👨‍💻 Author

Deep Learning project for **plant disease classification using CNN**.
