# Adding Random Stuff for Demo
import streamlit as st

# Creating a Random Title
st.title("Random Website Title")

# Creating a Text Input
my_input = st.text_input("This is my input: ")

# Show Me My Value Here
st.write(my_input)

# Adding Numerical Input
my_num = st.number_input("Put in a number: ")

# Transforming the Number
st.write(f"Your number multiplied by 100 is: {100*my_num}")

# Creating a Dropdown Menu to Select Gender
gender_options = ['male', 'female', 'non-binary']
gender = st.selectbox("Please select your gender: ", gender_options)

# Viewing Option
st.write(f"Your gender is {gender}")

# Selecting Multiple Options Via Checkbox
fun_activities = st.multiselect("Which of the following things do you do for fun?: ", ['Netflix and Chill', 'Drink Alcohol', 'Watch YouTube', 'Sports', 'Music'])

st.write(f"You chose: {' and '.join(fun_activities)}")
