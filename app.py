import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Custom CSS
st.markdown("""
<style>
    .main {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    h1 {
        color: #1E3A8A;
        padding-bottom: 1rem;
    }
    h3 {
        color: #2563EB;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Judul Website
st.title("📈 Performa Model dalam Peramalan Harga Saham Berdasarkan Indikator Teknikal dan Sentimen Pasar")

# Deskripsi dalam card
st.markdown("""
<div style='padding: 1rem; background-color: #F3F4F6; border-radius: 10px; margin: 1rem 0;'>
    <h4 style='color: #1E3A8A;'>Informasi Dataset:</h4>
    • Peramalan fokus pada harga penutupan saham BBCA<br>
    • Sentimen pasar dari judul berita IHSG dan The Fed<br>
    • Data sentimen dilatih menggunakan dataset FSA<br>
    • Periode: 2 Januari 2020 - 26 September 2024<br>
    • Model: Transformer, BiLSTM, LSTM, dan GRU dengan TensorFlow
</div>
""", unsafe_allow_html=True)

# Data
testing_data = [
    {"name": "Univariat GRU", "rmse": 125.67, "link": "https://univar-gru.netlify.app/"},
    {"name": "Univariat LSTM", "rmse": 160.47, "link": "https://univar-lstm.netlify.app/"},
    {"name": "Multivariat GRU", "rmse": 144.62, "link": "https://7tis-indobert-gru.netlify.app/"},
    {"name": "Multivariat LSTM", "rmse": 166.97, "link": "https://7tis-indobert-lstm.netlify.app/"},
    {"name": "Multivariat BiLSTM", "rmse": 173.33, "link": "https://7tis-indobert-bilstm.netlify.app/"},
    {"name": "Multivariat Transformer", "rmse": 766.37, "link": "https://7tis-indobert-transformer.netlify.app/"}
]

future_data = [
    {"name": "Univariat GRU", "rmse": 275.28, "link": "https://univar-gru.netlify.app/"},
    {"name": "Univariat LSTM", "rmse": 505.67, "link": "https://univar-lstm.netlify.app/"},
    {"name": "Multivariat GRU", "rmse": 772.78, "link": "https://7tis-indobert-gru.netlify.app/"},
    {"name": "Multivariat LSTM", "rmse": 257.32, "link": "https://7tis-indobert-lstm.netlify.app/"},
    {"name": "Multivariat BiLSTM", "rmse": 399.07, "link": "https://7tis-indobert-bilstm.netlify.app/"},
    {"name": "Multivariat Transformer", "rmse": 1790.17, "link": "https://7tis-indobert-transformer.netlify.app/"}
]

# Convert to DataFrames
testing_df = pd.DataFrame(testing_data)
future_df = pd.DataFrame(future_data)

# Helper function for color gradient
def get_color_scale(value, min_val, max_val):
    if value == min_val:
        return '#2563EB'  # Blue for best
    elif value == max_val:
        return '#EF4444'  # Red for worst
    else:
        # Calculate position in range
        position = (value - min_val) / (max_val - min_val)
        if position < 0.33:
            return '#60A5FA'  # Light blue
        elif position < 0.66:
            return '#FB923C'  # Light orange
        else:
            return '#F87171'  # Light red

# Testing Data Chart
testing_min_rmse = testing_df['rmse'].min()
testing_max_rmse = testing_df['rmse'].max()
st.subheader("📊 Performa Model pada Data Testing")
fig_testing = go.Figure(data=[
    go.Bar(
        x=testing_df['name'],
        y=testing_df['rmse'],
        marker_color=[get_color_scale(val, testing_min_rmse, testing_max_rmse) for val in testing_df['rmse']],
        text=testing_df['rmse'].round(2),
        textposition='outside'
    )
])
fig_testing.update_layout(
    title="RMSE pada Data Testing",
    xaxis_title="Model",
    yaxis_title="RMSE",
    plot_bgcolor='white',
    showlegend=False,
    height=500
)
fig_testing.update_xaxes(tickangle=45)
st.plotly_chart(fig_testing, use_container_width=True)

# Future Data Chart
future_min_rmse = future_df['rmse'].min()
future_max_rmse = future_df['rmse'].max()
st.subheader("🔮 Performa Model pada Data Future")
fig_future = go.Figure(data=[
    go.Bar(
        x=future_df['name'],
        y=future_df['rmse'],
        marker_color=[get_color_scale(val, future_min_rmse, future_max_rmse) for val in future_df['rmse']],
        text=future_df['rmse'].round(2),
        textposition='outside'
    )
])
fig_future.update_layout(
    title="RMSE pada Data Future",
    xaxis_title="Model",
    yaxis_title="RMSE",
    plot_bgcolor='white',
    showlegend=False,
    height=500
)
fig_future.update_xaxes(tickangle=45)
st.plotly_chart(fig_future, use_container_width=True)

# Links in cards
st.markdown("### 🔗 Link Model Deployment")
cols = st.columns(3)
for idx, row in testing_df.iterrows():
    with cols[idx % 3]:
        st.markdown(f"""
        <div style='padding: 1rem; background-color: #F3F4F6; border-radius: 10px; margin: 0.5rem 0; text-align: center;'>
            <a href='{row['link']}' style='color: #2563EB; text-decoration: none; font-weight: bold;'>{row['name']}</a>
        </div>
        """, unsafe_allow_html=True)