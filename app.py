import google.generativeai as genai 
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Select the model
model = genai.GenerativeModel('gemini-pro')

# Initialize session state
if 'project_ideas' not in st.session_state:
    st.session_state.project_ideas = []

# Title and description
st.header("🤖 Project Ideas & Custom Project Description Generator")
st.subheader("Generate project ideas/guidelines for data-related roles.")

# User input
job_title = st.text_input("Enter your job title (e.g., data analyst, data scientist, data engineer):")
tools = st.text_input("Enter tools for projects (comma-separated, e.g., Python, R, Excel, PowerBI):")
technique = st.text_input("Enter a focus topic technique to showcase:")
industry = st.text_input("Enter an industry for projects:")

# Button to generate project ideas
if st.button("Generate Project Ideas"):
    if job_title and tools and technique and industry:
        # Generate project ideas using Gemini AI
        prompt = f"Generate only top 10 project titles for a {job_title} using {tools} with a focus on {technique} in the {industry} industry."
        response = model.generate_content(prompt)

        # Store project ideas in session state
        st.session_state.project_ideas = response.text.split("\n")

        # Display the generated project ideas
        for idea in st.session_state.project_ideas:
            st.write(idea)

# Dropdown to select a project for detailed explanation
selected_project = st.selectbox("Select a project for detailed explanation:", st.session_state.project_ideas, key="selected_project")

# Button to generate detailed explanation
if st.button("Generate Detailed Explanation"):
    if selected_project:
        # Generate detailed explanation for the selected project
        explanation_prompt = f"Provide detailed explanation for {selected_project} project using {tools} with a focus on {technique} in the {industry} industry. give entire guidelines for project lifecycle step by step , start with stating the problem statement and then start solutions approcah problem solving"
        explanation_response = model.generate_content(explanation_prompt)

        # Display the detailed explanation
        st.write(explanation_response.text)
    else:
        st.warning("Please select a project first.")


st.markdown("---")
st.caption("Python-Langchain Application created by Khalid kifayat :sunglasses:")

hide_streamlit_style = """
            <style>

            [data-testid="stToolbar"] {visibility: hidden;}
            .reportview-container {
            margin-top: -2em;
        }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            #stDecoration {display:none;}
            footer {visibility: hidden;}
            div.embeddedAppMetaInfoBar_container__DxxL1 {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

