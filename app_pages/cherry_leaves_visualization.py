import streamlit as st


import matplotlib.pyplot as plt
from matplotlib.image import imread

from src.visualization.image_montage import display_label_samples

def cherry_leaves_visualization_body(model_version):
    st.header("Cherry Leaves Visualization")

    st.info(
        f"*The client is interested in conducting a study to visually differentiate"
        f" a healthy cherry leaf from one with powdery mildew.*\n\n"
        f"__Hypothesis__ - Cherry leaf with powdery mildew have visual signs that diffirentiate them from healthy cherry leaves."
        )
    st.write(
        f" __*Click on the checkbox headings below to see the approch for this hypothesis*__")

    if st.checkbox('Label Samples'):
        st.info(f'The dataset is devided into two classes namely "powdery Mildew" and "Healthy".'
                f' Below, you can view a set of samples from each class to get familiar with the charicaristics.')
        label = st.radio('Select what class you want to view image samples from:', ('Healthy', 'Powdery Mildew'))
        if label == 'Healthy':
            display_label_samples('healthy')
        elif label == 'Powdery Mildew':
            display_label_samples('powdery_mildew')
        st.write('---')


    if st.checkbox('Average and Variability'):
        st.info(f'Below, plots show a calculated Avarage and Variability of image samples from each class.\n\n'
                f'The idea behind this study is to reveal patterns in color values that indicate a'
                f' charicaristic of the class.')
        avg_healthy = plt.imread(f"outputs/deployed_version/img_avg_and_varblty_healthy.png")
        avg_powdery_mildew = plt.imread(f"outputs/deployed_version/img_avg_and_varblty_powdery_mildew.png")

        st.image(avg_healthy, caption='leafs_healthy - Average and Variability')
        st.image(avg_powdery_mildew, caption='leafs_powdery_mildew - Average and Variability')
        st.write('---')


    if st.checkbox('Label Difference in avarage'):
        st.info(f'Below, the Avarage for each class studied above is plotted toghether with '
                f'an additional plot showing the calculated difference between them (Avarage1 - Avarage2).\n\n'
                f'The idea is to try and reveal any color value charicaristic that seperate the classes.')
        avg_difference1 = plt.imread(f"outputs/deployed_version/diff_in_label_img_avg.png")
        st.image(avg_difference1, caption='leafs_healthy - Average and Variability')
        st.write('---')

