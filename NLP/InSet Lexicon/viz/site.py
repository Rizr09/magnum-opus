import streamlit as st
import pandas as pd
import re
import json
import numpy as np

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def load_lexicon(file_path):
    lexicon = pd.read_csv(file_path, sep='\t', header=0, names=['word', 'weight'])
    lexicon['weight'] = pd.to_numeric(lexicon['weight'], errors='coerce')
    lexicon['length'] = lexicon['word'].apply(lambda x: len(x.split()))
    return lexicon.sort_values(by='length', ascending=False).reset_index(drop=True)

@st.cache_data
def load_lexicons():
    positive_lexicon = load_lexicon('../positive.tsv')
    negative_lexicon = load_lexicon('../negative.tsv')
    return positive_lexicon, negative_lexicon

def calculate_sentiment(text, positive_lexicon, negative_lexicon):
    text = preprocess_text(text)
    sentiment_score = 0
    words = text.split()
    positive_words = []
    negative_words = []
    
    for i in range(len(words)):
        for j in range(len(words), i, -1):
            phrase = ' '.join(words[i:j])
            
            pos_match = positive_lexicon[positive_lexicon['word'] == phrase]
            if not pos_match.empty:
                score = pos_match.iloc[0]['weight']
                sentiment_score += score
                positive_words.append(phrase)
                words[i:j] = [''] * (j-i)
                break
            
            neg_match = negative_lexicon[negative_lexicon['word'] == phrase]
            if not neg_match.empty:
                score = neg_match.iloc[0]['weight']
                sentiment_score += score
                negative_words.append(phrase)
                words[i:j] = [''] * (j-i)
                break
    
    word_count = len(text.split())
    comparative = sentiment_score / word_count if word_count > 0 else 0
    
    verdict = "POSITIVE" if sentiment_score > 0 else "NEGATIVE" if sentiment_score < 0 else "NEUTRAL"
    
    result = {
        "verdict": verdict,
        "score": float(sentiment_score),  # Convert to float
        "comparative": float(comparative),  # Convert to float
        "positive": positive_words,
        "negative": negative_words
    }
    
    return result

# JSON encoder to handle numpy types
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

st.title('Analisis Sentimen')

positive_lexicon, negative_lexicon = load_lexicons()

text_input = st.text_area("Masukkan teks untuk dianalisis:", height=100)

if st.button('Analisis Sentimen'):
    if text_input:
        result = calculate_sentiment(text_input, positive_lexicon, negative_lexicon)
        
        st.subheader('Hasil Analisis:')
        st.json(json.dumps(result, indent=2, ensure_ascii=False, cls=NpEncoder))
        
        st.subheader('Interpretasi:')
        st.write(f"Verdict: **{result['verdict']}**")
        st.write(f"Score: **{result['score']}**")
        st.write(f"Comparative Score: **{result['comparative']:.4f}**")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write("Kata-kata Positif:")
            st.write(", ".join(result['positive']) if result['positive'] else "Tidak ada")
        with col2:
            st.write("Kata-kata Negatif:")
            st.write(", ".join(result['negative']) if result['negative'] else "Tidak ada")
    else:
        st.warning('Silakan masukkan teks untuk dianalisis.')

st.sidebar.header('Tentang Aplikasi')
st.sidebar.info('Aplikasi ini menggunakan analisis sentimen berbasis leksikon untuk mengevaluasi sentimen dari teks yang dimasukkan.')