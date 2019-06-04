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
- 프론트엔드는 Vue.js를 사용하였고 vue-cli를 통해 build 

####3. mongodb DB 및 Collection 설계 및 필요 데이터 importing 작업
- API 서버에서 필요한 데이터를 조회하기 위한 DB서버를 docker-compose를 통하여 생성합니다.
- DB schema: 
    - BD 이름: `mall`
    - COLLECTIONS:
        - `meta` : 쇼핑사 & 카테고리를 미리 추출하여 앱에서 필터를 위한 데이터로 로딩하기 위해 사용하였습니다.
            - 만든 이유: 앱을 켰을때 필요한 필터링 값들을 메타데이터 형식으로 가져오는 것이
                서비스에 들어왔을때 해당 필터링 값을 distinct로 조회하여 받는 것보다 나을 것이라는 이유때문이었습니다.
            - 구조:
                ````
                { 
                    "_id" : 아이디, 
                    "timeline_filters"(편성표 필터링 요소 모음): {
                        "dates" : 날짜 리스트 ex) [ 20171125, 20171126, ... ], 
                        "mall_names" : 쇼핑사 리스트 ex) ["cjmall", "gsshop", ....],  
                        "cate1s" : 카테고리 리스트 ["가전·디지털", "보험", ....]
                    }
                }
        
                ````
        - `timeline_goods` : 홈쇼핑에서 판매되는 상품 데이터 collection 입니다.
            - 구조:
                ````
                { 
                    "_id" : 상품아이디 , 
                    "mall_name" : 쇼핑사  ex) "cjmall", 
                    "name" : 상품 내용  ex) "[17여름신상]데싱디바 매직프레스 프리미엄 라인 시즌3", 
                    "img" : 이미지 경로 ex) "http://cdn.image.buzzni.com/2017/11/09/t9C96T1PjU.jpg", 
                    "url" :  상품 url ex) "http://display.cjmall.com/p/item/44795766?infl_cd=I0675", 
                    "cate1" : 카테고리 ex) "화장품·미용", 
                    "date" :  날짜 ex) 20171120, 
                    "start_time" : 홈쇼핑 시작 시간 ex) 100(1:00), 
                    "end_time" : 홈쇼핑 마감 시간 ex) 200(2:00), 
                    "org_price" : 원가격 ex) 79900, 
                    "price" : 행사 가격 ex) 79900
                }
                
        
                ````
            - indexes: mall_name, cate1, date, start_time, end_time
              (indexing은 서비스에서 쇼핑사, 카테고리, 시간 에 따른 조회가 발생하기에 이에 해당하는 목록들에 indexing을 하였습니다.)
              
####4. server(API) 개발
- flask에 flask-restplus를 사용하여 정형화된 포맷에 따른 개발을 통해 조금더 생산성을 높이는 구현을 진행하기위해 노력하였습니다.
- http://0.0.0.0:5001/apis/v1 => 해당 경로로 주소창 검색시 swagger형식의 API 명세페이지 및 테스팅 페이지 등을 사용할 수 있도록 하였습니다


## Key Point
- Front-end: 
    - 사용자의 Scroll up/down에 따른 javascript의 동작 제어 및 API 요청 가능하도록 구현하였습니다
- Back-end: 
    - docker 에서 client, server, mongodb 으로 서비스를 분리하여 container들를 만듦으로써 향후에 있을 autoscaling 등이 발생시 서로의 의존성을 낮추도록 하였습니다.
    - 필터링 값들을 메타데이터로 미리 데이터베이스화 하여 앱실행시에만 처음 가져오도록하여 필터링값을 반환하여 전체 상품 목록을 distint해야하는 부담을 덜어줍니다.
    - flask-restplus를 활용한 api구현의 정형화/단일화를 통해 생산성을 높이도록 하였습니다.
    - api를 v1, v2등으로 버져닝하여 scalable 하게 구현할 수 있게 api 서버 구조를 설계하였습니다.

## Hurdle Point
구현시 가장 문제가 되었던 부분은 다음의 두가지였습니다.
- docker을 처음 사용해보는 상태라 해당 image, container, dockerfile 및 docker-compose 에 대해서 이해하고 헉습할 시간이 필요했고 이로 인해 개발진행에서 많은 delay가 있었습니다.
- Front-end 개발시 스크롤업을 했을시 새로운 데이터를 fetching하면 이미지가 렌더링 되고나서 스크롤이 자연스래 가장 최근에 추가된 element로 이동하도록 되기때문에, 
이를 해결하기위해 스크롤업시 가장 상단에 다았을때에 가장 상단에 있던 요소의 아이디를 임시로 저장해 두고 데이터를 API에서 받아오고 난후,
다시 저장해둔 이전 최상단의 요소 위치로 scroll을 이동시켜서 계속해서 scroll이 같은 위치에 머무르도록 할 수 있었습니다. 


##Reference
- docker 설명 페이지: https://docs.docker.com/
- flask-restplus 페이지: https://flask-restplus.readthedocs.io/en/stable/

## 해당과제 실행 방법
아래의 방법으로 docker-compose 명령어 실행시 build image, run container 그리고 datebase 셋업이 모두 한번에 됩니다.
````
cd <buzzni-test folder>
docker-compose up 
````

##과제 페이지 url 
웹페이지: http://0.0.0.0:5000
API 명세 페이지(Swagger): http://0.0.0.0:5001/apis/v1

## 해당과제 종료 방법
````
cd <buzzni-test folder>
docker-compose stop 
````

