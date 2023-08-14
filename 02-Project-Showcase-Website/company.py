import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut fringilla ac tortor sit amet
fringilla. Aliquam sollicitudin fringilla est quis rhoncus. Quisque sodales arcu eros, ac
interdum diam tristique vitae. Fusce semper venenatis vehicula. Ut eget sollicitudin leo.
Aliquam quis orci egestas odio luctus luctus ac vel ante. Mauris placerat quam tortor, in
malesuada diam maximus non. Integer pellentesque arcu quam, vitae commodo tortor iaculis id.
"""
st.write(content)
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data2.csv')

with col1:
    for index, row in df[:4].iterrows():
        full_name = (row['first name'] + ' ' + row['last name']).title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images2/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        full_name = (row['first name'] + ' ' + row['last name']).title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images2/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        full_name = (row['first name'] + ' ' + row['last name']).title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images2/' + row['image'])
