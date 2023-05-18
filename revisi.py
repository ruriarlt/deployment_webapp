import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code !=200:
            return none
        return r.json()
    

# navigasi
with st.sidebar :
    
    from PIL import Image
    
    image = Image.open('clickclock.jpeg')
    st.image(image, caption='')
    print (image.width, image.height, image.format, type(image))
    image.show ()
    selected = option_menu('clickclock',
                           ['HOME',
                            'DEFINISI',
                            'PERHITUNGAN'],
       icons = ['house', 'book', 'calculator'], 
                           menu_icon='cast', default_index=1)
    
# pengertian
if (selected == 'HOME') :
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg?w=2000");
    background-size: cover;
    }
    
    [data-testid=stHeader"] {
    background-color: rgba(0,0,0,0);
    }
    </style>
    """
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    from PIL import Image
    st.header(':red[welcome, my dear! :wave:]')
    st.markdown('''Here We Are Presented, Our Webapps''')
    
    st.markdown('<h1 style="text-align: center; color: black;">WEB APLIKASI PERHITUNGAN KONSENTRASI TERUKUR, KADAR, DAN %RSD<h1>',unsafe_allow_html=True)
    lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_i9mtrven.json")
    st_lottie(lottie_hello, key="hello")
    
    st.markdown("<h2 style='text-align: center; color: black;'>Pembuatan aplikasi web ini bertujuan untuk mempermudah perhitungan dalam mata kuliah spektrofotometri dengan persamaan regresi yang telah diketahui</h2>", unsafe_allow_html=True)
    st.markdown('''Kelompok 5:
1. Amanda Berliana Widjaya (2260005)
2. Fifi Nuraini (2260016)
3. Marlina Cahyani (2260027)
4. Putri Nuraini (2260038)
5. Ruri Dwi Arlita (2260049)
6. Afdatul Saputra (2120377)''')
    
# halaman definisi
if (selected == 'DEFINISI') :
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg?w=2000");
    background-size: cover;
    }
    
    [data-testid=stHeader"] {
    background-color: rgba(0,0,0,0);
    }
    </style>
    """
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.header(':books: Berikut definisi-definisi yang diambil dari sumber terpercaya :books:')
    from PIL import Image
    image = Image.open('definisi.jpg')
    st.image(image, caption='')
    
# hitung %RSD
if (selected == 'PERHITUNGAN') :
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://img.freepik.com/free-vector/hand-painted-watercolor-pastel-sky-background_23-2148902771.jpg?w=2000");
    background-size: cover;
    }
    
    [data-testid=stHeader"] {
    background-color: rgba(0,0,0,0);
    }
    </style>
    """
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title('KALKULATOR PERHITUNGAN')
    st.header(':red[SELAMAT MENGAKSES :sunglasses:]')
    
    from PIL import Image
    image = Image.open('RUMUS_STER.png')
    st.image(image, caption='')
    absorbansi = st.number_input ("Masukkan Absorbansi", format="%.4f")
    intersep = st.number_input ("Masukkan Nilai Intercep", format="%.4f")
    slope = st.number_input ("Masukkan Nilai Slope", format="%.4f")
    vlt = st.number_input ("Masukkan Nilai Volume Labu Takar", format="%.0f")
    fp = st.number_input ("Masukkan Nilai fp", format="%.0f")
    sampel = st.number_input ("Masukkan Nilai Volume atau Bobot sampel (berupa nilai dalam KG ataupun L", format="%.8f")
    hitung = st.button('Hitung')
    
    if hitung :
        konsentrasi_terukur = (absorbansi - intersep) / slope
        st.success (f"nilai konsentrasi terukur adalah = {konsentrasi_terukur} mg/L ")
        kadar = (konsentrasi_terukur*vlt*fp) / sampel
        st.write('satuan yang dapat berupa mg/L atau mg/kg') 
        st.success (f"nilai konsentrasi terukur adalah = {kadar} ")
    
    from PIL import Image
    image = Image.open('RUMUS_RSD.png')
    st.image(image, caption='')
    nilai_total_kadar = st.number_input ("masukkan nilai total kadar", format="%.4f")
    banyak_jumlah_kadar = st.number_input ("masukkan banyak data kadar", format="%.0f")
    hitung = st.button('Hitung Nilai %RSD')
    
    if hitung :
        RSD = ((nilai_total_kadar**1/2)/(nilai_total_kadar/banyak_jumlah_kadar))
        st.write ("nilai %RSD adalah = ")
        st.success (f"nilai %RSD adalah = {RSD} %")
        if RSD<5:
            RSD=st.write('Tingkat akurasi sudah tercapai <5% dan baik')
        elif RSD>5:
            RSD=st.write('Tingkat akurasi tidak tercapai >5% dan kurang baik')