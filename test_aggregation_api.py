from aggregation_api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}

def test_aggr():
    response = client.post("/aggr/",
        json={"text": "Давайте попробуем более сложный пример теста, который сначала вызывает метод predict нашего API, а затем передает в него данные для распознавания и сравнивает полученный ответ с ожидаемым. Мы продолжим рассматривать пример приложения, которое определяет тональность текстов на английском языке"}
    )
    json_data = response.json() 
    
    assert isinstance(json_data, str)