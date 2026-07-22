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


st.header("This is a Header ")
st.subheader("This is a subheader ")
st.markdown(" **Bold**, *Italic*, 'code', [Link] (https://streamlit.io/)")
st.code("for i in range(5): print(i)", language="python")

#inputs in streamlit
st.text_input("What is your name")
st.text_area("Write your message")
st.number_input("pick a number", min_value=0, max_value=100)
st.slider("choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Orange", "Mango"])
st.multiselect("Choose toppings", ["Cheese","Tomato", "Olives"])
st.radio("Pick one",["Option A", "Option B"])
st.checkbox("I agree all terms & conditions.")