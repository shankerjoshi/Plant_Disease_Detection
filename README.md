# 🌿 Plant Disease Detection

A deep learning project that detects diseases in plant leaves from images. Upload a photo of a leaf and the model tells you what disease it has (or if it's healthy).

Built using a CNN with MobileNetV2 transfer learning, trained on the PlantVillage dataset. Comes with a Streamlit web app so you can actually use it without touching any code.

---

## 📂 Project Structure

```
Plant_Disease_Detection/
├── Plant_model_1.ipynb     # notebook used to train the model
├── plant_app1.py           # Streamlit web app
├── Plant_model.keras       # trained model (ready to use)
├── requirements.txt        # dependencies
├── .gitignore
└── README.md
```

The `dataset/` folder is not included here — you need to download it separately (see below).

---

## ⚙️ Setup

### 1. Clone the repo

```
git clone https://github.com/shankerjoshi/Plant_Disease_Detection.git
cd Plant_Disease_Detection
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. 📊 Download the dataset (only needed if you want to retrain)

Dataset: [PlantVillage on Kaggle](https://www.kaggle.com/datasets/moazeldsokyx/plantvillage)

After downloading, place it like this:

```
dataset/
├── train/
├── test/
└── validation/
```

---

## 🚀 Running the app

The trained model is already included (`Plant_model.keras`), so you can run the app directly without retraining:

```
streamlit run plant_app1.py
```

Then open the link it gives you in your browser, upload a leaf image, and it will predict the disease.

---

## 🧠 Retraining the model

If you want to train it yourself, open the notebook:

```
jupyter notebook Plant_model_1.ipynb
```

Make sure the dataset is downloaded and placed in the `dataset/` folder first. Run all the cells in order — it will save a new `Plant_model.keras` at the end.

---

## 🛠️ Tech used

- TensorFlow / Keras
- MobileNetV2 (transfer learning)
- Streamlit
- OpenCV
- PlantVillage dataset

---

## 📝 Notes

- The model works best with clear, well-lit photos of individual leaves
- Images that are blurry, have multiple leaves, or show only stems may give inaccurate results
- Dataset is not included in the repo due to its size — download it from the Kaggle link above
