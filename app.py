"""
    SUMMARY:
        - This is the main file of this application. App will be running from here. 
"""
import pyrebase 
import streamlit
from datetime import datetime


firebaseConfig = {
    "apiKey": "AIzaSyBUUSCs0nbP9iA4xUwTmONSC4Ix7eWrDck",
    "authDomain": "rentmapy.firebaseapp.com",
    "projectId": "rentmapy",
    "databaseURL": "https://rentmapy-default-rtdb.europe-west1.firebasedatabase.app/",
    "storageBucket": "rentmapy.appspot.com",
    "messagingSenderId": "860102137245",
    "appId": "1:860102137245:web:fff3cd73ea7cab5b620b74",
    "measurementId": "G-KM53Y2THK9"
}


# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Firebase Database
db = firebase.database()
storage = firebase.storage()

streamlit.sidebar.title("RENTMAPY")

# Authentication
choice = streamlit.sidebar.selectbox(
    "Log In/Sign Up",
    [
        "Log In",
        "Sign Up",
    ],
)

email = streamlit.sidebar.text_input("Email Address")
password = streamlit.sidebar.text_input("Password" ,type="password")

if choice == "Sign Up":
    handle = streamlit.sidebar.text_input("Enter your handle name", value="Default")
    submit = streamlit.sidebar.button("Create my account")

    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        # streamlit.success("Your account cretaed")

        # Sign In
        user = auth.sign_in_with_email_and_password(email, password)
        db.child(user["localId"]).child("Handle").set(handle)
        db.child(user["localId"]).child("ID").set(user["localId"])


        streamlit.title("Successfuly Signed Up" + "\n" + handle)

if choice == "Log In":
    login = streamlit.sidebar.checkbox("Login")
    if login:
        user = auth.sign_in_with_email_and_password(email, password)

        streamlit.title("Successfuly Logged In " + "\n" +  user["localId"] + "\t" +  user["email"])
        # streamlit.write("<style>div.row-widget.stRadio >div{flex-direction:row;}</style>", unsafe_allow_html=True)

        # bio = streamlit.radio("Jump to", ["Home", "Workplace", "Settings"])
        