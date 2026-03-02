import streamlit as st
from utils import extract_text_from_pdf, get_ats_score

st.set_page_config(page_title="AI Resume Checker", layout="wide")

st.title("🤖 AI-Based ATS Resume Score Checker")
st.markdown("Check how well your resume matches the job description using NLP.")

# Create two columns for a clean look
col1, col2 = st.columns(2)

with col1:
    st.subheader("📁 Upload Your Resume")
    uploaded_file = st.file_uploader("Upload PDF version of your resume", type=["pdf"])

with col2:
    st.subheader("📝 Job Description")
    jd_text = st.text_area("Paste the job requirements here...", height=300)

if st.button("Calculate ATS Score"):
    if uploaded_file and jd_text:
        with st.spinner('AI is analyzing...'):
            resume_text = extract_text_from_pdf(uploaded_file)
            score = get_ats_score(resume_text, jd_text)
            
            st.divider()
            st.success(f"### Match Score: {score}%")
            
            if score >= 70:
                st.balloons()
                st.write("✨ **Strong Match!** Your resume aligns well with this role.")
            else:
                st.warning("⚠️ **Low Match.** Consider adding more keywords from the job description.")
    else:
        st.error("Please upload a file and paste the job description first!")