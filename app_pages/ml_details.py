import streamlit as st
import pickle

import matplotlib.pyplot as plt
from matplotlib.image import imread


from src.visualization.image_montage import display_model_arc

def ml_details_body(model_version):
    st.header("Machine Learning Details")
#data information
    if st.checkbox('Data Preprocessing'):
        balance_check = plt.imread(f"outputs/{model_version}/dataset_balance.png")
        st.info(f' as seen below, data is perfectly balanced and was distributed by\n'
                f'* Training: 70%\n'
                f'* Validation: 10%\n'
                f'* Training: 20%\n'
                )
        st.image(balance_check, caption='Dataset Balance and distribution for train/validation/test')
        st.warning('No need for up or down sampling data')
        st.write("---")
        st.info(f' As seen below, all images are 256 by 256 pixels in hight/width ratio'
                f' with no need for standardization of image size')
        size_check = plt.imread(f"outputs/{model_version}/scatterplot_img_sizes.png")
        st.image(size_check, caption='Image sizes plotted in scatterplott')
        st.error(f'NOTE: Images were resized to a ratio of 100 by 100 pixels to reduce model size.')
        st.write("---")

#Architecture
    if st.checkbox('Model Architecture'):
        st.info(f'Model built using arcitecture displayed below.\n'
                f'* Image augmentation was applied during model training.\n'
                f'* Regulization was applied to reduce overfitting\n'
                )
        st.text(display_model_arc(model_version))
        st.write("---")

#Training
    if st.checkbox('Model Training'):
        st.info('Seen below is the model training history and how the accuracy/loss improved over training.')
        training_hist_acc = plt.imread(f"outputs/{model_version}/model_training_acc.png")
        st.image(training_hist_acc, caption='Training history for accuracy')
        
        training_hist_loss = plt.imread(f"outputs/{model_version}/model_training_losses.png")
        st.image(training_hist_loss, caption='Training history for loss')
        st.write("---")
            
#Evaluation
    if st.checkbox('Model Evaluation'):
        st.info('The deployed model was tested using a data "unseen" by the model, with the preformance metrics;')
        with open(f"outputs/{model_version}/evaluation_report.pkl", 'rb') as file:
            evaluation_summary = pickle.load(file)
        st.write(f'* __Loss:__ {round(evaluation_summary["Loss"], 3)}\n'
                f'* __Accuracy:__ {round(evaluation_summary["Accuracy"], 3)}')
        st.write("---")

#Output
    if st.checkbox('Model Output'):
        st.info(f'To better understand the "probability" metric that the model assigns to a prediction '
                f'and to answer hypothesis 3. The reports below were created.'
                f'The idea behind the reports is to check if predictions with higher probability, '
                f'are more likely to be true predictions and vice versa.')
        
        with open(f"outputs/{model_version}/proba_report.pkl", 'rb') as file:
            probability_report = pickle.load(file)
        reports = ['Training', 'Validation', 'Test']
        for report in reports:
            st.write(f"### Probability Report - {report} Data")
            st.write(
                    f"* 75% of false predictions show a probability lower than {probability_report[report]['threshold']}%.\n"
                    f"* {probability_report[report]['ratio']}% of all predictions show a probability lower than {probability_report[report]['threshold']}.\n"
                    f"* I.e., 75% of false predictions are found in the {probability_report[report]['ratio']}% of predictions with lowest probability.")
            distribution_plot = plt.imread(f'outputs/{model_version}/proba_dist_{report.lower()}.png')
            st.image(distribution_plot, caption=f'Probabiliaty distribution for {report} data.')
        st.write("---")
