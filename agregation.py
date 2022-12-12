import streamlit as st
from transformers import MBartTokenizer, MBartForConditionalGeneration

st.title('Сервис сокращения текста')
model_name = "IlyaGusev/mbart_ru_sum_gazeta"

# Загружаем модель в кэш
@st.cache(allow_output_mutation=True)
def load_model():
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    return model

# Загружаем токенизер в кэш
@st.cache(allow_output_mutation=True)
def load_tokenizer():
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    return tokenizer

model = load_model()
tokenizer = load_tokenizer()

text = st.text_area("Введите текст")
result = st.button("Агрегировать текст")

if result:
    input_ids = tokenizer(
        [text],
        max_length=600,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    st.write(summary)