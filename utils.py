import re

def get_missing_keywords(resume_text, job_description):
    # Clean and split into individual words
    resume_words = set(re.findall(r'\w+', resume_text.lower()))
    jd_words = set(re.findall(r'\w+', job_description.lower()))
    
    # Identify words in JD that are NOT in Resume
    missing = jd_words - resume_words
    
    # Filter for meaningful words (usually longer than 3 characters)
    # and remove common filler words
    common_fillers = {'with', 'from', 'that', 'this', 'your', 'have', 'experience', 'knowledge'}
    suggested_skills = [word for word in missing if len(word) > 3 and word not in common_fillers]
    
    # Return the top 10 most relevant missing words
    return suggested_skills[:10]