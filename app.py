# app.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

app = FastAPI(title="Job Resume Matcher API")

class JobResumeRequest(BaseModel):
    job_description: str
    resume: str

class MatchResponse(BaseModel):
    match_score: float
    match_percentage: float
    key_terms_found: list
    missing_terms: list

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

def extract_key_terms(text, top_n=20):
    vectorizer = TfidfVectorizer(max_features=100)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    
    scores = zip(feature_names, tfidf_matrix.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    return [term for term, score in sorted_scores[:top_n] if score > 0]

@app.post("/match/", response_model=MatchResponse)
async def match_resume_to_job(request: JobResumeRequest):
    if not request.job_description or not request.resume:
        raise HTTPException(status_code=400, detail="Both job description and resume must be provided")
    
    processed_job = preprocess_text(request.job_description)
    processed_resume = preprocess_text(request.resume)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([processed_job, processed_resume])
    
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    job_terms = extract_key_terms(processed_job)
    resume_terms = extract_key_terms(processed_resume)
    
    terms_found = [term for term in job_terms if term in resume_terms]
    missing_terms = [term for term in job_terms if term not in resume_terms]
    
    match_percentage = similarity_score * 100
    
    return MatchResponse(
        match_score=similarity_score,
        match_percentage=match_percentage,
        key_terms_found=terms_found,
        missing_terms=missing_terms
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Matcher API. Use POST /match/ endpoint."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)