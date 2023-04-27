from transformers import MBartTokenizer, MBartForConditionalGeneration
from functools import lru_cache


model_name = "IlyaGusev/mbart_ru_sum_gazeta"


# Загружаем модель агрегирования
@lru_cache(maxsize=None)
def load_model():
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    return model


# Загружаем токенайзер
@lru_cache(maxsize=None)
def load_tokenizer():
    tokenizer = MBartTokenizer.from_pretrained(model_name)
    return tokenizer


def aggregate(text):
    input_ids = tokenizer(
        [text],
        max_length=200,
        padding="max_length",
        truncation=True,
        return_tensors="pt",
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return summary


model = load_model()
tokenizer = load_tokenizer()
