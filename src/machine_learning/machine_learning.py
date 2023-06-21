import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
import pickle

def size_img_for_model(img):
    """
    Reshape image to average image size
    """



    img_display_shape = (200, 200, 3)
    img_display_resized = img.resize((img_display_shape[1], img_display_shape[0]), Image.LANCZOS)
    display_input_img = np.expand_dims(img_display_resized, axis=0)/255
    

    with open("outputs/current_output/image_size.pkl", 'rb') as file:
        img_model_shape = pickle.load(file)

    #img_model_shape = (75, 75, 3)
    img_model_resized = img.resize((img_model_shape[1], img_model_shape[0]), Image.LANCZOS)
    model_input_img = np.expand_dims(img_model_resized, axis=0)/255

    return model_input_img , display_input_img

def predict(img, model_version):

    model = load_model(f"outputs/{model_version}/mildew_detection_model.h5")
    prediction = model.predict(img)[0, 0]
    if prediction > 0.5:
        return 'Healthy', prediction
    else:
        return 'Powdery_Mildew', (1 - prediction)



import os
import base64
from datetime import datetime
import joblib


def download_report(df):

    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" '
        f'target="_blank">Download Report as CSV</a>'
    )
    return href