#importing package
import streamlit as st 
import pandas as pd 
import numpy as np

#streamlit tutorial
st.title(" Hello, Streamlit :streamlit:")
st.write(" Where do you want to begin ?")
st.text(" Lets Get Started ")

#conditional logic with widgets
name = st.text_input("Enter your name: ")
if st.button("Greet"):
    st.success(f"Hello, {name}")


#displaying a data chart
df = pd.DataFrame(np.random.rand(10,2), columns=('A','B'))
st.line_chart(df)
st.bar_chart(df)

#file uploading and caching
upload_file = st.file_uploader("upload CSV file", type= "csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)