import os
import pandas as pd
import numpy as np

from utils import preprocess_sentence, contractions

data = pd.read_csv("data/news_summary_more.csv", encoding="utf-8")

# inplace=True 를 설정하면 DataFrame 타입 값을 return 하지 않고 data 내부를 직접적으로 바꿉니다
data.drop_duplicates(subset=["text"], inplace=True)  # 중복 샘플 제거
data.dropna(axis=0, inplace=True)  # summary 값이 null인 샘플 제거

clean_text = [preprocess_sentence(text, contractions) for text in data["text"]]
clean_headlines = [
    preprocess_sentence(text, contractions) for text in data["headlines"]
]

data["text"] = clean_text
data["headlines"] = clean_headlines

# 전처리 후 빈 값을 Null 값으로 변환
data.replace("", np.nan, inplace=True)
data.dropna(axis=0, inplace=True)

data.to_csv(
    "data/preprocessed_news.csv",
    index=False,
    encoding="utf-8",
)
