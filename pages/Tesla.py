import streamlit as st  
import time   # 시간함수 사용을 위한 라이브러리
import numpy as np  # 랜덤함수 사용을 위한 라이브러리

st.set_page_config(  # 페이지 설정
    page_title="Tesla 주가 예견 데모", # 브라우저 탭의 제목
    page_icon="📈"
    )

st.markdown("# Tesla 주가 예견")  # st.markdown()을 이용한 헤더 작성
st.sidebar.header("그래프 데모")  # 사이드바에 헤더 작성

st.markdown(
    '''
    테슬라는 미국 텍사스주 오스틴에 기반을 둔 전기자동차 회사이다. 2003년, 마틴 에버하드와 마크 타페닝이 창업했다. 2004년 페이팔과 ZIP 2 의창업자이던 일론 머스크가 투자자로 참여했고 몇 년 후에 일론 머스크가 최대주주로 회장이 되었다.
    '''
)

st.text("") 
st.markdown(
    '''
    - **CEO:** 일론 머스크 (2008년 10월–)
    - **창립:** 2003년 7월 1일, 미국 캘리포니아 샌 칼로스
    - **설립자:** 일론 머스크, 마틴 에버하드, J B 스트라우벨, 마크 타페닝, 이안 라이트
    - **본사:** 미국 텍사스 오스틴
    - **직원 수:** 140,473 (2023년)
    - **자회사:** Tesla Insurance Ltd., Tesla Energy, Tesla (Thailand) 등
    '''
)

st.text("") 
st.write(
    """이 graph는 Tesla 주가의 **추락** 예견하기 위한 것입니다."""
)

progress_bar = st.sidebar.progress(0)  # 사이드바에 진행바 생성. 현제 진행률 0%
status_text = st.sidebar.empty()  # 사이드바에 빈 텍스트 상자 생성
last_rows = np.random.randn(1, 1)  # 가우시안 표준 정규 분포에서 난수 1X1 matrix array생성
chart = st.line_chart(last_rows) # 라인차트 생성

for i in range(1, 101):   # 1부터 100까지 반복
    # 표준 정규 분포에서 5X1 난수를 생성하여 누적합 행렬을 구하고 이를 기존 last_rows의 마지막 행에 더함
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0) 
    status_text.text("%i%% Complete" % i)  # 사이드바에 진행률 업데이트
    chart.add_rows(new_rows)  # 라인차트에 새로운 데이터를 추가
    progress_bar.progress(i)  # 사이드바에 진행바 업데이트
    last_rows = new_rows      # last_rows를 new_rows로 업데이트
    time.sleep(0.05)          # 0.05초 대기

progress_bar.empty()  # 진행바 삭제

# Streamlit 위젯은 자동적으로 스크립트를 처음부터 끝까지 재실행함
st.button("Re-run")   # 버튼을 클릭하면 스크립트를 재실행함
