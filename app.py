import streamlit as st
from google import genai
from google.genai import types

# 페이지 설정
st.set_page_config(
    page_title="AI News Search",
    layout="wide"
)

# 제목
st.title("📰 AI Latest News Search App")

# Gemini API 연결
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# 검색창
keyword = st.text_input("Enter keyword")

# 버튼
if st.button("Search News"):

    # 키워드 입력 확인
    if keyword:

        with st.spinner("Searching news..."):

            # Google Search Tool 활성화
            grounding_tool = types.Tool(
                google_search=types.GoogleSearch()
            )

            # 설정
            config = types.GenerateContentConfig(
                tools=[grounding_tool],
                temperature=0.0
            )

            # 프롬프트
            prompt = f"""
            Find 2 latest news articles about {keyword}.

            Return:
            - Title
            - Source
            - Date
            - Summary
            - Link
            """

            # Gemini 호출
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=config
            )

            # 결과 출력
            st.subheader("Search Result")
            st.write(response.text)

    else:
        st.warning("Please enter a keyword.")
