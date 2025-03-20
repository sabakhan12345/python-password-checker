import streamlit as st

# --- Page Navigation Handling ---
query_params = st.query_params
if "page" in query_params:
    page = query_params["page"]
    if page == "password-strength":
        st.switch_page("pages/2_🔐_password-strength.py")
    elif page == "randompassword":
        st.switch_page("pages/3_👀_randompassword.py")

# --- Title ---
st.title("🔐 Welcome to the Password Checker and Random Password Generator")

# --- Introduction Section ---
st.markdown(
    """
    <div style="
        background-color: #f0f2f6;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.5);
        font-size: 18px;
        color: #333;
        line-height: 1.6;
    ">
        <p>
            Welcome to the <b>Password Checker and Random Password Generator</b> website! 🔑  
            This website offers two powerful tools to help you create and strengthen your passwords.
        </p>
        <h4>🌟 Password Strength Meter:</h4>
        <ul>
            <li>Check if your password is <b>strong</b> or <b>weak</b>.</li>
            <li>Get <b>helpful suggestions</b> to make your password more secure.</li>
        </ul>
        <h4>⚙️ Random Password Generator:</h4>
        <ul>
            <li>Generate a random password of any <b>length</b> you prefer.</li>
            <li>Choose whether to include <b>special characters</b> and <b>digits</b> using checkboxes.</li>
        </ul>
        <p>Ready to make your passwords stronger and more secure? Let’s get started! 🚀</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Custom CSS for Interactive Buttons ---
st.markdown("""
    <style>
        .custom-btn {
            display: inline-block;
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            background: linear-gradient(135deg, #6A5ACD, #8A2BE2);
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
            text-align: center;
            text-decoration: none;
            transition: transform 0.2s, box-shadow 0.2s;
            cursor: pointer;
        }
        .custom-btn:hover {
            background: linear-gradient(135deg, #8A2BE2, #6A5ACD);
            transform: translateY(-6px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# --- Create Columns for Buttons ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<a href="?page=password-strength" class="custom-btn">🔍 Password Strength Meter</a>', unsafe_allow_html=True)

with col2:
    st.markdown('<a href="?page=randompassword" class="custom-btn">⚙️ Random Password Generator</a>', unsafe_allow_html=True)

# --- Footer ---
st.markdown(
    """
    <hr style="margin-top: 40px;">
    <p style="text-align: center; color: #777;">
        Made with ❤️ by Saba Khan
    </p>
    """,
    unsafe_allow_html=True
)

