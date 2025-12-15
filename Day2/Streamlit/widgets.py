import streamlit as st 

name=st.text_input("Enter Your Name: ")
message=st.text_area("Enter Your Message:",height=100)
uploaded_file=st.file_uploader("Choose a file",type=['csv','txt','pdf'])
model=st.selectbox("Choose AI model:",["GPT-4","Leama 3","Gemini","Claude"] )

if name:
    st.write(f"Hello,{name}")

st.markdown("**This is bold text and *this is italic*")

import pandas as pd 
df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
st.dataframe(df)

config={"model":"gpt-4","temperature":0.7,"max_tokens":500}
st.json(config)
