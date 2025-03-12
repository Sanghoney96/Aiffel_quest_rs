import re
import random
from konlpy.tag import Mecab

def preprocess_sentence(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"\([^)]*\)", "", sentence)  # 괄호로 닫힌 문자열 제거
    
    # 알파벳, 문장부호, 한글만 남기고 모두 제거
    sentence = re.sub(r"[^0-9a-zㄱ-ㅎ가-힣,.!?]", " ", sentence)
    
    return sentence


def build_corpus(sentences_df, is_train=True):
    mecab = Mecab()
    
    processed_sentences = [preprocess_sentence(sentence) for sentence in sentences_df]
    
    if is_train:
        tokenized_sentences = [mecab.morphs(sentence) for sentence in processed_sentences]
        
        return tokenized_sentences

    return processed_sentences

def lexical_sub(src, wv, ratio=0.5):
    result = []
    for tok in src:
        # 확률적으로 단어를 바꿀지 말지를 결정
        if tok in wv and random.random() < ratio:
            similar_words = wv.most_similar(tok, topn=1)  # 단어를 입력으로 사용
            result.append(similar_words[0][0] if similar_words else tok)
        else:
            result.append(tok)

    return result