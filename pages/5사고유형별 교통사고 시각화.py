import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 공식 문서를 찾아 프로젝트에 적용해보기
#head 부분
st.set_page_config(
    page_title="사고 유형 별 교통사고",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 사고 유형별 교통사고 🚶🏻‍♂️💥🚗")
st.sidebar.markdown("# 사고 유형별 교통사고 🚶🏻‍♂️💥🚗")

# @st.cache  # 데이터용량이 큰 경우 데이터 로드가 오래 걸리기 때문에 한번 로드했으면 새로 로드하지 않고 기존 데이터를 사용해 부담을 줄이기 위해, 속도문제도 해결 
# def load_data():
#     data = pd.read_excel("/Users/youngbinlee/ais7/Mid/accident_type.xlsx",index_col=0)
#     return data

@st.cache(allow_output_mutation=True)
def load_data():
    data =  pd.read_csv(
        "https://raw.githubusercontent.com/meji9086/Traffic-Accident-Data-Analysis/master/data/accident_type.csv"
        , encoding='UTF-8')
    return data
data = load_data()

data.columns = ["","월","사고유형","사고분류","사고분류_소","사고분류_대","사고수","계절","발생장소","보행중교통사고"]



data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

st.markdown("## 개요")

"""
- 사고 유형별 데이터는 사고 대상과 사고 유형, 피해종류에 대해 나타낸 데이터이다.\n
- 차 대 차, 차 대 사람 그리고 차량 단독으로 일어날 수 있는 사고 유형을 분류해 월별 사망/사상/부상 발생 건수를 포함하고있다.
"""


"""
\n
"""

st.markdown("### 가설 1. 차vs사람간의 교통사고는 횡단보도에서 가장 많이 발생했을 것이다.")
gh1 = px.histogram(data[data["보행중교통사고"]], x='사고분류_소',y='사고수',title = '보행 중 교통사고')
st.plotly_chart(gh1)
"""
#### 분석결과 
\n차도에서 횡단보도를 건너거나 통행하는 것보다 보도를 통행했을 때 사고가 훨씬 많이 발생 했다. 
특히 길 가장자리 통행시 사고 건수가 높은 것으로 보았을때, 보도와 차도의 구분이 모호한 도로에서 보행자를 보호하는 규제 또는 도로 환경의 개선이 필요하다.
"""

"""
\n
\n
"""
st.markdown("### 가설 2: 계절별로 많이 발생하는 특정 사고가 있을 것이다")
gh2= px.bar(data, x="사고분류_소",y="사고수", color ="사고분류_소",facet_col ='계절',facet_col_wrap = 2, title= '계절별 사고 특징')
st.plotly_chart(gh2)
"""
#### 분석결과 
\n 계절별 기후의 영향 등으로 특정 사고 발생이 두드러질 것이라고 예상했지만, 봄가을철 행락객으로 인한 이동량 증가로 사고수가 증가할 뿐 
계절과 관계없이 발생하는 사고는 비슷하다. 
"""

"""
\n
"""

"""
\n
"""
st.markdown("## 제안: 길 가장자리에 조명 설치로 보행자 사고예방 ")
"""
<길 가장자리구역에 밤이 되면 켜지는 led 조명 설치하여 보행자 통행로의 식별성을 높이고 운전자의 시야 확보>

경찰청과 도로교통공단이 최근 5년간(2017년~2021년) 국내 교통사고 사망자를 분석한 결과 전체 교통사고 사망자 중 38%가 보행자인 것으로 나타났다. 이는 OECD 회원국 평균인 19.3%(2019년도 OECD 통계 기준)보다 2배 높은 수준이다.\n
이 같은 문제를 개선하기 위해 지난 4월 20일 보차혼용도로 보행자 통행 우선권 보장을 골자로 한 개정 도로교통법이 시행되었지만 여전히 보행자의 교통사고율은 높은 수준이다.
그 중 길 가장자리 교통사고율이 두드러지는데, 보도와 차도가 분리되지 않고 중앙선이 있는 도로의 경우 길 가장자리로 통행을 안내하고 있다. 하지만 이는 저녁시간 도로가 어두워 운전자의 시야에 보행자가 확보가 어렵기 때문에 사고가 발생할 확률이 높다는 한계가 있다.\n 
보행자 통행로의 식별성을 높여 운전자의 시야를 확보하기위해 길 가장자리구역에 밤이 되면 켜지는 led 조명 설치를 제안한다. 
"""

# Sidebar - origin
# sorted_unique_origin = sorted(data.origin.unique())
# selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

# if len(selected_origin) > 0:
#    data = data[data.origin.isin(selected_origin)]


# st.dataframe(data)

# st.line_chart(data["mpg"])

# st.bar_chart(data["mpg"])


# fig, ax = plt.subplots(figsize=(10, 3))
# sns.countplot(data=data, x="origin").set_title("지역별 자동차 연비 데이터 수")
# st.pyplot(fig)

# pxh = px.histogram(data, x="origin", title="지역별 자동차 연비 데이터 수")
# st.plotly_chart(pxh)

