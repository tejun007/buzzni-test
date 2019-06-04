# buzzni-test server & client

## 구현 프로세스

####1. docker로 서비스 image & container 생성
- 시스템 구성
    - client(웹)서버
        - localhost:5000
        - vuejs & flask 
    - api 서버
        - localhost:5001
        - flask + flask-restplus
    - db 서버
        - localhost:27017
        - mongodb
- 실시간 소스코드 갱신 가능한 개발환경 설정
    - docker-compose 사용
        - docker-compose.yml
            - client & mongodb & server 세가지 서비스들로 구성하였습니다.
            - client & server의 경우 소스코드를 VOLUME에서 binding하여
             소스 수정시 이를 detect하고 서버가 재실행 될 수 있도록 수정하였습니다.
      
####2. client개발  
- 서비스의 UI를 먼저 개발 진행하였습니다.
- 이유: UI를 먼저 구성함으로써 필요한 데이터들에 대한 이해를 명확히 할 수 있다고 생각했습니다.

####3. mongodb DB 및 Collection 설계 및 필요 데이터 importing 작업
- API 서버에서 필요한 데이터를 조회하기 위한 DB서버를 docker-compose를 통하여 생성합니다.
- DB schema
    ````
    
    ````
####4. server(API) 개발
- 
