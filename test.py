import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth 
import requests
import json

# Firebase Admin SDK initialization
if not firebase_admin._apps:
    cred = credentials.Certificate("viit-streamlit-e0199028a7cc.json")
    firebase_admin.initialize_app(cred)

# Firebase Authentication REST API URL
FIREBASE_WEB_API_KEY = "AIzaSyAf0p-7oHTe5jV9Cea5ZHT0jWrtHb8kHgk"  # Replace with your Firebase Web API key

# Function to sign in with email and password using Firebase REST API
def sign_in_with_email_and_password(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, data=payload)
    
    # Check if login was successful
    if response.status_code == 200:
        return response.json()  # Returns user data on successful login
    else:
        return None  # Failed login

def app():
    # CSS for centered title
    centered_style = """
    <style>
        body {
            background: linear-gradient(to bottom, #f8f9fa, #e9ecef);
            font-family: 'Roboto', sans-serif;
        }
        .main-title {
            text-align: center;
            font-weight: bold;
            font-size: 36px;
            color: #FFFFFF;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #7f8c8d;
            margin-top: -10px;
        }
        .login-container {
            max-width: 400px;
            margin: 20px auto;
            padding: 20px;
            background: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            border: 2px solid #3498db; /* Adding border to the form */
        }
        .login-btn {
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        .login-btn:hover {
            background-color: #2980b9;
        }
    </style>
    """
    st.markdown(centered_style, unsafe_allow_html=True)
    #st.markdown("<h1 class='main-title'>VISHWAKARMA INSTITUTE OF INFORMATION TECHNOLOGY</h1>", unsafe_allow_html=True)
    #st.markdown('<img class="logo" src="https://www.vcacs.ac.in/assets/images/logo/VIIT01.webp" alt="Custom Logo">', unsafe_allow_html=True)
    st.image("vit_logo.png", use_container_width=True)
    st.markdown("<p class='subtitle'>ViEPA - EDUCATIONAL PROGRESS ANALYZER</p>", unsafe_allow_html=True)
    # Initialize session states
    if 'username' not in st.session_state:
        st.session_state.username = ""
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ""

    def f():
        # Call the sign-in function
        user_data = sign_in_with_email_and_password(email, password)
        if user_data:
            st.session_state.username = user_data['localId']
            st.session_state.useremail = user_data['email']
            st.session_state.signedout = True
            st.session_state.signout = True    
            st.success(f"Logged in as {user_data['email']}")
        else:
            st.warning('Login Failed: Invalid email or password')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''
    
    # Session management for login/signup
    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    
    
    if not st.session_state["signedout"]:  # Show login/signup form if not signed out
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        
        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            
            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=f)
    
    # Show the user's info if signed in
    if st.session_state.signout:
        st.text('Name: ' + st.session_state.username)
        st.text('Email ID: ' + st.session_state.useremail)
        st.button('Sign out', on_click=t) 

# Call the main app function
if __name__ == "__main__":
    app()
