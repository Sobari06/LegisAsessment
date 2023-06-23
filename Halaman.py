def halaman_BirdeptVers1(Logo,nama_birdept, programkerja,total_program_kerja,Kinerja_Panitia,Manfaat, Tujuan,Bar1,Bar2,Bar3,Bar4,Bar5,Bar6,Bar7,Bar8,Bar9,Bar10,Bar11,Bar12,Bar13,Bar14,Bar15):
    import streamlit as st
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
            st.image(Logo, width=400)

    st.markdown('-------------')
    st.subheader('Metriks Hasil Penilaian Kinerja '+ nama_birdept +' Ormawa Eksekutif PKU IPB')
    st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.metric("Program Kerja", programkerja)
    with col2:
        st.metric("Total Program Kerja", total_program_kerja)
    with col3:
        st.metric("Kinerja Panitia", Kinerja_Panitia)
    with col4:
        st.metric("Manfaat", Manfaat)
    with col5:
        st.metric("Tujuan", Tujuan)

    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Dari Semua Aspek')
    col3, col4, col5 = st.columns([1,7,1])
    col4.plotly_chart(Bar4,use_container_width=True)

    st.title('Rincian Hasil Penilaian 15 Aspek Kinerja Panitia')
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Berdasarkan Aspek A,B,C,D,E')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    left_column, Right_Column, col3, col4, col5 = st.columns(5)
    left_column.plotly_chart(Bar1, use_container_width=True)
    Right_Column.plotly_chart(Bar2,use_container_width=True)
    col3.plotly_chart(Bar3,use_container_width=True)
    col4.plotly_chart(Bar4,use_container_width=True)
    col5.plotly_chart(Bar5,use_container_width=True)
    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Berdasarkan Aspek A,B,C,D,E')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    left_column, Right_Column, col3, col4, col5 = st.columns(5)
    left_column.plotly_chart(Bar6, use_container_width=True)
    Right_Column.plotly_chart(Bar8,use_container_width=True)
    col3.plotly_chart(Bar9,use_container_width=True)
    col4.plotly_chart(Bar10,use_container_width=True)
    col5.plotly_chart(Bar11,use_container_width=True)
    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Berdasarkan Aspek A,B,C,D,E')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    left_column, Right_Column, col3, col4, col5 = st.columns(5)
    left_column.plotly_chart(Bar12, use_container_width=True)
    Right_Column.plotly_chart(Bar13,use_container_width=True)
    col3.plotly_chart(Bar14,use_container_width=True)
    col4.plotly_chart(Bar15,use_container_width=True)
    col5.plotly_chart(Bar7,use_container_width=True)

def halaman_BirdeptVers2(Logo,nama_birdept, programkerja,total_program_kerja,Kinerja_Panitia,Manfaat, Tujuan):
    import streamlit as st
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
            st.image(Logo, width=400)

    st.markdown('-------------')
    st.subheader('Metriks Hasil Penilaian Kinerja '+ nama_birdept +' Ormawa Eksekutif PKU IPB')
    st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.metric("Program Kerja", programkerja)
    with col2:
        st.metric("Total Program Kerja", total_program_kerja)
    with col3:
        st.metric("Kinerja Panitia", Kinerja_Panitia)
    with col4:
        st.metric("Manfaat", Manfaat)
    with col5:
        st.metric("Tujuan", Tujuan)

    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Berdasarkan Aspek A,B,C,D,E')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
            st.metric("Program Kerja", programkerja)
    with col2:
            st.metric("Total Program Kerja", total_program_kerja)
    with col3:
            st.metric("Kinerja Panitia", Kinerja_Panitia)
    with col4:
            st.metric("Manfaat", Manfaat)
    with col5:
            st.metric("Tujuan", Tujuan)
    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Berdasarkan Aspek A,B,C,D,E')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.metric("Program Kerja", programkerja)
    with col2:
        st.metric("Total Program Kerja", total_program_kerja)
    with col3:
        st.metric("Kinerja Panitia", Kinerja_Panitia)
    with col4:
        st.metric("Manfaat", Manfaat)
    with col5:
        st.metric("Tujuan", Tujuan)
    st.markdown('-------------')
    #=============================== Jenis Prestasi ===========================================
    st.subheader('Bar Chart Terkait Akumulasi Jumlah Nilai Mutu Berdasarkan Aspek A,B,C,D,E')
    st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
            st.metric("Program Kerja", programkerja)
    with col2:
            st.metric("Total Program Kerja", total_program_kerja)
    with col3:
            st.metric("Kinerja Panitia", Kinerja_Panitia)
    with col4:
            st.metric("Manfaat", Manfaat)
    with col5:
            st.metric("Tujuan", Tujuan)