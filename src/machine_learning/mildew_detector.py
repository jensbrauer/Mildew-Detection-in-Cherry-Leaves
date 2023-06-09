import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import pickle
import base64
from datetime import datetime


def size_img_for_model(img, model_version):
    img_display_shape = (200, 200, 3)
    img_display_resized = img.resize((img_display_shape[1], img_display_shape[0]), Image.LANCZOS)
    display_input_img = np.expand_dims(img_display_resized, axis=0)/255
    
    with open(f"outputs/{model_version}/image_size.pkl", 'rb') as file:
        img_model_shape = pickle.load(file)

    img_model_resized = img.resize((img_model_shape[1], img_model_shape[0]), Image.LANCZOS)
    model_input_img = np.expand_dims(img_model_resized, axis=0)/255
    return model_input_img , display_input_img


def predict(img, model_version):
    model = load_model(f"outputs/{model_version}/mildew_detection_model.h5")
    prediction = model.predict(img)[0, 0]
    if prediction > 0.5:
        return 'Healthy', (0 + prediction)
    else:
        return 'Powdery_Mildew', (1 - prediction)

#Used basically the same code as in walkthroughproject at "https://github.com/Code-Institute-Solutions/WalkthroughProject01/blob/main/src/data_management.py" by NielMc on github https://github.com/NielMc
def download_report(df):
    report_name = datetime.now().strftime('Mildew_Report_' + "%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = (
        f'<a href="data:file/csv;base64,{b64}" download="{report_name}.csv" '
        f'target="_blank">Download Report as CSV</a>'
    )
    return href