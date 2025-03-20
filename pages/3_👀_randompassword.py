import streamlit as st # importing the streamlit Library for creating web application
import random #importing the Random Library for generating random password/charcters
import string # importing the string Library for providing characters

# function to generate password based on user preferences
def generate_password(length, use_digits,use_special):
    characters = string.ascii_letters # ascii => its provide upper case or lower case letters (a-z or A-Z)
    if use_digits:
        characters += string.digits # digits => its provide numbers (0-9)
    if use_special:
        characters += string.punctuation # punctuation => its provide special characters(!,@,#,$,%,^,&,*)
        
 # random.choice => its provide random characters,  generates a random password of the specified length using the characters defined above  
    return ''.join(random.choice(characters) for _ in range(length))

st.title("✨Random Password Generator🤞")

length = st.slider("select your password length", min_value=6, max_value=20, value=9)           

use_digits = st.checkbox("Include Digits ")
use_special = st.checkbox("Include special Characters ")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special) # function call , length's value come from slider & its compulsory parameter  and use_digits's and use_special's value come from checkbox & its optional parameter
    st.write(f"Your Generated Passwod => `{password}` ")

    st.write("**Note**: This password is generated using random module of python")
    st.write(" *** Created by ❤ Saba khan ***")