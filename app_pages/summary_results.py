import streamlit as st

def summary_results_body(model_version):
    st.header("Summary & Results")
    st.info(
        f"To meet the business requirements for the project, 3 hypothesis related to the "
        f"business requirements where formulated and tested. Click the hypotheses below "
        f"to read more about how they where tested and what can be concluded based on the results.")

# Business Rquirements 1
    st.write(f"#### Business rquirement 1 - Satisfied\n"
            f"*The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.*\n")

    if st.checkbox("-- HYPOTHESIS 1 --  Cherry leaf with powdery mildew have visual signs that diffirentiate them from healthy cherry leaves."):
        st.info(
            f"**General Information**\n\n"
            f" *A visual study was conducted including plotting a set of samples"
            f" for each class as well as plotting the avarage and variability for"
            f" a subset of images in each class."
            f' The results can be found in the "Cherry Leaves Visualization"-page through the menu*\n\n'
            
            f"**Conclusions / Fingings**\n\n"
            f" * Samples of images from each class plotted against each other seem "
            f" to indicate a visual difference that we as humans can pick up intuitively.\n"
            f" * A barely noticable visual difference between the classes can"
            f" be found when studying image avarage and image variability.\n")

        st.warning(
            f" __The hypothesis can not be confirmed or rejected based on these studies.__\n\n"
            f" __NOTE:__ * The sense that classes are different based on raw samples should be considered enough "
            f" to support a likelyhood of success in building an ML model capable of classification.*"
            )

# Business Rquirement 2
    st.write(f"#### Business rquirement 2 - Satisfied\n"
            f"*The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.*")

    if st.checkbox("-- HYPOTHESIS 2 --  A convolutional neural network (CNN) for image classification, can predict if a cherry leaf is healthy or have powdery mildew."):
        st.info(
            f"**General Information**\n\n"
            f" *A CNN was buildt, trained and evaluated using the dataset provided by the client."
            f" Technical information about model architecture, data augmentation, performance etc."
            f' can be found on the "Machine Learning Details"-page through the left hand side menu.*\n\n'
            
            f"**Conclusions / Fingings**\n\n"
            f" * The model performance scores shown when tested with data that is excluded,"
            f"  in model training meet the business requirement.")
        st.success(
            f"  __The hypothesis is confirmed.__")

    if st.checkbox("-- HYPOTHESIS 3 --  The model can give users a probability score that is represantative of the probability that the prediction is correct."):
        st.info(
            f"**General Information**\n\n"
            f" *The model that was buildt, outputs two decimal numbers for each image."
            f" that sum up to 1. These numbers represent the probability that the image"
            f" belong to a given class. The class with the higher probability assign to it"
            f" will be the class assigned to the prediction."
            f" A statistical analysis was conducted to understand if false predictions"
            f" correlated to lower probability for the predicted class."
            f' Technical information about the analysis can be found under "Model Output" on the'
            f' "Machine Learning Details"-page through the left hand side menu.*\n\n'
            
            f"**Conclusions / Fingings**\n\n"
            f" * Due to high model performance there are few false predictions to study."
            f" Though the metrics seem to show some indication of confirming the hypothesis,"
            f" the support for the findings are extremely weak and the analysis can not reliably"
            f" confirm or reject the hypothesis")
        st.warning(
            f" __The hypothesis can not be confirmed or rejected based on these studies.__\n\n")
