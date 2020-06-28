import streamlit as st
from random import choice

# Creating a Simple Coin Flip App

## Adding Title
st.title("Coin Flip App")

## Adding List of Options
options = ['heads', 'tails']

## Adding Options for User to Select
user_option = st.selectbox("Please choose heads or tails: ", options)

## Adding Button for Coin Flip
if st.button("Flip Coin"):
    coin_flip = choice(options)
    if user_option == coin_flip:
        st.write("Congratulations! You got your choice!")
    else:
        st.write("Aww, better luck next time!") 
