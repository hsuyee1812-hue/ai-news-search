import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="AI News Search",
    layout="wide"
)

# 제목
st.title("AI Latest News Search App")

# Gemini API 연결
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# 입력창
keyword = st.text_input("Enter keyword")

# 버튼
if st.button("Search News"):

    # 키워드 확인
    if keyword:

        with st.spinner("Searching..."):

            # 프롬프트
            prompt = f"""
Tell me 2 recent news topics about {keyword}.

For each news topic include:
1. Title
2. Summary
"""

            try:

                # Gemini 호출
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                # 결과 출력
                st.subheader("Search Result")

                result_text = response.text

                st.write(result_text)

            except Exception as e:

                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a keyword.")
