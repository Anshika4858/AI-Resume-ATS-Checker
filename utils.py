import PyPDF2
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_ats_score(resume_text, job_description):
    content = [resume_text, job_description]
    cv = TfidfVectorizer()
    matrix = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(matrix)
    match_percentage = similarity_matrix[0][1] * 100
    return round(match_percentage, 2)

def get_missing_keywords(resume_text, job_description):
    # Clean and split into individual words
    resume_words = set(re.findall(r'\w+', resume_text.lower()))
    jd_words = set(re.findall(r'\w+', job_description.lower()))
    
    # Identify words in JD that are NOT in Resume
    missing = jd_words - resume_words
    
    # Filter for meaningful words
    common_fillers = {'with', 'from', 'that', 'this', 'your', 'have', 'experience', 'knowledge'}
    suggested_skills = [word for word in missing if len(word) > 3 and word not in common_fillers]
    
    return suggested_skills[:10]