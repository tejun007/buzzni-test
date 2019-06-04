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
            - client & mongodb & server 세가지 서비스들로 구성
            - 
        

