import streamlit as st


import matplotlib.pyplot as plt
from matplotlib.image import imread

from src.visualization.image_montage import display_label_samples

def cherry_leaves_visualization_body(model_version):
    st.header("Cherry Leaves Visualization")

    st.write(
        f"*The client is interested in conducting a study to visually differentiate"
        f" a healthy cherry leaf from one with powdery mildew.*"
        )

    if st.checkbox('Label Samples'):
        label = st.radio('Select what class you want to view image samples from:', ('Healthy', 'Powdery Mildew'))
        if label == 'Healthy':
            display_label_samples('healthy')
        elif label == 'Powdery Mildew':
            display_label_samples('powdery_mildew')


    if st.checkbox('Average and Variability'):
        avg_healthy = plt.imread(f"outputs/deployed_version/img_avg_and_varblty_healthy.png")
        avg_powdery_mildew = plt.imread(f"outputs/deployed_version/img_avg_and_varblty_powdery_mildew.png")

        st.image(avg_healthy, caption='leafs_healthy - Average and Variability')
        st.image(avg_powdery_mildew, caption='leafs_powdery_mildew - Average and Variability')


    if st.checkbox('Label Difference in avarage'):
        avg_difference1 = plt.imread(f"outputs/deployed_version/diff_in_label_img_avg.png")
        st.image(avg_difference1, caption='leafs_healthy - Average and Variability')


    if st.checkbox('Label Difference in variability'):
        avg_difference2 = plt.imread(f"outputs/deployed_version/diff_in_label_img_varblty.png")
        st.image(avg_difference2, caption='leafs_powdery_mildew - Average and Variability')

