import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
from indicnlp.tokenize.indic_tokenize import trivial_tokenize
import os

# -----------------
# Dictionaries
# -----------------
marathi_dictionary = {
    "हाय": "नमस्कार",
    "बाय": "पुन्हा भेटूया",
    "थॅंक्यू": "धन्यवाद",
    "काय चाललंय?": "सध्या काय सुरू आहे?",
    "कसा आहेस?": "आपण कसे आहात?",
    "कशी आहेस?": "आपण कशा आहात?",
    "कसं काय?": "आपण कसे आहात?",
    "कुठं जातोस?": "आपण कुठे जात आहात?",
    "मी येतो": "मी येत आहे",
    "मी तुला कॉल करतो": "मी तुम्हाला फोन करतो",
    "चल भेटू": "आपण भेटूया",
    "मला झोप येतेय": "मला झोप येत आहे",
    "मला काही विचारायचं आहे": "मला काही विचारायचे आहे",
    "तू कुठे आहेस?": "आपण कुठे आहात?",
    "तुला कळलं का?": "आपल्याला समजले का?",
    "जेवण झालं का?": "आपले जेवण झाले आहे का?",
    "मस्त आहे": "छान आहे",
    "भारी आहे": "खूप छान आहे",
}

synonym_dict = {
    "रे": "महोदय",
    "अगं": "महोदया",
    "हाय": "नमस्कार",
    "हो": "होय",
    "काय": "काय आहे",
    "झालं": "झाले आहे",
    "झालंय": "झाले आहे",
    "झालेय": "झाले आहे",
    "माहित": "माहिती",
    "चल": "चला",
    "बघ": "पहा",
    "सांग": "कृपया सांगा",
    "ना": "कृपया",
    "मला": "माझ्यासाठी",
    "नंतर": "पश्चात",
    "भेटू": "भेटूया",
    "कॉल": "फोन",
    "भारी": "छान",
    "मस्त": "छान",
    "खूप": "अत्यंत",
    "थांब": "थांबा",
}

# ---------
# Cleaning / preprocessing
# ---------
PUNCT = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~।…–—'
TRANS = str.maketrans({c: " " for c in PUNCT})

factory = IndicNormalizerFactory()
normalizer = factory.get_normalizer("mr")

def marathi_lemmatize(text: str) -> str:
    text = normalizer.normalize(text)
    return ' '.join(trivial_tokenize(text, lang="mr"))

def normalize_synonyms(text: str) -> str:
    words = text.split()
    return ' '.join(synonym_dict.get(w, w) for w in words)

def preprocess_sentence(sentence: str) -> str:
    if sentence in marathi_dictionary:  # direct mapping first
        return marathi_dictionary[sentence]
    sentence = sentence.translate(TRANS)
    sentence = sentence.strip()
    sentence = marathi_lemmatize(sentence)
    sentence = normalize_synonyms(sentence)
    return sentence

# -----------------
# Load vectorizer + dataset
# -----------------
VECTOR_PATH = os.path.join(os.path.dirname(__file__), "..", "vectorizer.pkl")
DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "processed_dataset.csv")

vectorizer = joblib.load(VECTOR_PATH)
df = pd.read_csv(DATASET_PATH)

informal_sentences = df["input_processed"].fillna("").tolist()
formal_sentences = df["target_processed"].fillna("").tolist()
informal_vectors = vectorizer.transform(informal_sentences)

# -----------------
# Retrieval function
# -----------------
def formalize_sentence(user_sentence: str) -> str:
    """Given an informal Marathi sentence, return the most similar formal sentence."""
    processed = preprocess_sentence(user_sentence)
    user_vec = vectorizer.transform([processed])
    similarities = cosine_similarity(user_vec, informal_vectors)
    best_idx = similarities.argmax()
    return formal_sentences[best_idx]
