# 4Mart
- 주제 : 전국 대형마트 입점 현황

- 목적 : 대표 대형마트(4개점)의 입점 현황을 토대로 전국 분포 현황을 파악하여 지도 및 차트로 시각화.

- 결과 : 롯데마트112개,이마트137개,탑마트77개,홈플러스134개
     - 이마트의 30%는 경기도, 21%는 서울 -> 51%가 수도권에 집중되어있음.
     - 롯데마트의 26%는 경기도, 12%는 서울 -> 38%가 수도권에 집중
     - 홈플러스 23%는 경기도, 14%는 서울 -> 37%가 수도권에 집중
     - 탑마트는 경상남도,경상북도,부산광역시,울산광역시,대구광역시에만 존재. 
       총 77개의 점포중 44%는 경상남도, 33%는 부산에 입점되어있음을 확인.



## 데이터 수집 방법
- 크롤링
     - Selenium,BeautifulSoup 을 사용하여 웹사이트 크롤링
      -> 롯데마트,이마트,홈플러스,탑마트
- 위/경도 (시연영상)
     - 프로그램을 동작시켜 위/경도 값을 도출.


## 수집 데이터 분석
- Seaborn 
     - countplot
- matplolib
     - barh
     - piechart
- scipy
     - corr 
          
## 시각화
- Folium
     - marker,blockmap

### Stacks
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 

### Tools
![Git](https://img.shields.io/badge/Git-F05032.svg?&style=for-the-badge&logo=Git&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC.svg?&style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)

        
