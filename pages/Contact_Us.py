import streamlit as st
import send_email as snm

st.title('Contact Me')

with st.form(key='my-form'):
    email = st.text_input('Your email address: ')
    message = st.text_area('Your message:')
    button = st.form_submit_button('Submit')
    if button:
        snm.email_sender(message=message, email=email)
