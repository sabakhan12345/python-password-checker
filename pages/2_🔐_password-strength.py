import re # regex
import streamlit as st
st.title('Password Strength Meter')
st.markdown("""
## This page shows you the Ultimate Password Checker ⚓🔐
we will give you helpfull suggestions to make your **Password More Secure and Strong!** 🦾 
# """)
password_input = st.text_input("Enter Your Password :", type="password", placeholder="Enter Your Password")

feedback = []

score = 0

if password_input:
    #length check
    if len(password_input) >= 8:
        score += 1
    else:
        feedback.append("📌 Password Should be at least 8 Characters Long.")
# upper and lower case check 
    if re.search(r"[A-Z]",password_input) and re.search(r"[a-z]",password_input):
        score += 1
    else:
        feedback.append("📌 Include both Uppercase and Lowercase Letters (A-Z, a-z) ")
#digit check
    if re.search(r"[0-9]",password_input):
        score += 1
    else:
        feedback.append("📌 Password Should Contain at least One Digit (0-9)")    
# symbols
    if re.search(r"[!@#$%^&*]",password_input):
        score += 1
    else:
        feedback.append(" 📌Password Should Contain at least One Special Characters! (!@#$%^&*)")

# Strength 
    if score == 4:
        feedback.append("✅ Your Password is Strong 🙌")
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")    
    else:
      feedback.append("🚨 Weak Password - Improve it using the suggestions above.")


if feedback:
    st.markdown(" ## Improvement Suggestion")
    for tip in feedback:
     st.write(tip)


else:
    st.info("Please enter your Password to get started!")

