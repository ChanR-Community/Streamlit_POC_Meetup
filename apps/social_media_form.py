import streamlit as st
from PIL import Image
from os import getcwd

# Creating a Simple Contact Form
st.title("Social Network Account Creation")

st.balloons()

# Getting an Image of You
img = st.file_uploader("Please upload an image of you: ")

# Creating Name Fields
first_name = st.text_input("First Name: ")
last_name = st.text_input("Last Name: ")

# Getting a Password
password = st.text_input("Password: ", type='password')

# Asking for Email
email = st.text_input("Email: ")

# Ask for Simple Description
description = st.text_area("Describe yourself in the length of a tweet: ", max_chars=280)

# Ask to Choose Color from Color JSON File
color = st.beta_color_picker("What color are you feeling today: ", "#000000")
st.write(f"You chose: {color}")


# Display Results
if email != "":
    st.success(f"## Email Sent To: {email}")

if (first_name != "") and (last_name != ""):
    st.markdown(f"## Welcome, {first_name} {last_name}")

if img != None:
    img_input = Image.open(img)
    st.image(img_input, use_column_width=True)


if (description != "") and (color != ""):
    st.markdown(f"## Biography: \n {description}")
