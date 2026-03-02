import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def get_ats_score(resume_text, job_description):
    # This creates a list containing both texts to compare them
    content = [resume_text, job_description]
    cv = TfidfVectorizer()
    matrix = cv.fit_transform(content)
    similarity_matrix = cosine_similarity(matrix)
    
    # The match score is found at index [0][1] of the matrix
    match_percentage = similarity_matrix[0][1] * 100
    return round(match_percentage, 2)