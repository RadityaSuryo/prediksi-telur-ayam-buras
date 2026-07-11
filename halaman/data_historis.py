"""
halaman/data_historis.py
Halaman tabel dan grafik data historis mentah (sebelum prediksi).
"""

import streamlit as st
import matplotlib.pyplot as plt

from utilitas import muat_data, judul_bagian, WARNA_TEKS, WARNA_DASAR, WARNA_GARIS


def tampilkan():
    st.markdown("<h1>📊 Data Historis</h1>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subjudul'>Produksi telur ayam buras Jawa Barat, 2013–2025</div>",
        unsafe_allow_html=True
    )

    df = muat_data()
    tahun = df['tahun'].tolist()
    data = df['total_produksi'].tolist()

    judul_bagian("Grafik Tren Historis")
    fig, ax = plt.subplots(figsize=(10, 4.5))
    fig.patch.set_facecolor(WARNA_DASAR)
    ax.set_facecolor("#FFFBF2")

    ax.plot(tahun, data, marker='o', color=WARNA_TEKS, linewidth=2.2, markersize=5)
    ax.set_xlabel('Tahun', color=WARNA_TEKS, fontsize=10)
    ax.set_ylabel('Produksi (ton)', color=WARNA_TEKS, fontsize=10)
    ax.set_title('Total Produksi Telur Ayam Buras — Jawa Barat',
                 color=WARNA_TEKS, fontsize=13, fontweight='bold', pad=14)
    ax.tick_params(colors=WARNA_TEKS)
    for spine in ax.spines.values():
        spine.set_color(WARNA_GARIS)
    ax.grid(True, alpha=0.25, color=WARNA_GARIS)

    with st.container(border=True):
        st.pyplot(fig)

    judul_bagian("Tabel Data Lengkap")
    with st.container(border=True):
        st.dataframe(df, use_container_width=True, hide_index=True)

    st.caption("Sumber data: Open Data Jabar, diagregasi tahunan dari 27 kabupaten/kota.")