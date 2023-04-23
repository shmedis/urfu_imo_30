import streamlit as st
import aggregation as ag

st.title("Сервис сокращения текста")

input_text = st.text_area("Введите текст")
output_text = st.button("Агрегировать текст")

if result:
    st.write(ag.aggregate(input_text))
