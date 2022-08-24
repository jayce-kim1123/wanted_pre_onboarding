![header](https://capsule-render.vercel.app/api?type=waving&color=0064ff&height=100&section=header&fontSize=90)


---
# 초기기획 & ERD

## ERD
<img src="https://user-images.githubusercontent.com/61664975/186319528-2b5e4812-b41d-4ac4-8fad-bb1bc9b76ead.png">

## 초기기획 및 구현 목표
* 짧은 시간동안 기능구현에 집중해야하므로 기본적인 user-flow를 구현하는데 집중
* 개발은 초기세팅부터 전부 직접 구현
* 필수과제-선택과제-유닛테스트 순서로 중요도 배분

<br><br>

---
# 개발기간 및 팀원

* ## 개발기간  
    2022.08.23 21:00 ~ 2022.08.24 12:00 (약 13시간 소요)   

* ## 개발인원 및 파트
    단독개발
<br><br>

---
# 적용 기술 및 구현 기능

* ## 기술 스택 
    <a href="#"><img src="https://img.shields.io/badge/python-3873A9?style=plastic&logo=python&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/Django-0B4B33?style=plastic&logo=django&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/MySQL-005E85?style=plastic&logo=mysql&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/postman-F76934?style=plastic&logo=postman&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/git-E84E32?style=plastic&logo=git&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/RESTful API-415296?style=plastic&logoColor=white"/></a>
    <a href="#"><img src="https://img.shields.io/badge/github-1B1E23?style=plastic&logo=github&logoColor=white"/></a>
<br>

* ## 구현기능
    * 채용공고의 C.R.U.D.
        - 하나의 공고에 다수의 근무지역, 사용기술, 채용포지션을 적용할 수 있게 함
        - 최대한 nested 구조를 피해가려 했으나 불가피한 부분도 존재
        - 수정기능은 근무지역, 사용기술, 채용포지션의 다중 옵션 처리 미완성 (추후 업데이트 예정)
    * 채용 공고 리스트
        - limit, offset 방식을 이용한 pagenation 구현
    * 채용 공고상세 페이지
        - 리스트의 정보에 description만 추가
    * 공고 지원 기능
        - 각 유저는 하나의 공고에 1번만 지원할 수 있도록 구현
    * 검색
        - q객체를 이용해 구현
        - 키워드를 공고의 제목과 내용 모두에서 검색할 수 있도록 구현
        - limit, offset 방식을 이용한 pagenation 구현
    
<br><br>

---
# API 기능정의서
추후 추가 예정

---
# Reference
* 이 프로젝트는 학습목적으로 만들었습니다.
* 학습용으로 만들었기 떄문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.

![Footer](https://capsule-render.vercel.app/api?type=waving&color=0064ff&height=100&section=footer)
