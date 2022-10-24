# 🚗 Traffic-Accident-Data-Analysis 🚗

**🦁Likelion AI SCHOOL7** 
**🔥 6조 핫식스 팀** 
교통사고의 원인을 분석하는 것이 목표이다.            

## 🗃 Data Info.                                       
도로교통공단 TAAS : [http://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_ASA#](http://taas.koroad.or.kr/sta/acs/exs/typical.do?menuId=WEB_KMP_OVT_UAS_ASA#)               
공공데이터 포털 : [https://www.data.go.kr/index.do](https://www.data.go.kr/index.do)                


## 👩‍👩‍👧‍👦 Team Info.            
|이름|역할|             
|:------:|:---:|                    
|<span style="color:blue">[이영빈](https://github.com/Y0ungbinLEE)</span>|사고유형별 교통사고 데이터 전처리 및 시각화, PPT 제작|                            
|<span style="color:blue">[손진선](https://github.com/Son-jinseon)</span>|월/요일/시간별 교통사고 데이터 전처리 및 시각화, PPT 제작|          
|<span style="color:blue">[정세리](https://github.com/SERi-J)</span>|차종별 교통사고 데이터 전처리 및 시각화, PPT 제작|            
|<span style="color:blue">[이선오](https://github.com/seonseono)</span>|가해자 연령별 교통사고 데이터 전처리 및 시각화, 노션 정리, 발표|             
|<span style="color:blue">[김예지](https://github.com/meji9086)</span>|법규위반별 교통사고 데이터 전처리 및 시각화, streamlit 메인 페이지 작성|           
|<span style="color:blue">[김준모](https://github.com/junmojjang)</span>|도로형태별 교통사고 데이터 전처리 및 시각화, streamlit 메인 페이지 작성|               


## 📜 Summary.             
![Untitled (1)](https://user-images.githubusercontent.com/72390138/196888620-5ae69373-2747-4cb8-a8d7-8bd400c8f138.png)

대형 화물차부터 개인형 이동수단(PM)까지 다양한 이동 수단이 도로 위에 등장하며 관련 법이 속속 제정되고 있지만, 교통사고의 다양화를 막을 수는 없었습니다.           
사고 현장의 블랙박스만 전문으로 다루는 변호사 유튜버까지 등장할 정도로 교통사고는 핫한 이슈입니다.          
**교통사고가 어디서 어떻게 왜 발생하는지, 그 답을 찾기 위해 데이터 분석 프로젝트를 진행**해보았습니다.                 
      

## 💻 Pipeline.
### Scripts   
```
Traffic Accident               
├── acc_type.py  # 사고유형별 분석                  
├── driver_age.py  # 연령별 분석   
├── pm_count.py  # 차종별 분석   
├── time_zones.py  # 월/요일/시간별 분석   
├── traffic_kind.py  # 도로형태별 분석   
├── violatoin_raw.py  # 법규위반별 분석   
└──                            
```

## 📊 Data Analysis             
**교통사고 발생 원인 분석 결과 키워드** : '휴가철', '가을', '금요일', '퇴근시간', '교차로', '노인'        

<img src="https://user-images.githubusercontent.com/72390138/197427413-2cd50650-2f99-4bf5-9662-4d677385d85f.png"  width="600" height="750"/>

월/요일/시간대별 교통사고 발생 건수 데이터를 시각화하여 확인한 결과 월로는 *10월*, 요일로는 *금요일*, 시간으로는 *오후 6시-8시*에 가장 많은 사고가 발생했습니다.        

<img src="https://user-images.githubusercontent.com/72390138/197427629-5345488e-b14b-40b3-83cc-d23b0119726c.png"  width="650" height="500"/>       
<img src="https://user-images.githubusercontent.com/72390138/197427690-64055b43-e203-49e0-87ea-902255cea995.png"  width="650" height="500"/>           

월/시간대, 요일/시간대에 따른 교통사고 발생 건수를 히트맵으로 시각화한 결과, 색의 농도를 통해 퇴근 시간대 차량 사고 발생률이 높다는 것을 다시 한 번 확인할 수 있었습니다.      
활동량 및 이동량과 사고 발생량이 비례하는 것입니다.         

<img src="https://user-images.githubusercontent.com/72390138/197427776-05f5a255-29db-4565-9b7d-8de44f549544.png"  width="750" height="500"/>           

교통 사고가 많이 일어나는 시기에는 개인형 이동 수단의 교통사고 발생률도 높았습니다.                  
공유 킥보드 회사 ‘씽씽’의 자사 데이터 분석에 따르면 계절별 이용량은 여름 36.0%, 가을 29.1%, 봄 22.9%, 겨울 12.0% 순으로 개인형 이동 수단 역시 **이용량과 사고 발생량이 비례함**을 알 수 있습니다.            

‘라임’의 서울 지역 운행 데이터에서 **평일 오전 8시 ~ 10시, 오후 6시 ~ 8시 이용량이 전체의 약 34.8%를 차지**하는 것으로 보아 이 시간에 개인형 이동 수단의 교통사고가 많을 것이라 예상할 수 있습니다.          
 
2021년 5월 개인형 이동 수단과 관련해 도로교통법이 개정되어 관련 사고도 감소했을 것이라는 가설을 세웠지만, 이용자가 증가하며 사고 건수 또한 증가했습니다. 기상 조건으로 사용자 수가 줄어든 11월과 12월을 제외하면 **법 개정 이후에도 사고가 줄어들지 않았습니다.**                        
 
관련 법 제정만으로는 사고 감소에 큰 효과가 없는 것입니다. 이 같은 현상은 보행 중 교통사고 분석에서도 찾아볼 수 있었습니다.         

<img src="https://user-images.githubusercontent.com/72390138/197430166-0e145297-4efb-496d-b553-842fd7cac461.png"  width="550" height="450"/>       

사고 유형 별 교통사고 발생 건수 분석에서 차와 사람 사이에서 발생한 교통사고는 횡단 보도가 아닌 길 **가장자리 구역 통행 중**에 가장 많이 일어남을 확인했습니다. 

길 가장자리 구역은 보도와 차도가 구분되지 않은 도로에서 보행자의 안전을 위하여 안전 표지, 흰선 등으로 경계를 표시한 도로의 가장자리 부분으로, 갓길과는 다르게 정의됩니다.      
**길 가장자리 구역은 보행자 안전을 위한 곳이지만 실제로는 그렇지 않은 것**입니다.       

해당 데이터가 집계된 이후인 2022년 4월 20일부터 개정 도로교통법 시행으로 보행자의 통행 우선권이 보장, 확대되었으나, 길 가장자리는 법 개정 이전부터 보행자 우선이었던 곳으로, 규제만으로는 보행자 보호가 충분하지 않음을 보여줍니다.         
 
노인 보행자 교통사고 위험도가 높은 상주시 마을 10곳의 길 가장자리 구역에 led 조명이 켜지는 점등형표지병을 설치한 경북경찰청의 사례처럼 실질적인 도로 환경의 개선이 필요한 상황입니다.         

<img src="https://user-images.githubusercontent.com/72390138/197430234-6361c139-e86f-474d-9d51-de4acfbb8c0b.png"  width="660" height="500"/>       

**길 가장자리 구역 뿐만 아니라 교차로 역시 교통사고 발생이 많은 구역**입니다.      
도로 형태 별 교통사고 발생 건수 분석 또한 교차로 내에서 가장 많은 사고가 발생하며, 후 순위까지 교차로가 차지하는 것으로 나타났습니다.      
조사 대상인 다른 형태의 도로보다 교차로의 수가 많다는 점을 고려해도 큰 차이입니다.     

<img src="https://user-images.githubusercontent.com/72390138/197430285-86cbbb3f-58c1-4e01-8b1d-274e69e3aa76.png"  width="1000" height="500"/>     

**법규 위반별 사고 건수 분석에서 교차로 운행 방법 위반은 신호 위반, 안전 거리 미확보에 이어 3위**를 차지했습니다. 교차로에서는 주로 어떤 사고가 발생하는지 추가적으로 조사하던 중 교차로 사고에서 **노인 보행자의 피해가 많다**는 사실을 발견했습니다.             

행정안전부와 도로교통공단이 발표한 ‘21년 발생 노인보행자 교통사고 다발지역(30개소)’에 따르면 노인 교통사고 발생 1, 2위는 두 곳 모두 서울 동대문구로, 경동시장 앞 교차로와 성바오로병원 앞 교차로 부근입니다.          

서울시 고령자 현황 통계에 따르면 동대문구의 노인 비율은 서울시 전체의 7위. 노인 비율 1위인 강북구는 2곳이 다발 지역에 포함되었고, 노인 비율 2위는 도봉구는 한 곳도 포함되지 않았습니다.             

경동시장은 지난 2019년에도 노인 교통사고 다발 지역으로 선정되어 서울시가 보행 환경 개선에 나섰지만, **아직까지도 노인보호구역으로 지정되지 않는 등 허점**이 많았습니다. **노인 보행자에 대한 미흡한 대처가 사고**로 이어진 것입니다.         

<img src="https://user-images.githubusercontent.com/72390138/197430390-5a9c3ede-ab15-442a-ab56-8972fd472a74.png"  width="700" height="700"/>

**노인은 보행 안전에서만 사각지대에 있는 것이 아니었습니다.**        
교통사고 가해 운전자 연령별 시간대별 교통사고 발생 건수를 분석한 결과 **51세에서 64세 운전자**는 다른 연령대와 동일하게 출퇴근 시간에 사고가 가장 많이 발생했으나, 65세 이상 운전자의 경우 **오전 10시 ~ 12시, 오후 2시 ~ 4시**에 정점을 찍는 것을 확인했습니다.          

비슷한 연령임에도 차이가 발생하는 이유를 조사하며 퇴직 연령과 관련되어 있다는 사실을 발견했습니다.                 
비자발적인 조기 퇴직으로 65세 이상 운전자의 생활 시간이 달라진 것입니다.              
9 to 6에서 멀어진 65세 이상 고령 노동자의 19.7%는 운송업에 종사해, 운전과 생계가 연결되어 있습니다.           

한국은 2025년 고령 인구가 20.3%에 달해 초고령 사회로 진입합니다.            
고령 보행자 보호와 더불어, **고령 운전자의 교통사고 감소를 위해 실질적인 대책 마련이 필요함**을 이번 분석을 통해 파악할 수 있었습니다.                


## 💡 Results
### 🛠 개선방안

1. 휴가철, 출퇴근 시간처럼 교통량이 증가함에 따라 사고율이 증가한다.             
    1. 운전자와 보행자의 교통 인식 교육, 도로 상황이나 제도 개선이 필요하다.          
    2. 휴가철과 출퇴근 시간에 도로 통행 관리 인력을 늘린다.      
    
2. 법 개정으로는 교통사고 증가를 막기 어려웠다.        
    1. 관련 법과 제도 뿐만 아니라 실질적인 대책을 마련한다.       
    2. 강화한 내용을 홍보해 인식을 강화한다.       
    
3. 노인은 교통사고의 피해자일 뿐 아니라 가해자가 될 수 있다.       
    1. 운전면허 갱신 주기 단축 및 교통 안전 교육을 시행한다.       
    2. 특정 연령 이상 운전자의 신체검사를 강화한다.        
    
**저희는 이와 같이 교통사고 원인에 대해 분석하고 개선 방안을 제시하면서 방향을 제시하고자 합니다.**       
