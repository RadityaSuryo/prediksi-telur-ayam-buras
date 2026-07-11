"""
app.py
Entry point aplikasi. Mengatur konfigurasi halaman, styling,
proteksi tampilan, dan navigasi sidebar antar halaman.
"""

import streamlit as st

from proteksi import aktifkan_proteksi_tampilan
from utilitas import muat_css
from halaman import beranda, tentang_model, data_historis

# ===== Konfigurasi halaman =====
st.set_page_config(
    page_title="Prediksi Produksi Telur Ayam Buras",
    page_icon="🥚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== Aktifkan styling & deterrent klik kanan/seleksi teks =====
muat_css("style.css")
aktifkan_proteksi_tampilan()

# ===== Definisi halaman untuk navigasi sidebar =====
halaman_beranda = st.Page(beranda.tampilkan, title="Beranda", icon="🥚", url_path="beranda", default=True)
halaman_tentang = st.Page(tentang_model.tampilkan, title="Tentang Model", icon="📖", url_path="tentang-model")
halaman_data = st.Page(data_historis.tampilkan, title="Data Historis", icon="📊", url_path="data-historis")

navigasi = st.navigation([halaman_beranda, halaman_tentang, halaman_data])
navigasi.run()