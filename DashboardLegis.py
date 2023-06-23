import streamlit as st
import pandas as pd
import plotly_express as px
import openpyxl as ox
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# Mengatur konfigurasi tampilan Streamlit
def set_page_config():
        st.set_page_config(
            page_title="Penilaian Gantari",
            page_icon='LOGO EKSE1.png',
            layout="wide",
            initial_sidebar_state="expanded",
        )

# Memanggil fungsi set_page_config()
set_page_config()


dfa= pd.read_excel(
    io='DataContohLegis.xlsx',
    engine='openpyxl',
    sheet_name='PerformaBirdept',
    usecols='A:B')
names = dfa['Nama'].apply(str)
values = dfa['Nilai'].apply(int)

fig1= px.bar(
dfa, y= values,  x=names,
title= 'Fakultas')
print(dfa)
fig1.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )



#Visualisasi Grafik Prestasi Eksekutif Ormawa
#Mendefinisikan fungsi untuk menampilkan animasi Lottie
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Mendefinisikan URL animasi Lottie yang akan ditampilkan
url = "https://assets2.lottiefiles.com/packages/lf20_FAm4ibqGlI.json"


# Menampilkan animasi Lottie di tampilan utama Streamlit
st_lottie(load_lottie_url(url))

col1, col2= st.columns([2,1])
with col1:
            st.title('Dashboard Penilaian Ormawa Legislatif')
            st.subheader("Ormawa Eksekutif PKU IPB Kabinet Gantari Arti")   
with col2:
        # Tampilkan informasi nilai mutu
             st.image('RISBANG X AKPRES.png', width=300)

st.markdown('-------------') 
st.write("Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59 ini bertujuan untuk memberikan pemahaman yang lebih baik tentang pencapaian akademik dan non-akademik mahasiswa PKU IPB, serta mengapresiasi prestasi yang telah mereka raih. Dengan adanya dashboard ini, diharapkan dapat memberikan informasi terkait perkembangan prestasi mahasiswa, sehingga dapat memberikan motivasi dan inspirasi dalam mengejar prestasi lebih baik.")
#=============================== Skala Lomba ===========================================
st.markdown('-------------')   
st.subheader('Ketentuan Penilaian Program Kerja')
st.markdown("(1) Perbandingan proporsi penilaian indikator kinerja panitia sebesar 50%, tujuan sebesar 20%, dan manfaat sebesar 30%.")
st.markdown("(2) Persentase penilaian program kerja berasal dari penjumlahan nilai kinerja panitia, tujuan, dan manfaat.")
st.markdown("(3) Penilaian kinerja departemen berasal dari penjumlahan nilai total program kerja kemudian dibagi dengan jumlah total program kerja tiap biro dan departemen.")
st.markdown("(4) Penilaian kinerja organisasi berasal dari penjumlahan nilai total kinerja departemen dibagi dengan jumlah total departemen organisasi.")
st.markdown("(5) Kinerja organisasi diterima jika minimal nilai total kinerja organisasi sebesar 75% dengan mempertimbangkan kesesuaian landasan peraturan yang berlaku.")
#=============================== Skala Lomba ===========================================
st.markdown('-------------')
st.subheader('Metriks Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')
col1, col2, col3= st.columns(3)
with col1:
            st.image('LOGOEKSE1.png', width=400)
with col2:
        # Tampilkan informasi nilai mutu
            st.image('85.png', width=400)
with col3:
        # Tampilkan informasi nilai mutu
            st.image('144.png', width=400)

st.markdown('-------------')
st.subheader('Metriks Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')
col1, col2, col3= st.columns([1,1,1])
with col1:
    st.metric("Kinerja Panitia", 27)
with col2:
    st.metric("Manfaat", 2)
with col3:
    st.metric("Tujuan", 20)

st.markdown('-------------')
#=============================== Jenis Prestasi ===========================================
st.subheader('Bar Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

left_column, Right_Column = st.columns([4,4])
left_column.plotly_chart(fig1, use_container_width=True)
Right_Column.plotly_chart(fig1,use_container_width=True)

st.markdown('-------------')
#=============================== Jenis Prestasi ===========================================
st.subheader('Bar Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

left_column, Right_Column = st.columns([4,4])
left_column.plotly_chart(fig1, use_container_width=True)
Right_Column.plotly_chart(fig1,use_container_width=True)
#=============================== Data Foto ===========================================



