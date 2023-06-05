import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def cherry_leaves_visualization_body():
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


def display_label_samples(label):
    montage_rows = 2
    montage_cols = 3
    figsize=(10,7)

    sns.set_style("white")
    img_path = '/workspace/Mildew-Detection-in-Cherry-Leaves/inputs/cherry_leaves_dataset/cherry-leaves/validation'

    print(f'Sample data from label: {label}')
    imgs_list = os.listdir(img_path + '/' + label)
    imgs_sample = random.sample(imgs_list, montage_rows * montage_cols)

    # create list of axes indices based on montage_rows and montage_cols
    pos_index = []
    for i in range(0, montage_rows):
        for j in range(0, montage_cols):
            pos_index.append([i, j])

    # create a Figure and display images
    fig, axes = plt.subplots(nrows=montage_rows,ncols=montage_cols, figsize=figsize)
    for k in range(0, len(imgs_sample)):
        img = imread(img_path + '/' + label + '/' + imgs_sample[k], 0)
        img_shape = img.shape
        axes[pos_index[k][0], pos_index[k][1]].imshow(img)
        axes[pos_index[k][0], pos_index[k][1]].set_xticks([])
        axes[pos_index[k][0], pos_index[k][1]].set_yticks([])
    plt.tight_layout()
    st.pyplot(fig=fig)

