import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.machine_learning.machine_learning import (
                                                    size_img_for_model,
                                                    predict,
                                                    download_report
                                                    )


def mildew_detector_body(model_version):
    st.header("Mildew Detector")
    st.info(
        f'Below, you can test the deployed prototype model. You can upload one of more images for classification'
        f'and choose to view the model output in a downloadable table format or a webformat, '
        f'both with filenames, predictions and assigned probabilities included.\n\n'
        f'For more information on how the output can be interpreted, see the "Model Output"-section '
        f'on the "Machine Learning Details"-page.\n\n'
        f'Find cherry leaf images for testing [here](https://www.kaggle.com/codeinstitute/cherry-leaves).')
    st.write('---')
    
    img_dump = st.file_uploader('Upload one or more cherry leaf .jpeg images for powdery mildew diagnostics.',
                                        type='jpg',accept_multiple_files=True)

    if img_dump is not None:
        df_report = pd.DataFrame([])
        results = []
        for img in img_dump:
            img_pil = (Image.open(img))

            resized_images = size_img_for_model(img=img_pil)
            st.info(f'{len(resized_images)}')
            prediction = predict(resized_images[0])
            df_report = df_report.append({"Name":img.name, 'Prediction': prediction[0], 'Probability': prediction[1] }, ignore_index=True)
            results.append([resized_images[1], img.name, prediction[0], prediction[1]])

        st.header('View results as:')
        format = st.radio('Select in what format you want to view the results:', ('Table', 'Images'))
        st.write('---')
        if format == 'Table':
            if len(results) != 0:
                st.markdown(download_report(df_report.set_index('Name')), unsafe_allow_html=True)
                st.table(df_report.set_index('Name'))

        elif format == 'Images':
            for item in results:
                st.image(item[0])
                st.info(item[2])
                st.warning(item[3])
                st.write('---')