import streamlit as st
import openai
import os

st.set_page_config(page_title="IT 센싱 리포트 생성기", layout="wide")
st.title("📊 Weekly IT 센싱 리포트 생성기")

openai_api_key = st.text_input("🔑 OpenAI API 키 입력", type="password")

topic = st.text_input("📌 키워드 (예: 로봇, 전고체배터리 등)")
period = st.selectbox("🗓️ 분석 기간", ["1주", "2주", "1달"])

if st.button("리포트 생성하기"):
    if not openai_api_key:
        st.warning("API 키를 입력해주세요.")
    elif not topic:
        st.warning("키워드를 입력해주세요.")
    else:
        openai.api_key = openai_api_key
        prompt = f"""
        다음 키워드에 대해 최근 {period} 간의 뉴스 동향을 분석해서 요약해줘.
        키워드: {topic}

        형식:
        1. 핵심 뉴스 요약 (3개 정도)
        2. 시사점 및 인사이트
        3. 출처 URL이 있으면 포함
        """

        with st.spinner("GPT가 리포트를 작성 중입니다..."):
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.success("✅ 리포트 생성 완료!")
            st.text_area("📄 생성된 리포트", result, height=400)
