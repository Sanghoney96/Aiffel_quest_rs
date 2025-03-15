# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 정상헌
- 리뷰어 : 정상헌


# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 한국어 문장을 영어로 번역한 결과와 attention map을 시각화하였다.
      ![Image](https://github.com/user-attachments/assets/6f0aff27-6aec-493f-8534-ddeae0b397d8)  
    
- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - Transformer 모델의 핵심 모듈인 multi-head self-attention을 구현했다.
      ![Image](https://github.com/user-attachments/assets/fa019f52-8128-4427-a52e-3b4eed817f9f)  
        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 데이터에 맞는 새로운 전처리 로직을 추가하였다.
      ![Image](https://github.com/user-attachments/assets/c2837063-ef26-4bf1-9ad9-2be43013cc98)  
    - validation loss를 측정하였다.  
      ![Image](https://github.com/user-attachments/assets/f51daece-f06e-427c-99d7-633e7d02ea82)  
        
- [X]  **4. 회고를 잘 작성했나요?**
    - 에러가 난 부분과 새롭게 추가한 부분을 회고로 정리하였다.
      ![Image](https://github.com/user-attachments/assets/e5d66ff9-fea9-470c-83db-e21cdc320c77)  
        
- [X]  **5. 코드가 간결하고 효율적인가요?**
    - train_step 함수를 pythonic하게 구현했다.
      ![Image](https://github.com/user-attachments/assets/5418a7ab-4e9f-4fdd-ac1b-380256dc9ea9)  


# 회고(참고 링크 및 코드 개선)
```
seq2seq 모델과 비교했을 때 성능개선은 확실히 있었다.  
하지만 더 좋은 모델을 만들기 위한 여러가지 작업을 해봤으면 어땠을까 하는 생각이 있었는데 에러 수정과 결과 산출에 많은 시간을 소비한 것이 아쉬웠다.
```
