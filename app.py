import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_background import project_background_body
from app_pages.summary_results import summary_results_body
from app_pages.cherry_leaves_visualization import cherry_leaves_visualization_body
from app_pages.mildew_detector import mildew_detector_body
from app_pages.ml_details import ml_details_body

app = MultiPage(app_name="Mildew Detector", model_version="deployed_version")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Background", project_background_body)
app.add_page("Summary & Results", summary_results_body)
app.add_page("Cherry Leaves Visualization", cherry_leaves_visualization_body)
app.add_page("Mildew Detector", mildew_detector_body)
app.add_page("Machine Learning Details", ml_details_body)

app.run()  # Run the app