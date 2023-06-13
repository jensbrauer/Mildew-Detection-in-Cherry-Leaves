import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image

def size_img_for_model(img):
    """
    Reshape image to average image size
    """
    img_model_shape = (75, 75, 3)
    img_display_shape = (200, 200, 3)
    #image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    img_display_resized = img.resize((img_display_shape[1], img_display_shape[0]), Image.ANTIALIAS)
    display_input_img = np.expand_dims(img_display_resized, axis=0)/255
    
    img_model_resized = img.resize((img_model_shape[1], img_model_shape[0]), Image.ANTIALIAS)
    model_input_img = np.expand_dims(img_model_resized, axis=0)/255

    return model_input_img, display_input_img

def predict(img):

    model = load_model("outputs/deployed_version/mildew_detection_model.h5")
    prediction = model.predict(img)[0, 0]
    if prediction > 0.5:
        return 'Healthy', prediction
    else:
        return 'Powdery_Mildew', (1 - prediction)