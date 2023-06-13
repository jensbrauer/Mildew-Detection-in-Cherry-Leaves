import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.machine_learning.machine_learning import (
                                                    size_img_for_model
                                                    )


def mildew_detector_body():
    st.header("Mildew Detector")
    
    img_dump = st.file_uploader('Upload one or more cherry leaves for mildew diagnostics.',
                                        type='png',accept_multiple_files=True)

    if img_dump is not None:
        df_report = pd.DataFrame([])
        st.header('View results as:')
        format = st.radio('Select what class you want to view image samples from:', ('Images', 'Powdery Mildew'))
        st.write('---')
        if format == 'Images':
            for img in img_dump:
                img_pil = (Image.open(img))
                
                img_array = np.array(img_pil)
                st.image(size_img_for_model(img=img_pil)[1], caption=f"Image name: {img.name}")
                st.write('---')
        elif format == 'Powdery Mildew':
            st.write('hej')