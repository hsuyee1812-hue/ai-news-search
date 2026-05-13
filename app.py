import streamlit as st

st.set_page_config(page_title="AI News Search", layout="wide")

st.title("📰 AI 최신 뉴스 검색 웹앱")

keyword = st.text_input("검색 키워드 입력")

if st.button("뉴스 검색"):
    st.success(f"{keyword} 관련 뉴스 검색 기능 준비 완료!")
