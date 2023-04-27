import streamlit as st
import aggregation as ag

st.title("Сервис сокращения текста")

input_text = st.text_area("Введите текст для сокращения")
output_text = st.button("Агрегировать текст")

if output_text:
    st.write(ag.aggregate(input_text))
