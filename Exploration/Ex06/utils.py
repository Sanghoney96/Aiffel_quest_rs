import re
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
from num2words import num2words

nltk.download("stopwords")

# 정규화 사전 정의
contractions = {
    "ain't": "is not",
    "aren't": "are not",
    "can't": "cannot",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he would",
    "he'll": "he will",
    "he's": "he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how is",
    "I'd": "I would",
    "I'd've": "I would have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'm": "I am",
    "I've": "I have",
    "i'd": "i would",
    "i'd've": "i would have",
    "i'll": "i will",
    "i'll've": "i will have",
    "i'm": "i am",
    "i've": "i have",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "it'll": "it will",
    "it'll've": "it will have",
    "it's": "it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she would",
    "she'd've": "she would have",
    "she'll": "she will",
    "she'll've": "she will have",
    "she's": "she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as",
    "this's": "this is",
    "that'd": "that would",
    "that'd've": "that would have",
    "that's": "that is",
    "there'd": "there would",
    "there'd've": "there would have",
    "there's": "there is",
    "here's": "here is",
    "they'd": "they would",
    "they'd've": "they would have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what will",
    "what'll've": "what will have",
    "what're": "what are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": "who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you would",
    "you'd've": "you would have",
    "you'll": "you will",
    "you'll've": "you will have",
    "you're": "you are",
    "you've": "you have",
}


def preprocess_sentence(sentence, contractions, remove_stopwords=True):
    sentence = sentence.lower()  # 텍스트 소문자화
    sentence = BeautifulSoup(sentence, "lxml").text  # HTML 태그 제거
    sentence = re.sub(r"\([^)]*\)", "", sentence)  # 괄호로 닫힌 문자열 제거
    sentence = re.sub(r'["\,]', "", sentence)  # 쌍따옴표 " 및 콤마 , 제거

    # 특수기호 변경
    sentence = re.sub(r"\$", "dollars ", sentence)  # $ → dollars
    sentence = re.sub(r"%", " percents", sentence)  # % → percent
    sentence = re.sub(r"&", "and", sentence)  # & → and

    # 숫자에서 소수점 처리 (예: 1.5 → one point five)
    sentence = re.sub(
        r"(\d+)\.(\d+)",
        lambda x: f"{num2words(x.group(1))} point {num2words(x.group(2))}",
        sentence,
    )

    # 숫자를 문자로 변경 (정수 부분)
    sentence = re.sub(
        r"\d+", lambda x: num2words(int(x.group())), sentence
    )  # 숫자 → 문자

    sentence = " ".join(
        [contractions[t] if t in contractions else t for t in sentence.split(" ")]
    )  # 약어 정규화
    sentence = re.sub(r"'s\b", "", sentence)  # 소유격 제거
    sentence = re.sub("[^a-zA-Z]", " ", sentence)  # 영어 외 문자 공백으로 변환
    sentence = re.sub(
        r"([a-zA-Z])\1{2,}", r"\1\1", sentence
    )  # 3개 이상의 동일한 문자를 2개로 변경

    # 불용어 제거 (Text)
    if remove_stopwords:
        tokens = " ".join(
            word
            for word in sentence.split()
            if not word in stopwords.words("english") and len(word) > 1
        )
    # 불용어 미제거 (Summary)
    else:
        tokens = " ".join(word for word in sentence.split() if len(word) > 1)

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


# 원문의 정수 시퀀스를 텍스트 시퀀스로 변환
def seq2text(input_seq, src_index_to_word):
    temp = ""
    for i in input_seq:
        if i != 0:
            temp = temp + src_index_to_word[i] + " "
    return temp


# 요약문의 정수 시퀀스를 텍스트 시퀀스로 변환
def seq2summary(input_seq, tar_word_to_index, tar_index_to_word):
    temp = ""
    for i in input_seq:
        if (
            (i != 0)
            and i != tar_word_to_index["sostoken"]
            and i != tar_word_to_index["eostoken"]
        ):
            temp = temp + tar_index_to_word[i] + " "
    return temp
