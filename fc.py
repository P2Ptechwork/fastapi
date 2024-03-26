import streamlit as st
import face_recognition
import cv2
import numpy as np
import pickle

def register_user():
    st.title("User Registration")
    
    username = st.text_input("Enter username")
    userid = st.text_input("Enter user ID")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Display the image
        st.image(img, caption='Uploaded Image.', use_column_width=True)
        
        if st.button("Submit"):
            # Find all the faces and face encodings in the uploaded image
            face_locations = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations)
            
            if face_encodings:
                user_data = {
                    'username': username,
                    'userid': userid,
                    'face_encodings': face_encodings[0]
                }
                
                # Save user_data in a file
                with open(f"{userid}.pkl", 'wb') as f:
                    pickle.dump(user_data, f)
                st.success(f"User {username} registered successfully.")
            else:
                st.error("No face detected in the image. Registration failed.")

def take_attendance():
    # function to take attendance using face recognition
    pass

def display_attendance():
    # function to display the attendance
    pass

# Use Streamlit to create a sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Register", "Take Attendance", "Display Attendance"])

if menu == "Register":
    register_user()
elif menu == "Take Attendance":
    take_attendance()
elif menu == "Display Attendance":
    display_attendance()