# Integrasi Analisis Sentimen Pasar dan Indikator Teknikal pada Peramalan Harga Saham di Indonesia Berbasis Deep Learning
By Rizky Ramadhan S - 140810210004  

## **Tahapan Keseluruhan**

### **Preprocess News**
- Dataset berita tersedia di: `Tugas Akhir\Data\News`
- Membersihkan data dengan:
  - Menghapus simbol yang tidak berguna dari title
  - Menggabungkan data
  - Mengurutkan berdasarkan tanggal
  - Notebook terkait: `Tugas Akhir\NLP\Datasets\sync_date.ipynb`
- Menerjemahkan dataset Financial Sentiment Analysis ke Bahasa Indonesia
- Mengonversi label sentimen menjadi angka:
  - Positif = 2
  - Netral = 1
  - Negatif = 0
  - Notebook terkait: `Tugas Akhir\NLP\Datasets\clean_datasets.ipynb`
- Mengunggah dataset ke Hugging Face untuk kemudahan hosting: [Hugging Face Dataset](https://huggingface.co/datasets/rizr09/fin-dataset)

---

### **Preprocess Saham**
- Mengunduh data saham BBCA dari **2020-01-01 hingga 2024-09-26**
  - [Google Colab Link](https://colab.research.google.com/drive/1ulbOtWHYH3ETynitGvjR5yQNk_89gkZ3?usp=sharing)
- Membuat indikator teknikal menggunakan **TA-Lib**
  - Script terkait: `Tugas Akhir\Time Series\generate_technical_indicator.py`
- Memilih 7 indikator teknikal berdasarkan studi empiris:
  1. Xu, Y., & Keselj V. (2019). [Stock Prediction Using Deep Learning and Sentiment Analysis](https://doi.org/10.1109/BigData47090.2019.9006342)
  2. Sim, H. S., Kim, H. I., & Ahn, J. J. (2019). [Is Deep Learning for Image Recognition Applicable to Stock Market Prediction?](https://doi.org/10.1155/2019/4324878)
  3. Tan, X., Li, S., Wang, C., & Wang, S. (2020). [Enhancing High Frequency Technical Indicators Forecasting Using Shrinking Deep Neural Networks](https://doi.org/10.1109/icim49319.2020.244707)
  4. 7 indikator terakhir didapat dari eksperimen.

---

### **Sentimen Analisis**
- Analisis sentimen **Financial Sentiment Analysis** menggunakan:
  1. **IndoBERT**: [Kaggle Notebook](https://www.kaggle.com/code/rizr09/indobert-skripsi)
  2. **Lexicon-based**: `Tugas Akhir\NLP\InSet Lexicon\lexicon_report.ipynb`
- Memilih **IndoBERT** dengan F1 Score **81%**
- Melakukan **group by** per hari dan rata-rata skor sentimen:
  - Positive = 1
  - Neutral = 0
  - Negative = -1
  - Notebook terkait: `Tugas Akhir\NLP\IndoBERT\avg_sentiment_per_day.ipynb`
- Menggunakan **KNN (n=5)** untuk mengisi nilai sentimen yang kosong per hari
  - Notebook terkait: `Tugas Akhir\NLP\IndoBERT\count_sentiment_per_day_sync.ipynb`

---

### **Forecast Stock**
- **Menggabungkan** data sentimen, harga saham, indikator teknikal, dan sentimen pasar
  - Notebook terkait: `Tugas Akhir\Time Series\merge.ipynb`
- **Melakukan forecasting** menggunakan beberapa model:
  1. **Multivariat**: Transformer, BiLSTM, LSTM, GRU
  2. **Univariat**: LSTM, GRU
  - [Kaggle Notebook](https://www.kaggle.com/code/rizr09/final-skripsi/edit/run/200034866)
