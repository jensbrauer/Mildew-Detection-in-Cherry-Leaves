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
    st.info(model_version)
    
    img_dump = st.file_uploader('Upload one or more cherry leaves for mildew diagnostics.',
                                        type='jpg',accept_multiple_files=True)

    if img_dump is not None:
        df_report = pd.DataFrame([])
        results = []
        for img in img_dump:
            img_pil = (Image.open(img))
            img_array = np.array(img_pil)
            resized_images = size_img_for_model(img=img_pil)
            prediction = predict(resized_images[0])
            df_report = df_report.append({"Name":img.name, 'Prediction': prediction[0], 'Probability': prediction[1] }, ignore_index=True)
            results.append([resized_images[0], img.name, prediction[0], prediction[1]])

        st.header('View results as:')
        format = st.radio('Select in what format you want to view the results:', ('Table', 'Images'))
        st.write('---')
        if format == 'Table':
            if len(results) != 0:
                st.markdown(download_report(df_report.set_index('Name')), unsafe_allow_html=True)
                st.table(df_report.set_index('Name'))

        elif format == 'Images':
            for item in results:
                st.image(item[0], caption=f"Image name: {item[1]}")
                st.info(item[2])
                st.warning(item[3])
                st.write('---')