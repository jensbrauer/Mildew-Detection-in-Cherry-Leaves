import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.machine_learning.machine_learning import (
                                                    size_img_for_model,
                                                    predict
                                                    )


def mildew_detector_body(model_version):
    st.header("Mildew Detector")
    st.info(model_version)
    
    img_dump = st.file_uploader('Upload one or more cherry leaves for mildew diagnostics.',
                                        type='jpg',accept_multiple_files=True)

    if img_dump is not None:
        df_report = pd.DataFrame([])
        st.header('View results as:')
        format = st.radio('Select what class you want to view image samples from:', ('Images', 'Powdery Mildew'))
        st.write('---')
        if format == 'Images':
            df_report = pd.DataFrame([])
            for img in img_dump:
                img_pil = (Image.open(img))
                
                img_array = np.array(img_pil)
                st.image(size_img_for_model(img=img_pil)[1], caption=f"Image name: {img.name}")
                prediction = predict(size_img_for_model(img=img_pil)[0])
                st.info(prediction[0])
                st.warning(prediction[1])
                st.write('---')
                df_report = df_report.append({"Name":img.name, 'Prediction': prediction[0], 'Probability': prediction[1] }, ignore_index=True)
            st.write('---')
            st.table(df_report.set_index('Name'))

        elif format == 'Powdery Mildew':
            st.write('hej')
            #plot_predictions_probabilities(pred_proba, pred_class)