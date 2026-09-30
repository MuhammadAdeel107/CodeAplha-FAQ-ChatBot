A simple, lightweight, and practical NLP-based FAQ Chatbot built with Python, Flask, NLTK, Scikit-learn, HTML, CSS, and JavaScript.

The chatbot accepts a user's question, preprocesses the text using NLP techniques, compares it with a predefined FAQ dataset using TF-IDF and Cosine Similarity, and returns the most relevant answer.

Features

FAQ-based question answering

NLP text preprocessing

Lowercase normalization

Special-character cleaning

Tokenization

Stop-word removal

Porter stemming

TF-IDF vectorization

Cosine similarity matching

Configurable similarity threshold

Flask REST API

Responsive chatbot interface

JSON-based FAQ dataset

Automated unit and API tests

Python 3.14 support

uv dependency management

Vercel deployment configuration

No paid AI/API key required

How It Works

User Question
      |
      v
Chatbot UI (HTML/CSS/JavaScript)
      |
      v
POST /api/chat
      |
      v
NLP Preprocessing
(lowercase -> cleaning -> tokenization
 -> stop-word removal -> stemming)
      |
      v
TF-IDF Vectorization
      |
      v
Cosine Similarity
      |
      v
Best FAQ Match
      |
      v
Similarity Threshold Check
      |
      v
Answer Returned to User

Technology Stack

Technology

Purpose

Python 3.14

Backend programming

Flask

Web framework and API

NLTK

NLP preprocessing

Scikit-learn

TF-IDF and cosine similarity

HTML

Chatbot interface

CSS

Responsive styling

JavaScript

Frontend interaction and API calls

JSON

FAQ data storage

uv

Python package/environment management

pytest

Automated testing

Vercel

Deployment

Project Structure

Faq-ChatBot/
├── api/
│   └── index.py
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── chat.py
│   └── services/
│       ├── __init__.py
│       ├── preprocessing.py
│       └── faq_matcher.py
├── data/
│   └── faqs.json
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── tests/
│   ├── test_preprocessing.py
│   ├── test_matcher.py
│   └── test_api.py
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
└── vercel.json

Installation

1. Clone the repository

git clone https://github.com/YOUR-USERNAME/Faq-ChatBot.git
cd Faq-ChatBot

Replace YOUR-USERNAME with your GitHub username.

2. Install dependencies

This project uses uv for Python dependency management.

uv sync

3. Run the application

uv run python -m flask --app api.index run --debug

Open the application in your browser:

http://127.0.0.1:5000

API

The chatbot exposes a POST endpoint:

POST /api/chat

Example request:

{
  "question": "How much does shipping cost?"
}

Example response:

{
  "answer": "Delivery is free for orders over $50. Otherwise, a $5 delivery fee applies.",
  "matched": true,
  "matched_question": "How much does shipping cost?",
  "score": 1.0
}
Example Questions
Try questions such as:
How much does shipping cost?
How long will my order take?
Where can I track my order?
What payment methods do you accept?
Can I pay with a credit card?
Can I cancel my order?
What is your refund policy?
How can I get a refund?
How do I create an account?
I forgot my password
How can I contact customer support?
What are your business hours?
The chatbot can also handle differently worded questions because it uses similarity-based matching rather than
relying only on exact text.

