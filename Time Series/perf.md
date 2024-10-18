# Perbandingan Performa BiLSTM (MAE, MSE, RMSE, MAPE) 
**Running Trial:** 25  
**Code:** https://www.kaggle.com/code/rizr09/final-skripsi  
Summary:
- Data yang digunakan adalah data 7 TIs dan data IndoBERT
- 7 teknikator indikator yang digunakan adalah: 
  - Moving Average Convergence/Divergence (12, 26)
  - Relative Strength Index (28)
  - Stochastic Oscillator (k, d)
  - Exponential Moving Average (20)
  - Bollinger Bands (20, 2)
  - Simple Moving Average (20)
  - Volume
- Lexicon-based tidak digunakan karena hasil analisis sentimen yang jauh dari kata akurat
- Metode time series yang digunakan adalah BiLSTM, LSTM, GRU, dan Transformer
- Semakin kompleks arsitektur yang digunakan, proyeksi yang dihasilkan justru semakin buruk.
- Secara MAE, MSE, RMSE, dan MAPE memang Univariate GRU yang paling baik, namun proyeksi yang dihasilkan tidak sesuai dengan tren data aktual.
- Proyeksi yang paling baik adalah yang dihasilkan oleh model Multivariate GRU, namun secara MAE, MSE, RMSE, dan MAPE masih kalah dengan Univariate GRU.

## 7 TIs + IndoBERT W Transformer
### Trial 09 Summary

**Hyperparameters:**
- `num_transformer_blocks`: 4  
- `num_heads`: 5  
- `ff_dim`: 64  
- `dropout_rate`: 0.2  
- `num_dense_layers`: 1  
- `dense_units`: 192  
- `dense_dropout`: 0.2  

**Score:** 0.0006428841006709263  

---

### Model: "functional_4"

| Layer (type)               | Output Shape   | Param # |
| -------------------------- | -------------- | ------- |
| `input_layer (InputLayer)` | (None, 14, 11) | 0       |
| `transformer_block`        | (None, 14, 11) | 4,123   |
| `transformer_block_1`      | (None, 14, 11) | 4,123   |
| `transformer_block_2`      | (None, 14, 11) | 4,123   |
| `transformer_block_3`      | (None, 14, 11) | 4,123   |
| `global_average_pooling1d` | (None, 11)     | 0       |
| `dense_8 (Dense)`          | (None, 192)    | 2,304   |
| `dropout_12 (Dropout)`     | (None, 192)    | 0       |
| `dense_9 (Dense)`          | (None, 1)      | 193     |

**Total params:** 18,989 (74.18 KB)  
**Trainable params:** 18,989 (74.18 KB)  
**Non-trainable params:** 0 (0.00 B)  

---

**Metrics:**
- **MSE:** 343749.3602  
- **MAE:** 452.8305  
- **RMSE:** 586.3014  
- **MAPE:** 4.5636%  

---

## <a href="https://7tis-indobert-transformer-rizr09.netlify.app/" target='_blank'>Interactive Plot</a>
<img src="https://i.ibb.co.com/s1pzBqX/7tis-indobert-transformer.png" alt="transformer" width="800"/>

---

## 7 TIs + IndoBERT W BiLSTM
### Trial 00 Summary

**Hyperparameters:**
- `units_1`: 128  
- `dropout_1`: 0.4  
- `units_2`: 96  
- `dropout_2`: 0.3  
- `units_3`: 256  

**Score:** 0.00025109827402047813  

---

### Model: "sequential"

| Layer (type)                      | Output Shape    | Param # |
| --------------------------------- | --------------- | ------- |
| `bidirectional (Bidirectional)`   | (None, 14, 256) | 143,360 |
| `dropout (Dropout)`               | (None, 14, 256) | 0       |
| `bidirectional_1 (Bidirectional)` | (None, 14, 192) | 271,104 |
| `dropout_1 (Dropout)`             | (None, 14, 192) | 0       |
| `bidirectional_2 (Bidirectional)` | (None, 512)     | 919,552 |
| `dense (Dense)`                   | (None, 1)       | 513     |

**Total params:** 1,334,529 (5.09 MB)  
**Trainable params:** 1,334,529 (5.09 MB)  
**Non-trainable params:** 0 (0.00 B)  

---

**Metrics:**
- **MSE:** 30043.6704  
- **MAE:** 138.5850  
- **RMSE:** 173.3311  
- **MAPE:** 1.4417%  

---

## <a href="https://7tis-indobert-bilstm-rizr09.netlify.app/" target='_blank'>Interactive Plot</a>
<img src="https://i.ibb.co.com/FWBmGW0/7tis-indobert-bilstm.png" alt="bilstm" width="800"/>

---

## 7 TIs + IndoBERT W LSTM
### Trial 08 Summary

**Hyperparameters:**
- `units_1`: 128  
- `dropout_1`: 0.35  
- `units_2`: 320  
- `dropout_2`: 0.3  
- `units_3`: 448  

**Score:** 0.00039979560824576765  

---

### Model: "sequential"

| Layer (type)          | Output Shape    | Param #   |
| --------------------- | --------------- | --------- |
| `lstm (LSTM)`         | (None, 14, 128) | 71,680    |
| `dropout (Dropout)`   | (None, 14, 128) | 0         |
| `lstm_1 (LSTM)`       | (None, 14, 320) | 574,720   |
| `dropout_1 (Dropout)` | (None, 14, 320) | 0         |
| `lstm_2 (LSTM)`       | (None, 448)     | 1,378,048 |
| `dense (Dense)`       | (None, 1)       | 449       |

**Total params:** 2,024,897 (7.72 MB)  
**Trainable params:** 2,024,897 (7.72 MB)  
**Non-trainable params:** 0 (0.00 B)  

---

**Metrics:**
- **MSE:** 34293.0025  
- **MAE:** 147.4623  
- **RMSE:** 185.1837  
- **MAPE:** 1.5522%  

---

## <a href="https://7tis-indobert-lstm-rizr09.netlify.app/" target='_blank'>Interactive Plot</a>
<img src="https://i.ibb.co.com/3Rbh1Bt/7tis-indobert-lstm.png" alt="lstm" width="800"/>

---

## 7 TIs + IndoBERT W GRU
### Trial 0 Summary

**Hyperparameters:**
- `units_1`: 512
- `dropout_1`: 0.15
- `units_2`: 256
- `dropout_2`: 0.30
- `units_3`: 512

**Score:** 0.0002464966382831335

---

### Model: "sequential"

| Layer (type)          | Output Shape    | Param #   |
| --------------------- | --------------- | --------- |
| `gru (GRU)`           | (None, 14, 512) | 806,400   |
| `dropout (Dropout)`   | (None, 14, 512) | 0         |
| `gru_1 (GRU)`         | (None, 14, 256) | 591,360   |
| `dropout_1 (Dropout)` | (None, 14, 256) | 0         |
| `gru_2 (GRU)`         | (None, 512)     | 1,182,720 |
| `dense (Dense)`       | (None, 1)       | 513       |

**Total params:** 2,580,993 (9.85 MB)  
**Trainable params:** 2,580,993 (9.85 MB)  
**Non-trainable params:** 0 (0.00 B)  

---

**Metrics:**
- **MSE:** 23810.6023  
- **MAE:** 119.7513  
- **RMSE:** 154.3068  
- **MAPE:** 1.2511%


---

## <a href="https://7tis-indobert-gru-rizr09.netlify.app/" target='_blank'>Interactive Plot</a>
<img src="https://i.ibb.co.com/dJXLvpf/7tis-indobert-gru.png" alt="gru" width="800"/>

---

## Univariate w GRU
### Trial 03 Summary

**Hyperparameters:**
- `units_1`: 512  
- `dropout_1`: 0.2  
- `units_2`: 288  
- `dropout_2`: 0.1  
- `units_3`: 256  

**Score:** 0.00022619890660280362  

---

### Model: "sequential"

| Layer (type)          | Output Shape    | Param # |
| --------------------- | --------------- | ------- |
| `gru (GRU)`           | (None, 14, 512) | 791,040 |
| `dropout (Dropout)`   | (None, 14, 512) | 0       |
| `gru_1 (GRU)`         | (None, 14, 288) | 692,928 |
| `dropout_1 (Dropout)` | (None, 14, 288) | 0       |
| `gru_2 (GRU)`         | (None, 256)     | 419,328 |
| `dense (Dense)`       | (None, 1)       | 257     |

**Total params:** 1,903,553 (7.26 MB)  
**Trainable params:** 1,903,553 (7.26 MB)  
**Non-trainable params:** 0 (0.00 B)  

---

**Metrics:**
- **MSE:** 15794.1707  
- **MAE:** 97.5444  
- **RMSE:** 125.6749  
- **MAPE:** 1.0246%  

---

## <a href="https://univariate-gru-rizr09.netlify.app/" target="_blank">Interactive Plot</a>
<img src="https://i.ibb.co.com/Ss0XJpM/univariate-gru.png" alt="univariate" width="800"/>

---