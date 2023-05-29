import streamlit as st

def project_background_body():
    st.write("### Project Background")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew is a fungal disease that affects cherry trees, and a wide range of other plants.\n"
        f"* The process to verify if a given cherry tree is infected with powdery mildew or not "
        f"involves an employee, taking a few samples of leaves from the tree and visually examining them.\n"
        f"* For a company, managing thousands of cherry trees located in multiple farms across the country "
        f"requires a scalable solution to ensure that the market is not supplied "
        f"with a product of compromised quality. \n")

    st.success(
        f"**Business Requirements**\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a parasitized and uninfected cell visually.\n"
        f"* 2 - The client is interested in telling whether a given cell contains a malaria parasite or not. "
        )

    st.info(
        f"**Project Dataset**\n"
        f"* The dataset available for the project contains 4208 images in .jpeg format, "
        f" taken from the client's crop fields. The dataset include two classes of images "
        f"with 2104 images each. The classes are labeled 'Powdery Mildew' for images of leaves "
        f"that are infected with the fungal desease and 'Healthy' for images of leaves "
        f"that are uninfected.\n"
        f"* The dataset can be found at "
        f"[this Kaggle endpoint](https://www.kaggle.com/codeinstitute/cherry-leaves).")

    st.write(
        f"* More information about the project can be found in the "
        f"[Project README file](https://github.com/jensbrauer/Mildew-Detection-in-Cherry-Leaves/blob/main/README.md).")
    
