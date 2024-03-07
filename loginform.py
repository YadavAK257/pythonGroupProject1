import streamlit as st

st.title("Login Page")

account = {
    "fs23ai005@gmail.com": "1819",
    "fs23ai013@gmail.com": "0000",
    "fs23ai024@gmail.com": "0909"
}

username = st.text_input("Enter Email: ")
password = st.text_input("Enter Password:")

btn = st.button('Login here!')

if btn:
    if username in account and password == account[username]:
        st.success("Login successful!")
        st.snow()
    else:
        st.error("Invalid username or password")