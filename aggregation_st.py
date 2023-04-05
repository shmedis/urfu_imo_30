import streamlit as st
import aggregation as ag

st.title("Сервис сокращения текста")

text = st.text_area("Введите текст")
result = st.button("Агрегировать текст")

if result:
    st.write(ag.aggregate(text))
