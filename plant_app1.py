import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("Plant_model.keras")

IMG_SIZE = 224

# Class labels (IMPORTANT)
class_names = {'Pepper__bell___Bacterial_spot': 0, 'Pepper__bell___healthy': 1,
                            'Potato___Early_blight': 2,
              'Potato___Late_blight': 3, 'Potato___healthy': 4,
                            'Tomato_Bacterial_spot': 5, 'Tomato_Early_blight': 6,
              'Tomato_Late_blight': 7, 'Tomato_Leaf_Mold': 8, 'Tomato_Septoria_leaf_spot': 9,
                            'Tomato_Spider_mites_Two_spotted_spider_mite': 10,
              'Tomato__Target_Spot': 11, 'Tomato__Tomato_YellowLeaf__Curl_Virus': 12,
                            'Tomato__Tomato_mosaic_virus': 13, 'Tomato_healthy': 14}

st.title("🌿 Plant Disease Detection AI")
st.write("Upload a leaf image to detect disease")

# Upload image
uploaded_file = st.file_uploader("Choose leaf image...", type=["jpg","png","jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img)/255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    prediction = model.predict(img_array)
    i = np.argmax(prediction)
    predicted_class = [ key for key, value in class_names.items() if value==i]
    confidence = np.max(prediction)*100

    st.success(f"Prediction: {predicted_class}")
    st.info(f"Confidence: {confidence:.2f}%")
