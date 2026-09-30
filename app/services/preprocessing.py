import re

from nltk.stem import PorterStemmer
from nltk.tokenize import wordpunct_tokenize


stemmer = PorterStemmer()


STOP_WORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "am",
    "was",
    "were",
    "what",
    "how",
    "can",
    "could",
    "would",
    "should",
    "i",
    "you",
    "your",
    "my",
    "our",
    "we",
    "to",
    "of",
    "for",
    "in",
    "on",
    "at",
    "do",
    "does",
    "did",
    "and",
    "or",
    "with",
    "this",
    "that",
    "it",
    "me",
    "from",
    "about",
}


def preprocess_text(text: str) -> str:
    """
    Preprocess text using:
    1. Lowercase
    2. Remove special characters
    3. Tokenization
    4. Stop-word removal
    5. Stemming
    """

    if not isinstance(text, str):
        return ""

    # 1. Convert text to lowercase
    text = text.lower()

    # 2. Remove special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # 3. Tokenize
    tokens = wordpunct_tokenize(text)

    processed_tokens: list[str] = []

    for token in tokens:

        # Ignore non-alphanumeric tokens
        if not token.isalnum():
            continue

        # 4. Remove stop words
        if token in STOP_WORDS:
            continue

        # 5. Apply stemming
        stemmed_token = stemmer.stem(token)

        processed_tokens.append(stemmed_token)

    return " ".join(processed_tokens)