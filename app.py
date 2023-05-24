import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_one import page_one_body
from app_pages.page_two import page_two_body

app = MultiPage(app_name="Mildew Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("First Page", page_one_body)
app.add_page("Second Page", page_two_body)

app.run()  # Run the app