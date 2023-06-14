import streamlit as st
import pickle

import matplotlib.pyplot as plt
from matplotlib.image import imread


from src.visualization.image_montage import display_model_arc

def model_specs_body(model_version):
    st.header("Model Specifications")
#data information
    if st.checkbox('View Data Preprocessing Section'):
        st.write('### Data Preprocessing')
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
        st.write("---")

#Architecture
    if st.checkbox('Model Architecture'):
        st.text(display_model_arc())
        st.write("---")

#Training
    if st.checkbox('Model Training'):
        training_hist_acc = plt.imread("outputs/deployed_version/model_training_acc.png")
        st.image(training_hist_acc, caption='Training history for accuracy')
        
        training_hist_loss = plt.imread("outputs/deployed_version/model_training_losses.png")
        st.image(training_hist_loss, caption='Training history for loss')
        st.write("---")
            
#Evaluation
    if st.checkbox('Model Evaluation'):
        with open("outputs/current_output/evaluation_report.pkl", 'rb') as file:
            evaluation_summary = pickle.load(file)
#        with open("outputs/current_output/evaluation_reports.txt", "r") as file:
#            evaluation_summary = file.read()
        st.write(f'* Loss: {round(evaluation_summary["Loss"], 3)}\n'
                f'* Accuracy: {round(evaluation_summary["Accuracy"], 3)}')
        st.write("---")

#Output
    if st.checkbox('Model Output'):
        
        with open("outputs/current_output/proba_report.pkl", 'rb') as file:
            probability_report = pickle.load(file)
        #f = open('outputs/current_output/proba_report.json')
        #probability_report = json.load(f)
        reports = ['Training', 'Validation', 'Test']
        for report in reports:
            st.write(f"### Probability Report - {report} Data")
            st.info(
                    f"75% of false predictions show a probability lower than {probability_report[report]['threshold']}%.\n\n"
                    f"{probability_report[report]['ratio']}% of all predictions show a probability lower than {probability_report[report]['threshold']}.\n\n"
                    f"I.e., 75% of false predictions are found in the {probability_report[report]['ratio']}% of predictions with lowest probability.")
            distribution_plot = plt.imread(f'outputs/current_output/proba_dist_{report.lower()}.png')
            st.image(distribution_plot, caption=f'Probabiliaty distribution for {report} data.')
        st.write("---")
