import pandas
import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/bigimage.jpg')

with col2:
    st.title('Sparsh Singh')
    st.info('I am sparsh singh, and I am a programmer. I am from Agra which is famous for the Taj Mahal.'
            ' I completed my 10th from Symboyzia School Agra which is affiliated by CBSE. Currently I am '
            'pursuing Diploma from GLA University Mathura with CS branch and I am in my 3rd year. ')

below_programs = '''
Below are the programs in python that I made or am about to make.
'''
st.write(below_programs)

col3, col4 = st.columns(2)

titles = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, content in titles[:10].iterrows():
        st.title(content['title'])
        st.image(f"images/{content['image']}")
        st.write(content['description'])
        st.write(f'[Source Code]({content["url"]})')

with col4:
    for index, content in titles[10:].iterrows():
        st.title(content['title'])
        st.image(f"images/{content['image']}")
        st.write(content['description'])
        st.write(f'[Source Code]({content["url"]})')
