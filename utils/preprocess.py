import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()


def handle_negation_enhanced(text):
    """Enhanced negation handling"""

    # More comprehensive negation list
    negations = [
        "tidak",
        "tak",
        "bukan",
        "jangan",
        "belum",
        "tanpa",
        "gak",
        "ga",
        "engga",
        "nggak",
        "kagak",
        "ngg",
        "ngga",  # ← Slang variations!
        "gk",
        "g",
        "tdk",  # Abbreviations
    ]

    for neg in negations:
        # More flexible pattern (handle spacing issues)
        pattern = r"\b" + neg + r"\s+(\w+)"
        text = re.sub(pattern, r"not \1", text)

    return text


def preprocess_text(text):
    """
    Preprocessing steps:
    1. Lowercase
    2. Remove special characters
    3. Remove stopwords
    4. Stemming
    """
    # Lowercase
    text = text.lower()

    # Remove special characters and digits
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    text = stemmer.stem(text)

    return handle_negation_enhanced(text)
