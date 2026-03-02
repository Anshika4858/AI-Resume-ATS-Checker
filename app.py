import streamlit as st
from utils import extract_text_from_pdf, get_ats_score, get_missing_keywords

st.set_page_config(page_title="AI Resume Checker", layout="wide")

st.title("🤖 AI-Based ATS Resume Score Checker")
st.markdown("Check how well your resume matches the job description using NLP.")

# You need these lines to define the variables!
col1, col2 = st.columns(2)

with col1:
    st.subheader("📁 Upload Your Resume")
    uploaded_file = st.file_uploader("Upload PDF version of your resume", type=["pdf"])

with col2:
    st.subheader("📝 Job Description")
    jd_text = st.text_area("Paste the job requirements here...", height=300)

# Now the button can use those variables
if st.button("Calculate ATS Score"):
    if uploaded_file and jd_text:
        with st.spinner('AI is analyzing...'):
            resume_text = extract_text_from_pdf(uploaded_file)
            score = get_ats_score(resume_text, jd_text)
            
            st.divider()
            st.success(f"### Match Score: {score}%")
            
            st.subheader("💡 Suggested Changes & Missing Keywords")
            missing_keywords = get_missing_keywords(resume_text, jd_text)
            
            if missing_keywords:
                st.write("To improve your score, consider adding these keywords:")
                st.write(", ".join([f"**{word}**" for word in missing_keywords]))
            else:
                st.write("Great job! You have covered most of the key terms.")

            if score >= 70:
                st.balloons()
            else:
                st.warning("⚠️ Improvement needed. See the suggestions above.")