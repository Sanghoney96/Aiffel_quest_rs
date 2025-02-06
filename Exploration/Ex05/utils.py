import konlpy
from konlpy.tag import Mecab
import numpy as np
from collections import Counter

tokenizer = Mecab()
stopwords = [
    "의",
    "가",
    "이",
    "은",
    "들",
    "는",
    "좀",
    "잘",
    "걍",
    "과",
    "도",
    "를",
    "으로",
    "자",
    "에",
    "와",
    "한",
    "하다",
]


def load_data(train_data, test_data, num_words=10000):
    train_data.drop_duplicates(subset=["document"], inplace=True)
    train_data = train_data.dropna(how="any")
    test_data.drop_duplicates(subset=["document"], inplace=True)
    test_data = test_data.dropna(how="any")

    X_train = []
    for sentence in train_data["document"]:
        temp_X = tokenizer.morphs(sentence)  # 토큰화
        temp_X = [word for word in temp_X if not word in stopwords]  # 불용어 제거
        X_train.append(temp_X)

    X_test = []
    for sentence in test_data["document"]:
        temp_X = tokenizer.morphs(sentence)  # 토큰화
        temp_X = [word for word in temp_X if not word in stopwords]  # 불용어 제거
        X_test.append(temp_X)

    words = np.concatenate(X_train).tolist()
    counter = Counter(words)
    counter = counter.most_common(10000 - 4)
    vocab = ["", "", "", ""] + [key for key, _ in counter]
    word_to_index = {word: index for index, word in enumerate(vocab)}

    def wordlist_to_indexlist(wordlist):
        return [
            word_to_index[word] if word in word_to_index else word_to_index[""]
            for word in wordlist
        ]

    X_train = list(map(wordlist_to_indexlist, X_train))
    X_test = list(map(wordlist_to_indexlist, X_test))

    return (
        X_train,
        np.array(list(train_data["label"])),
        X_test,
        np.array(list(test_data["label"])),
        word_to_index,
    )


def get_encoded_sentence(sentence, word_to_index):
    return [word_to_index["<BOS>"]] + [
        word_to_index[word] if word in word_to_index else word_to_index["<UNK>"]
        for word in sentence.split()
    ]


# 여러 개의 문장 리스트를 한꺼번에 단어 인덱스 리스트 벡터로 encode해 주는 함수입니다.
def get_encoded_sentences(sentences, word_to_index):
    return [get_encoded_sentence(sentence, word_to_index) for sentence in sentences]


# 숫자 벡터로 encode된 문장을 원래대로 decode하는 함수입니다.
def get_decoded_sentence(encoded_sentence, index_to_word):
    return " ".join(
        index_to_word[index] if index in index_to_word else "<UNK>"
        for index in encoded_sentence[1:]
    )  # [1:]를 통해 <BOS>를 제외


# 여러 개의 숫자 벡터로 encode된 문장을 한꺼번에 원래대로 decode하는 함수입니다.
def get_decoded_sentences(encoded_sentences, index_to_word):
    return [
        get_decoded_sentence(encoded_sentence, index_to_word)
        for encoded_sentence in encoded_sentences
    ]
