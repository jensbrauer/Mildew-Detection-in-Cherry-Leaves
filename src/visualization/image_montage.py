import os
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

from tensorflow.keras.models import load_model
import sys
from io import StringIO

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

def display_model_arc():
    model = load_model('/workspace/Mildew-Detection-in-Cherry-Leaves/outputs/deployed_version/mildew_detection_model.h5')
    # Redirect stdout to a variable
    stdout = sys.stdout
    sys.stdout = StringIO()
    # Display model summary
    model.summary()
    # Get the console output
    output = sys.stdout.getvalue()
    # Reset stdout
    sys.stdout = stdout
    return(output)
