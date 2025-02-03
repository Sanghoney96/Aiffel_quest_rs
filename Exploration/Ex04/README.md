# AIFFEL Campus Online Code Peer Review Templete
- 코더 : 정상헌
- 리뷰어 : 김천지

# PRT(Peer Review Template)
- [X]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요?**
    - 동물, 인물, 배경 크로마키, 문제점 인식 및 해결안 제시사항 모두 완료된 모습을 확인할 수 있습니다.
    - 결과 근거 사진은 전체 과정 중 하나만을 대표로 제시하겠습니다.
    - <img src="https://github.com/user-attachments/assets/6c0897f3-89ef-4ab3-81d4-e80e644bfc8b" width=300px/>
    
- [X]  **2. 전체 코드에서 가장 핵심적이거나 가장 복잡하고 이해하기 어려운 부분에 작성된 
주석 또는 doc string을 보고 해당 코드가 잘 이해되었나요?**
    - colormap 배열에서 dog에 해당하는 값을 주석 처리하여 설명하여 어떤 class에 대해서 segmentationd을 진행하는지 확인이 쉬웠습니다.
    - <img src="https://github.com/user-attachments/assets/01d1bc7e-84a5-4161-9f8a-71359f5807e4" width=300px/>
  
 
        
- [X]  **3. 에러가 난 부분을 디버깅하여 문제를 해결한 기록을 남겼거나
새로운 시도 또는 추가 실험을 수행해봤나요?**
    - Semantic segmentation을 이용하여 shallow focus를 진행하였을 때, 카메라와 가장 가까운 피사체가 blur처리가 되고, 카메라와 먼 피사체는 blur가 되지 않는 문제점을 지적해주셨습니다.
    - 이것을 해결하는 방법으로, 단일 카메라의 이미지로부터 깊이 정보를 추정하는 작업인 mono depth estimation을 소개하여 적절한 해결 방안을 제시하였습니다.
    - <img src="https://github.com/user-attachments/assets/deacad6d-c14a-42c8-b0a3-a32553f0d8b0" width=300px/>
    -

- [ ]  **4. 회고를 잘 작성했나요?**
    - 노트북 맨 마지막에 자세한 설명이 회고로 작성되어 있습니다.
    - <img src="https://github.com/user-attachments/assets/d5e382f1-dca3-4699-bf0d-7a539cc07740" width=300px/>
  

            
- [X]  **5. 코드가 간결하고 효율적인가요?**
    -  전체적으로 간결하게 코드가 작성되어 있습니다. 작성된 코드가 무슨 역할을 하는 지 주석을 보고 잘 이해할 수 있습니다.


# 회고(참고 링크 및 코드 개선)
    - 문제점을 확인하고 해결 방안을 제시하는 부분이 자세하게 제시되어 있어서 인상적이었습니다. 수고 많으셨습니다!
