import streamlit as st
from streamlit_option_menu import option_menu
import test, Home, uploads, subject, Tasks, trial, submissions, view_submission

st.set_page_config(
    page_title="Student_Analysis",
)
st.markdown(
    """
    <style>
    /* Apply background to the main app content */
    .stApp {
        background-image: url('https://i.giphy.com/3q3SUqPnxZGQpMNcjc.webp');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }

    /* Optional: Customize the sidebar */
    .css-1v3fvcr {
        background-color: rgba(255, 255, 255, 0.7) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        with st.sidebar:
            st.markdown(
                '<img class="logo" src="https://www.vcacs.ac.in/assets/images/logo/VIIT01.webp" alt="Custom Logo" style="height: 200px; position: absolute; align-item:center; top: -130px; left: 10px; z-index: 1;">',
                unsafe_allow_html=True
            )
            app = option_menu(
                menu_title='MENU',
                options=['Account', 'Home', 'Class Insights', 'Assign Task', 'View Submissions', 'Student Stats', 'Uploads', 'Student Submission'],
                icons=['person-circle', 'house-door-fill', 'graph-up', 'journal-bookmark', 'clipboard-check', 'bar-chart-line-fill', 'box-arrow-up', 'cloud-upload-fill'],
                menu_icon='list',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": '#87ceeb'},  # Skyblue
                    "menu_icon": {"color": "MidnightBlue", "font-size": "23px"},
                    "icon": {"color": "MidnightBlue", "font-size": "23px"},
                    "nav-link": {"color": "black", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "SteelBlue"},
                    "nav-link-selected": {"background-color": "#0375bc"},
                    "menu_title": {"color": "black"},
                }
            )
        if app == "Account":
            test.app()
        if app == 'Home':
            Home.app()
        if app == 'Class Insights':
            subject.app()
        if app == 'Uploads':
            uploads.app()
        if app == 'Assign Task':
            Tasks.app()
        if app == 'Student Stats':
            trial.app()
        if app == 'Student Submission':
            submissions.app()
        if app == 'View Submissions':
            view_submission.app()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()
