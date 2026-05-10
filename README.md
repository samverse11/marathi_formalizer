# Marathi Formalizer

A simple tool to convert informal Marathi sentences into formal language using natural language processing.

## How It Works

- **Preprocessing:** Sentences are normalized, tokenized, and mapped using custom dictionaries and synonym lists.
- **Retrieval-Based Approach:** Uses TF-IDF embeddings and cosine similarity to match the most relevant formal sentence from a dataset.
- **Web & CLI:** Streamlit web app for user input and support for command-line usage.

## Usage

### Web UI
Run:
```bash
streamlit run app.py
```
Enter an informal Marathi sentence to receive a formalized version.

### Command Line
Run:
```bash
python src/test_model.py
```
or
```bash
python src/inference.py
```

## Requirements

- Python 3.10+
- See `requirements.txt` for dependencies

## NLP Techniques Used

- Text normalization (indicnlp)
- Tokenization
- Synonym and dictionary mapping
- TF-IDF vectorization
- Cosine similarity

---
## Preprocessing Steps

- **Unicode Normalization:** Standardizes and cleans Marathi text for consistent processing.
- **Tokenization:** Splits input into language-appropriate tokens for better handling.
- **Custom Dictionary Mapping:** Replaces informal phrases with formal equivalents using curated lookup tables.
- **Synonym Replacement:** Normalizes variants and synonyms to a consistent, formal representation.
- **Punctuation Cleaning:** Removes or replaces special characters and punctuation for cleaner text analysis.

---

**Dataset and model files must be present as described in the repo.**
