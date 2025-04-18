import requests
import json

url = "http://localhost:8000/match/"

job_description = """
Senior Python Developer
Requirements:
- 5+ years of experience with Python
- Strong knowledge of FastAPI or Django
- Experience with machine learning libraries like scikit-learn and TensorFlow
- Proficient in SQL and database design
- Familiarity with cloud services (AWS, GCP)
- Experience with Docker and containerization
- Strong problem-solving skills and attention to detail
"""

resume = """
PROFESSIONAL SUMMARY
Experienced software engineer with 7 years of Python development expertise. Skilled in web frameworks, data analysis, and cloud infrastructure. Strong background in implementing machine learning solutions using scikit-learn.

SKILLS
Programming Languages: Python, JavaScript, SQL
Frameworks: Django, Flask, React
Machine Learning: scikit-learn, pandas, numpy
Cloud: AWS (EC2, S3, Lambda)
Tools: Git, Docker, Jenkins

EXPERIENCE
Senior Python Developer | Tech Solutions Inc. | 2020-Present
- Developed scalable APIs using Django Rest Framework
- Implemented data processing pipelines using pandas and numpy
- Containerized applications using Docker and Docker Compose
- Collaborated with data scientists to deploy ML models

Python Engineer | Data Insights Corp | 2017-2020
- Created data visualization dashboards using Plotly and Dash
- Developed ETL processes for large datasets
- Implemented CI/CD pipelines using GitHub Actions
"""

payload = {
    "job_description": job_description,
    "resume": resume
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response:")
print(json.dumps(response.json(), indent=2))
