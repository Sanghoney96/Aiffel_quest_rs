import re

from konlpy.tag import Okt


def preprocess_sentence(text, stopwords):
    # 문장부호/특수문자 앞뒤 공백 넣기
    text = re.sub(r"([.,!?()])", r" \1 ", text)

    # 문장부호 제거
    text = re.sub(r"[^\w\s]", "", text)

    # 특수문자, 숫자 제거
    text = re.sub(r"[^가-힣a-zA-Z\s]", "", text)

    # 형태소 단위로 토큰화 (Okt 형태소 분석기 사용)
    okt = Okt()
    tokens = okt.morphs(text)

    # 불용어 제거
    tokens = [word for word in tokens if word not in stopwords]

    return tokens


def below_threshold_len(max_len, nested_list):
    cnt = 0
    for s in nested_list:
        if len(s.split()) <= max_len:
            cnt = cnt + 1
    print(
        "전체 샘플 중 길이가 %s 이하인 샘플의 비율: %s"
        % (max_len, (cnt / len(nested_list)))
    )
