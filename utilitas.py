"""
utilitas.py
Fungsi bersama yang dipakai di beberapa halaman:
load model, load data, dan konstanta warna tema.
"""

import joblib
import pandas as pd
import streamlit as st

# ===== Palet warna tema (dipakai juga di grafik matplotlib) =====
WARNA_TEKS = "#3D2B1F"
WARNA_AKSEN_HIJAU = "#6B7A4F"
WARNA_AKSEN_TELUR = "#D98E3F"
WARNA_DASAR = "#F5EFE3"
WARNA_GARIS = "#DCD2BC"


@st.cache_resource
def muat_model():
    """Load model ARIMA yang sudah dilatih. Di-cache supaya tidak reload setiap interaksi."""
    return joblib.load('model_arima.pkl')


@st.cache_data
def muat_data():
    """Load data historis produksi telur. Di-cache supaya tidak baca ulang file setiap interaksi."""
    df = pd.read_csv('data_siap_ARIMA.csv')
    return df


def muat_css(path_file="style.css"):
    """Suntikkan file CSS eksternal ke halaman."""
    with open(path_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def judul_bagian(label):
    """Tampilkan pemisah bertema oval telur sebagai judul bagian."""
    st.markdown(
        f"<div class='pemisah-telur'><div class='oval'></div>"
        f"<div class='label'>{label}</div></div>",
        unsafe_allow_html=True
    )