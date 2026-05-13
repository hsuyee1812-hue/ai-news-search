import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="AI News Search", layout="wide")

st.title("📰 AI 최신 뉴스 검색 웹앱")

# Gemini API 연결
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

keyword = st.text_input("검색 키워드 입력")

if st.button("뉴스 검색"):
    if keyword:
        with st.spinner("뉴스 검색 중..."):
            grounding_tool = types.Tool(
                google_search=types.GoogleSearch()
            )

            config = types.GenerateContentConfig(
                tools=[grounding_tool],
                temperature=0.0
            )

            prompt = f"""
            '{keyword}'에 대한 최신 뉴스 2개를 찾아줘.
            각 뉴스는 아래 형식으로 정리해줘.

            제목:
            출처:
            날짜:
            요약:
            링크:
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=config,
            )

            st.subheader("검색 결과")
            st.write(response.text)
    else:
        st.warning("검색 키워드를 입력해 주세요.")
