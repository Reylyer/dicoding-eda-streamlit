import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache_data
def init_df_day():
    _df_day = pd.read_csv('dataset/day.csv')
    _df_day = _df_day.replace({
        'season' :{ 1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'},
        'weekday':{0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'},
        'yr' : {0: 2011, 1: 2012 }
    })
    return _df_day

df_day = init_df_day()


st.title("Eksplorasi dataset Bike Sharing")

season_data = df_day.groupby(['season', 'yr']).agg({
    'cnt': 'sum'
}).reset_index(level=[0,1])

st.header("Pengaruh musim", divider='rainbow')

st.plotly_chart(
    px.histogram(season_data, x='season', y='cnt', color='yr', barmode='group', 
             title="Banyak rental sepeda per musim")
)

st.markdown("""
Kami menemukan rental sepeda paling laku ada di musim gugur. 
Ini dimungkinkan dikarenakan suhu yang nyaman untuk bersepeda di luar,
tidak terlalu panas dan tidak terlalu dingin. Kita juga menemukan musim semi sebagai musim yang 
paling sepi aktivitas rental sepeda. Ini mungkin dikarenakan curah hujan yang cukup tinggi atau
alasan lain.
""")

st.header("Pengaruh temperatur", divider='red')
st.plotly_chart(
    px.scatter(df_day, x='temp', y='cnt', title='Temperatur vs Jumlah rental sepeda').update_layout(
             xaxis_title="Temperatur", 
             yaxis_title="Jumlah",
))

st.markdown("""
Dari musim sebelumnya, kami melakukan analisis faktor apa yang mempengaruhi dan memiliki korelasi
dengan jumlah rental sepeda. Yang berkorelasi kuat adalah temperatur. Namun, korelasinya tidak sepenuhnya 
linear. Menuju temperatur yang cukup tinggi, jumlah rental sepeda mulai menurun.
""")

st.header("Pengaruh kecepatan angin", divider='grey')
st.plotly_chart(
    px.scatter(df_day, x='windspeed', y='cnt', title='Kecepatan angin vs Jumlah rental sepeda').update_layout(
             xaxis_title="Kecepatan angin", 
             yaxis_title="Jumlah"
))
st.markdown("""
Dari kecepatan angin, kami tidak melihat korelasi yang signifikan dengan jumlah rental sepeda.
""")


st.header("Pengaruh kelembaban", divider='blue')
st.plotly_chart(
    px.scatter(df_day, x='hum', y='cnt', title='Kelembaban vs Jumlah rental sepeda').update_layout(
             xaxis_title="Kelembaban", 
             yaxis_title="Jumlah"
))

st.markdown("""
Sama dengan kecepatan angin, kami tidak melihat korelasi yang signifikan dengan jumlah rental sepeda.
""")

st.header("Data rental sepeda 2011 - 2012", divider='violet')
st.markdown("""
Berikut merupakan data rental sepeda dari 2011 awal sampai 2012 akhir
""")
st.plotly_chart(
    px.line(df_day, 'dteday', 'cnt', title='Data rental sepeda').update_layout(
             xaxis_title="Tanggal", 
             yaxis_title="Jumlah"
))