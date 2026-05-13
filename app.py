import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="AI News Search",
    layout="wide"
)

st.title("AI Latest News Search App")

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

keyword = st.text_input("Enter keyword")

if st.button("Search News"):

    if keyword:

        with st.spinner("Searching news..."):

            grounding_tool = types.Tool(
                google_search=types.GoogleSearch()
            )

            config = types.GenerateContentConfig(
                tools=[grounding_tool],
                temperature=0.0
            )

            prompt = f"""
Find 2 latest news articles about {keyword}.

Return:
- Title
- Source
- Date
- Summary
- Link
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=config
            )

            st.subheader("Search Result")

            result_text = response.text.encode(
                "ascii",
                "ignore"
            ).decode()

            st.text(result_text)

    else:
        st.warning("Please enter a keyword.")
