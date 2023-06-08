import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Sparsh Singh')
    st.info('I am sparsh singh, and I am a programmer. I am from Agra which is famous for the Taj Mahal.'
            ' I completed my 10th from Symboyzia School Agra which is affiliated by CBSE. Currently I am '
            'pursuing Diploma from GLA University Mathura with CS branch and I am in my 3rd year. ')

st.write('This is some extra content added for implementing an exercise given by the mentor.')
