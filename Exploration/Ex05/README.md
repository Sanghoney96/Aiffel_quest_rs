# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 정상헌
- 리뷰어 : 이동건


# PRT(Peer Review Template)
- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
        - 중요! 해당 조건을 만족하는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/d32219d3-bcb8-4e9b-b217-937299960e7b)
        - ![image](https://github.com/user-attachments/assets/0f1684d3-6cd3-429e-92d5-cb1bfc5cf093)
        - Embedding Layer와 LSTM 레이어를 이용한 모델을 생성하여 주어진 문제를 해결하는 코드가 완성되었습니다.
        - 테스트셋에 대해서 84.7%의 성능을 확인하였습니다.
     
        - ![image](https://github.com/user-attachments/assets/306cd60d-628f-4e54-ae1f-f73aa1848884)
        - 한국어 word vector를 이용한 모델을 구성하고 성능 분석이 진행되었습니다.
        - Embedding Layer와 bidirectional LSTM 레이어를 구성하였습니다.
        - ![image](https://github.com/user-attachments/assets/a66460b7-b19f-443e-9574-55a85858ad4f)
        - 최종 성능은 84.4%로 확인하였습니다.
    
- [x]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - 해당 코드 블럭을 왜 핵심적이라고 생각하는지 확인
    - 해당 코드 블럭에 doc string/annotation이 달려 있는지 확인
    - 해당 코드의 기능, 존재 이유, 작동 원리 등을 기술했는지 확인
    - 주석을 보고 코드 이해가 잘 되었는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/b821b3bd-1257-4864-ad31-305f889d838a)
        - 핵심 코드는 모델을 생성하는 부분으로 핵심 부분에 대한 주석과 함께 잘 구성되었습니다.
        
- [x]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - 문제 원인 및 해결 과정을 잘 기록하였는지 확인
    - 프로젝트 평가 기준에 더해 추가적으로 수행한 나만의 시도, 
    실험이 기록되어 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/e4220714-2571-419e-ba82-83e44c010384)
        - ![image](https://github.com/user-attachments/assets/ea0056af-55a9-4538-baea-e8ff639d3922)
        - 다양한 모델을 이용한 추가 실험이 진행되었습니다.
        
- [x]  **4. 회고를 잘 작성했나요?**
    - 주어진 문제를 해결하는 완성된 코드 내지 프로젝트 결과물에 대해
    배운점과 아쉬운점, 느낀점 등이 기록되어 있는지 확인
    - 전체 코드 실행 플로우를 그래프로 그려서 이해를 돕고 있는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/a85f2db9-62e9-4251-af44-bacad76cdd30)
        - 개선해야 할 사항에 대한 회고가 잘 작성되었습니다.
        
- [x]  **5. 코드가 간결하고 효율적인가요?**
    - 파이썬 스타일 가이드 (PEP8) 를 준수하였는지 확인
    - 코드 중복을 최소화하고 범용적으로 사용할 수 있도록 함수화/모듈화했는지 확인
        - 중요! 잘 작성되었다고 생각되는 부분을 캡쳐해 근거로 첨부
        - ![image](https://github.com/user-attachments/assets/89acf01d-cc92-4d85-8b60-efe2dd7ff07b)
        - ![image](https://github.com/user-attachments/assets/d5813ced-493d-4f10-8b78-fcf62bb67872)
        - 코드가 간략하게 구성되어 있으며, 특히 자주 사용하는 함수 부분을 별도의 파이썬 파일(utils.py)로 구분하여 구성하였습니다.

# 회고(참고 링크 및 코드 개선)
```
# 리뷰어의 회고를 작성합니다.
# 코드 리뷰 시 참고한 링크가 있다면 링크와 간략한 설명을 첨부합니다.
# 코드 리뷰를 통해 개선한 코드가 있다면 코드와 간략한 설명을 첨부합니다.
```

- 데이터로딩, 워드 임베딩 등 자주 사용하는 기능을 별도의 파이썬 파일로 구성하여 코드를 간결하고 이해하기 쉽게 구성한 점이 매우 좋았습니다.
- 기본 모델을 적용하여 테스트를 수행하였으며, 84% 정도의 좋은 성능 보이고 있습니다.
- 성능을 더 높이기 위해 여유 시간에 추가적인 테스트를 진행할 예정이라고 하여, 결과가 기대가 됩니다.
