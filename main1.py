import streamlit as st
import pandas as pd
import plotly_express as px

from streamlit_lottie import st_lottie
import requests
import Halaman

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

figa= px.bar(
dfa, y= names,  x=values,
title= 'Kesuksesan Program Kerja')

figd= px.bar(
dfa, y= names,  x=values,
title= 'Aspek Kebermanfaatan')

figc= px.bar(
dfa, y= names,  x=values,
title= 'Aspek Tujuan')

fige= px.bar(
dfa, y= names,  x=values,
title= 'Aspek Kinerja Panitia')
print(type(dfa))
figa.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

figb= px.pie(dfa, values= values, 
names= names)



dfa= pd.read_excel(
    io='DataContohLegis.xlsx',
    engine='openpyxl',
    sheet_name='A1(6)',
    usecols='A:B')
names = dfa['Nama'].apply(str)
values = dfa['Nilai'].apply(int)

fig1= px.bar(
dfa, y= names,  x=values,
title= 'Kode Etik')

fig2= px.bar(
dfa, y= names,  x=values,
title= 'Konsistensi')

fig3= px.bar(
dfa, y= names,  x=values,
title= 'Jumlah Peserta')

fig4= px.bar(
dfa, y= names,  x=values,
title= 'Keanggotaan')

fig5= px.bar(
dfa, y= names,  x=values,
title= 'Presensi Rapat Kerja')

fig6= px.bar(
dfa, y= names,  x=values,
title= 'Progress Report')

fig7= px.bar(
dfa, y= names,  x=values,
title= 'Press Release')

fig8= px.bar(
dfa, y= names,  x=values,
title= 'Pencapaian Target Dana Non-RKAPK')

fig9= px.bar(
dfa, y= names,  x=values,
title= 'Saldo Dana')

fig10= px.bar(
dfa, y= names,  x=values,
title= 'Kelancaran Acara')

fig11= px.bar(
dfa, y= names,  x=values,
title= 'kesesuaian LPJ')

fig12= px.bar(
dfa, y= names,  x=values,
title= 'Kesesuaian Waktu Acara')

fig13= px.bar(
dfa, y= names,  x=values,
title= 'Kesesuaian Proposal Kegiatan')

fig14= px.bar(
dfa, y= names,  x=values,
title= 'Penyerahan proposal kegiatan')

fig15= px.bar(
dfa, y= names,  x=values,
title= 'Penyerahan LPJ kegiatan ')




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
            st.title('Dashboard Kinerja Ormawa Eksekutif oleh Ormawa Legislatif PKU IPB')
            st.subheader("Ormawa Eksekutif PKU IPB Kabinet Gantari Arti")   
with col2:
        # Tampilkan informasi nilai mutu
             st.image('RISBANG X AKPRES.png', width=300)

st.markdown('-------------') 
st.write("Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59 ini bertujuan untuk memberikan pemahaman yang lebih baik tentang pencapaian akademik dan non-akademik mahasiswa PKU IPB, serta mengapresiasi prestasi yang telah mereka raih. Dengan adanya dashboard ini, diharapkan dapat memberikan informasi terkait perkembangan prestasi mahasiswa, sehingga dapat memberikan motivasi dan inspirasi dalam mengejar prestasi lebih baik.")
#=============================== Skala Lomba ===========================================

#=============================== Skala Lomba ===========================================
menu = ['Kabinet Gantari Arti', 'Biro Riset Pengembangan', 'Biro Internal', 'Departemen Pengembangan Sumberdaya Mahasiswa','Departemen Advokasi Kesejahteraan Mahasiswa', 'Departemen Akademik Prestasi','Biro Media Branding', 'Biro Bisnis Kemitraan','Departemen Pemuda Olahraga', 'Departemen Sosial Lingkungan Hidup', 'Departemen Kajian Aksi Strategis']
choice = st.sidebar.selectbox('Menu', menu)
if choice == "Kabinet Gantari Arti":
    st.markdown('-------------')   
    col1, col2= st.columns(2)
    with col1:
            st.subheader('Ketentuan Penilaian Program Kerja')
            st.markdown("(1) Perbandingan proporsi penilaian indikator kinerja panitia sebesar 50%, tujuan sebesar 20%, dan manfaat sebesar 30%.")
            st.markdown("(2) Persentase penilaian program kerja berasal dari penjumlahan nilai kinerja panitia, tujuan, dan manfaat.")
            st.markdown("(3) Penilaian kinerja departemen berasal dari penjumlahan nilai total program kerja kemudian dibagi dengan jumlah total program kerja tiap biro dan departemen.")
            st.markdown("(4) Penilaian kinerja organisasi berasal dari penjumlahan nilai total kinerja departemen dibagi dengan jumlah total departemen organisasi.")
            st.markdown("(5) Kinerja organisasi diterima jika minimal nilai total kinerja organisasi sebesar 75% dengan mempertimbangkan kesesuaian landasan peraturan yang berlaku.")



            # Mendefinisikan path file PDF
            pdf_file_path = "Peraturan 005 tentang SPPK.pdf"

            # Membaca file PDF dalam bentuk byte array
            with open(pdf_file_path, "rb") as file:
                pdf_contents = file.read()

            # Membuat tombol download menggunakan st.download
            st.download_button('Download Peraturan tentang SPPK (Standar Penilaian Program Kerja).PDF', data=pdf_contents, file_name='Peraturan 005 tentang SPPK.pdf')

    with col2:
            st.image('LOGOEKSE1.png', width=400)
      

    st.markdown('-------------')
    st.subheader('Metriks Hasil Penilaian Kinerja Ormawa Eksekutif PKU IPB')
    st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.metric("Program Kerja", 85)
    with col2:
        st.metric("Total Program Kerja", 185)
    with col3:
        st.metric("Kinerja Panitia", 95)
    with col4:
        st.metric("Manfaat", 85)
    with col5:
        st.metric("Tujuan", 65)

    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Pie Chart Terkait Proporsi Jumlah Proker dan Bar Chart Terkait Perbandingan Hasil Penilaian Program Kerja Antar Birdept.')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    left_column, Right_Column = st.columns([4,4])
    left_column.plotly_chart(figb, use_container_width=True)
    Right_Column.plotly_chart(figa,use_container_width=True)

    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Perbandingan Hasil Penilaian Aspek Kebermanfaatan dan Tujuan Antar Birdept')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    left_column, Right_Column = st.columns([4,4])
    left_column.plotly_chart(figc, use_container_width=True)
    Right_Column.plotly_chart(figd,use_container_width=True)
    #=============================== Data Foto ===========================================
    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Perbandingan Hasil Penilaian Aspek Kebermanfaatan dan Tujuan Antar Birdept')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    left_column, Right_Column = st.columns([4,4])
    left_column.plotly_chart(fige, use_container_width=True)
    Right_Column.plotly_chart(fig1,use_container_width=True)
if choice == "Biro Riset Pengembangan":
    Halaman.halaman_BirdeptVers1(nama_birdept="Biro Riset Pengembangan",
                    Logo="RISBANG.png",
                    programkerja=50, 
                    total_program_kerja=40,
                    Kinerja_Panitia=78, 
                    Manfaat=85,
                    Tujuan=90,
                    Bar1=fig1,  Bar2=fig6,   Bar4=fig11,
                    Bar3=fig2,  Bar5=fig7,   Bar6=fig12,
                    Bar7=fig3,  Bar8=fig8,   Bar9=fig13,
                    Bar10=fig4, Bar11=fig9,  Bar12=fig14,
                    Bar13=fig5, Bar14=fig10,  Bar15=fig15
                    )
    
    # Halaman.halaman_BirdeptVers2(nama_birdept="Biro Riset Pengembangan",
    #                 Logo="RISBANG.png",
    #                 programkerja=50, 
    #                 total_program_kerja=40,
    #                 Kinerja_Panitia=78, 
    #                 Manfaat=85,
    #                 Tujuan=90
    #                 )
    
