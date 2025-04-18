1. Atvērt termināli mapē

// sāk darbu virtuālajā vidē + uzinstalē bibliotēkas + palaiž API serveri
2. python -m venv venv
3. venv\Scripts\activate
4. pip install setuptools
5. pip install -r requirements.txt
6. python app.py

// izveidot pieprasījumu uz serveri
7. pip install requests
8. python example.py

Saņem atbildi:

Response:
{
  "match_score": 0.22311249032339006,
  "match_percentage": 22.311249032339006,
  "key_terms_found": [
    "python",
    "cloud",
    "django",
    "docker",
    "learning"
  ],
  "missing_terms": [
    "experience",
    "strong",
    "attention",
    "aws",
    "containerization",
    "database",
    "design",
    "detail",
    "developer",
    "familiarity",
    "fastapi",
    "gcp",
    "knowledge",
    "libraries",
    "like"
  ]
}