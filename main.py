from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

qa_model = pipeline(
    "question-answering",
    model="AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru",
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/answer/")
def answer():
    context = """Меня зовут Андрей Созыкин, я занимаюсь созданием учебных курсов по ИТ и компьютерным наукам.
           Сейчас я работаю в Уральском федеральном университете, где мы создаем магистерскую программу по 
           Инженерии искусственного интеллекта. В программу входят курсы по компьютерному зрению,
           обработке естественного языка, анализу временных рядов. Также есть интересный курс по 
           применению машинного обучения для информационной безопасности.
         """
    question = "Как называется программа магистратуры, которую создает Андрей Созыкин?"
    return qa_model(question=question, context=context)
