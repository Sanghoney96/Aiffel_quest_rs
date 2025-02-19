import os
import pandas as pd
import numpy as np

from utils import preprocess_sentence

data = pd.read_csv(
    "/home/masang/Desktop/Quest02/data/test.csv",
    encoding="utf-8",
)

# inplace=True 를 설정하면 DataFrame 타입 값을 return 하지 않고 data 내부를 직접적으로 바꿉니다
data.drop_duplicates(subset=["text"], inplace=True)  # 중복 샘플 제거
data.dropna(axis=0, inplace=True)  # summary 값이 null인 샘플 제거

with open("korean_stopwords.txt", "r") as f:
    stop_words = f.read().split("\n")

clean_text = [preprocess_sentence(text, stop_words) for text in data["text"]]

data["text"] = clean_text

# 전처리 후 빈 값을 Null 값으로 변환
data.replace("", np.nan, inplace=True)
data.dropna(axis=0, inplace=True)

data.to_csv(
    "/home/masang/Desktop/Quest02/data/preprocessed_test.csv",
    index=False,
    encoding="utf-8",
)
