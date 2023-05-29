import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.project_background import project_background_body
from app_pages.summary_results import summary_results_body

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Background", project_background_body)
app.add_page("Summary & Results", summary_results_body)

app.run()  # Run the app