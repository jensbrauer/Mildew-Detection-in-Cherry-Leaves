import streamlit as st

def project_background_body(model_version):
    st.header("Project Background")

    st.info(
        f"The project owner, a company managing thousands of cherry trees located in multiple farms across the country, "
        f"requires a scalable solution to ensure a healthy crop and that the market is not supplied "
        f"with a product of compromised quality. \n\n"
        f"Powdery mildew is a fungal disease that affects cherry trees, and a wide range of other plants.\n"
        f"The process to verify if a given cherry tree is infected with powdery mildew or not "
        f"involves an employee, taking a few samples of leaves from the tree and visually examining them.\n\n"
        f"This project is aimed at investigating the feasibility of employing Machine learning, "
        f"for the task of detecting powdery mildew in cherry leaves. ")

    st.write(
        f"**Business Requirements**\n"
        f"* 1 - The client is interested in conducting a study to visually "
        f"differentiate a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )

    st.write(
        f"**Project Dataset**\n\n"
        f"The dataset available for the project contains 4208 images in .jpeg format, "
        f" taken from the client's crop fields. The dataset include two classes of images "
        f"with 2104 images each. The classes are labeled 'Powdery Mildew' for images of leaves "
        f"that are infected with the fungal desease and 'Healthy' for images of leaves "
        f"that are uninfected.\n\n"
        f'The dataset is further explored in "Model Specifications" and the dataset itself can be found at '
        f"[this Kaggle endpoint](https://www.kaggle.com/codeinstitute/cherry-leaves).")

    st.info(
        f"__*More information about the project can be found in the *__"
        f"[__*Project README file*__](https://github.com/jensbrauer/Mildew-Detection-in-Cherry-Leaves/blob/main/README.md).")
    
