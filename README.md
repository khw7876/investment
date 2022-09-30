# Investment_Service
투자 서비스

<br>

## MVP Service
> 주어진 고객 투자 데이터를 응답하는 REST API 개발
> Apscheduler를 이용한 batch process 이용
> 매일09시마다 새로운 모델 갱신 구현
<br>


## 주요 기능

<details>
<summary> 회원관리 </summary>

- 사용자 정보
    - 기본정보
        - 이름
        - 패스워드
- 공통기능
    - 로그인
    
</details>

<details>
<summary> 투자관리 </summary>

- 데이터 조회
    - 투자 화면
        - 계좌명
        - 증권사
        - 계좌번호
        - 계좌 총 자산
    - 투자 상세 화면
        - 계좌명
        - 증권사
        - 계좌번호
        - 계좌 총 자산
        - 투자 원금
        - 총 수익금 (총 자산 - 투자 원금)
        - 수익률 (총 수익금 / 투자 원금 * 100)
    - 보유 종목 화면
        - 보유 종목명
        - 보유 종목의 자산군
        - 보유 종목의 평가 금액 (종목 보유 수량 * 종목 현재가)
        - 보유 종목 ISIN
        
- 투자금 입금
    - **Phase1** : 입금 거래 정보들을 서버에 등록
        
        - 요청 데이터
            - 계좌번호
            - 고객명
            - 거래 금액
        - 응답 데이터
            - 거래정보 식별자 - 요청 데이터 묶음을 식별할 수 있는 key 값
        
        요청 데이터
        
        ```bash
        {
        "account_number": "123123",
        "user_name": "아이작",
        "transfer_amount": 1000
        }
        ```
        
        응답 데이터
        
        ```bash
        {
        "transfer_identifier": 111
        }
        ```
        
    - **Phase2** : 위에서 등록한 거래정보 검증 후 실제 고객의 자산을 업데이트.
        
        거래 정보를 hashing 하여 서버에 phase2 요청을 하면 
        
        서버에서는 phase1 에서 등록하여 
        
        저장된 데이터를 hashing 하여 
        
        동일한 데이터에 대한 요청인지 *검증을 합니다.ㄴ*
        
        검증에 성공하면 고객의 총 자산을 업데이트하고 성공 응답을 하고, 검증 실패 시 자산 업데이트 없이 실패 응답을 합니다.
        
        (hint: 입금된 금액은 현금 자산입니다.)
        
        - 요청 데이터
            - phase1 요청 데이터 계좌번호, 고객명, 거래 금액 순서로 연결한 string 을 hash한 string. -hash 알고리즘은 자유롭게 선택하여도 좋습니다.
            - phase1 에서 응답받은 거래정보 식별자
        - 응답 데이터
            - 입금 거래 결과
        
        요청 데이터
        
        ```bash
        {
        "signature": "82b64b05dfe897e1c2bce88a62467c084d79365af1", 
        // "123123아이작
        1000" 을 sha512 hash 한 값.
        "transfer_identifier": 111
        }
        ```
        
        응답 데이터
        
        ```bash
        {
        "status": true
        }
        ```
</details>

<br>

## 기술 스택
<img src="https://img.shields.io/badge/Python 3.9.0-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/Django REST framework-092E20?style=flat-square&logo=Django REST framework&logoColor=white"/> 

<br>

## ERD
<img width="500" src="https://user-images.githubusercontent.com/104303285/190586254-b163d772-cd18-4164-a3f8-3430c4c695b1.png" />
<br>

## API 명세서
<img width="690" alt="스크린샷 2022-09-14 오후 3 47 03" src="https://user-images.githubusercontent.com/104303285/190586453-ffee7d87-5f9f-47b1-ae19-f2c5a6c867b2.png">



<br>

## 📌 컨벤션

### ❓ Commit Message

- feat/ : 새로운 기능 추가/수정/삭제
- enhan/ : 기존 코드에 기능을 추가하거나 기능을 강화할 때
- refac/ : 코드 리팩토링, 버그 수정
- test/ : 테스트 코드/기능 추가
- edit/ : 파일을 수정한 경우(파일위치변경, 파일이름 변경, 삭제)

### ❓ Naming

- Class : Pascal
- Variable : Snake
- Function : Snake
- Constant : Pascal + Snake

### ❓ 주석

- Docstring을 활용하여 클래스와 함수단위에 설명을 적어주도록 하자.
- input/output을 명시하여 문서 없이 코드만으로 어떠한 결과가 나오는지 알 수 있도록 하자.
