import streamlit as st

import matplotlib.pyplot as plt
from matplotlib.image import imread

def model_specs_body():
    st.header("Model Specifications")
#data information
    if st.checkbox('Data Preprocessing'):
        balance_check = plt.imread(f"outputs/deployed_version/dataset_balance.png")
        st.image(balance_check, caption='Dataset Balance and distribution for train/validation/test')
        st.info(f'Data is perfectly balanced and was distributed by\n'
                f'* Training: 70%\n'
                f'* Validation: 10%\n'
                f'* Training: 20%\n'
                )
        st.warning('No need for up or down sampling data')
        size_check = plt.imread(f"outputs/deployed_version/scatterplot_img_sizes.png")
        st.image(size_check, caption='Image sizes plotted in scatterplott')
        st.info(f'All images are 256 by 256 pixels hight/width ratio'
                f'No need for standardization of image size')
        st.error(f'NOTE: Images were resized to a ratio of 100 by 100 pixels to reduce model size.')

#Model architacture
    if st.checkbox('Model Architecture'):
        st.info('Data info')

#Training
    if st.checkbox('Model Training'):
        st.info('Data info')

#Evaluation
    if st.checkbox('Model Evaluation'):
        st.info('Data info')

#Output
    if st.checkbox('Model Output'):
        st.info('Data info')
