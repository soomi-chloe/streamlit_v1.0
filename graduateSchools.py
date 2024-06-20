import streamlit as st  # streamlit 라이브러리 임포트

st.set_page_config(  # 페이지 설정
    page_title="미국 대학원 유학 준비 A to Z", # 브라우저 탭의 제목
    page_icon="📚"
    )

# 타이틀 텍스트 출력
st.title('미국 대학원 유학 준비 A to Z 🕵🚀')

# 텍스트 출력
st.text("")  
st.write('미국 대학원은 가을 학기에 시작하고 원서 지원 마감은 보통 입학 전 해 12월 초중순부터 시작되어 2025년 가을학기 지원의 경우, 올 12월까지 지원해야 합니다.  합격 여부는 입학 당해 1월부터 4월에 걸쳐 발표되며 학기 시작은 8월 말경입니다.')
st.text("")    
st.write('미국 대학원 준비는 첫 단계인 학교 Search부터 TOEFL, GRE 점수 획득, 지원 학교 결정, SOP, 이력서 작성, 추천서 받기, 원서 제출 등의 단계까지 짧게는 6개월,  길게는 1년 여의 시간이 소요됩니다.  ')

# 이미지 출력
from PIL import Image     # 이미지 처리를 위한 PIL 라이브러리 임포트

st.write('# 2025년 미국 대학원 가을 학기 지원자를 위한 Sample Application Timeline')
img = Image.open('pic.png')    # 이미지 파일 열기
st.image(img, width=600)          # 이미지 출력

st.text("")  
st.text("")  

st.write('# 지원 전 준비 사항')
st.text("")  
# Markdown 문법으로 작성된 문장 출력
st.markdown(
    '''
    **School Search**
    '''
)
st.text("")  
st.write('미국 대학원은 유사한 Research를 다루는 프로그램도 학교마다 다른 이름으로 개설되거나 타 단과대학에 소속되어 있을 수 있으며 제공되는 학위, 입학요건 등이 모두 다릅니다. 따라서 지원할 전공과 연구 분야로 어느 학교가 좋은지, 지원자의 자격요건으로 어느 학교를 지원해야 하는지를 정하는 일은 생각보다 매우 복잡한 과정을 거치게 됩니다. 아래 내용은 수많은 후보군의 학교들 중에서 지원자에게 잘 맞고 합격 가능성이 높은 학교들을 찾는 가장 효과적인 방법입니다. ')
st.text("")  
img = Image.open('pic2.jpg')    # 이미지 파일 열기
st.image(img, width=600)  


st.text("")  
st.markdown(
    '''
    **1) 공인된 기관에서 발행된 전공 순위자료를 참고합니다.**
    '''
)
st.markdown(
    '''
    - http://www.usnews.com/ranking    
    - https://www.topuniversities.com 

    '''
    )


st.text("")  
st.markdown(
    '''
    **2) 순위자료가 없다면, 전공별 인증기관이 있는지 살펴봅니다.**
    '''
) 
st.write('건축학의 경우 The National Architectural Accrediting Board(NAAB), American Psychological Association이나 American Historical Association 에서도 심리학과 역사학 전공의 인증이 되어 있는 대학원 프로그램에 대한 정보를 얻을 수 있습니다. 이와 마찬가지로 Google 등 미국 검색 사이트를 이용해 다른 전공들 역시 유사한 대표 인증 기관을 찾아봅니다.')

st.text("")  
st.markdown(
    '''
    **2) 순위자료가 없다면, 전공별 인증기관이 있는지 살펴봅니다.**
    '''
) 
st.write('건축학의 경우 The National Architectural Accrediting Board(NAAB), American Psychological Association이나 American Historical Association 에서도 심리학과 역사학 전공의 인증이 되어 있는 대학원 프로그램에 대한 정보를 얻을 수 있습니다. 이와 마찬가지로 Google 등 미국 검색 사이트를 이용해 다른 전공들 역시 유사한 대표 인증 기관을 찾아봅니다.')

st.text("")  
st.markdown(
    '''
    3) 순위자료와 전공별 인증기관도 없다면 **www.gradschools.com 에서 희망하는 전공이나 학위가 어느 학교들에 개설되어 있는지 찾아 정리합니다.** 이 사이트를 통해 미국 내 대학원 프로그램을 학위별, 지역별, 프로그램명(A-Z)등으로 쉽게 검색할 수 있습니다. 
    '''
    )

st.text("") 
st.markdown(
    '''
    4) 대략적인 학교 군이 정해졌으면, 각 학교 해당학과 페이지의 ‘Research,’ ‘Faculty,’ ‘Lab,’ ‘Program’ 등의 항목을 참고하여 **본인이 연구하고자 하는 ‘Research interest’와 잘 맞는 학교들을 선택합니다.** 이 때 각 학교별 특장점, 교수 정보 등을 메모해 둡니다. 추후 SOP를 작성할 때 많은 도움이 됩니다. 
    '''
    )

st.text("") 
st.markdown(
    '''
    5) 선정된 학교리스트를 기준으로 박사 지원자는 지원할 학교의 교수에게 이메일로 Contact을 하거나 추천서를 써주실 교수님께 학교 추천을 부탁합니다. 이 외에도 날씨, 도시규모, 장학금 가능성, 학비 등도 고려해 학교 수를 줄여 나갑니다.
    '''
    )
 
st.text("") 
st.markdown(
    '''
    **6) 학과 홈페이지에 나와 있는 Admission requirement(마감일, GPA, TOEFL, GRE, 선수과목, 기타 부가 서류 여부 등)를 한눈에 볼 수 있게 스프레드시트로 정리합니다.** Grad cafe, 리더스 유학 어드미션 포스팅 등 국내외 Admissions posting 사이트를 참조해서 실제 합격자 통계과 최소 지원 요건을 비교해 보고, 마감까지 남은 기간 동안 본인이 준비할 수 있는 Qualification을 객관적으로 판단합니다. 정리된 표에서 제시하는 가장 빠른 마감일의 학교를 기준으로 준비 일정을 잡고 가장 높은 TOEFL, GRE 점수를 목표 점수로 설정합니다. 
    '''
    )

st.text("") 
st.markdown(
    '''
    **7) 미국 대학원 지원 마감은 입학 전해 12월 초부터 시작되지만, 9월부터 원서를 받기 때문에 마감일이 아닌 지원하고자 하는 시기를 Due date으로 설정하고 남은 기간 동안 스스로의 장단점을 파악하고 준비에 있어 우선 순위를 두고 월 별로 해야 할 일을 정리합니다. 
    '''
    )

# DataFrame 출력
import pandas as pd  # pandas 라이브러리 임포트

st.text("") 
st.write('# TOP 3 미국 대학원 공대 박사 합격 스펙')  # 텍스트 출력
df = pd.DataFrame({  # DataFrame 생성
    '학교명': ['Massachusetts Institute of Technology', 'Stanford University', 'Stanford University'],
    '평균 GPA': ['N/A', 'N/A', '3.8'],
    '평균 GRE': ['161/167/4.4', '161/167/4.5', '159/167/4.2'],
    '평균 TOEFL': [108,'N/A', 'N/A'],
    '합격률': ['8%','9.8%', '9.9%']

})

st.dataframe(df)  # DataFrame 출력

# 그래프 출력
import numpy as np   # numpy 라이브러리 임포트

st.text("") 
st.write('# 지역별 해외 유학생수(한국인 유학생)')  # 텍스트 출력
chart_data = pd.DataFrame(np.random.randn(20, 4), columns=["어학연수", "대학", "대학원", "기타연수"]) # DataFrame 생성

st.bar_chart(chart_data)  # 바 차트 출력