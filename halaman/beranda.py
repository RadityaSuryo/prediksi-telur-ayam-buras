"""
halaman/beranda.py
Halaman utama: input interaktif jumlah tahun prediksi,
grafik tren + prediksi, dan tabel hasil prediksi.
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from utilitas import (
    muat_model, muat_data, judul_bagian,
    WARNA_TEKS, WARNA_AKSEN_HIJAU, WARNA_AKSEN_TELUR, WARNA_DASAR, WARNA_GARIS
)


def tampilkan():
    st.markdown("<h1>🥚 Prediksi Produksi Telur Ayam Buras</h1>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subjudul'>Provinsi Jawa Barat &middot; Dibangun dengan model ARIMA</div>",
        unsafe_allow_html=True
    )

    model = muat_model()
    df = muat_data()
    tahun = df['tahun'].tolist()
    data = df['total_produksi'].tolist()

    n_prediksi = 3  # jumlah tahun prediksi tetap

    # ===== Hitung prediksi beserta interval kepercayaan =====
    hasil_forecast = model.get_forecast(steps=n_prediksi)
    hasil_prediksi = hasil_forecast.predicted_mean
    conf_int = hasil_forecast.conf_int(alpha=0.05)

    tahun_prediksi = [max(tahun) + i for i in range(1, n_prediksi + 1)]

    try:
        batas_bawah = conf_int[:, 0]
        batas_atas = conf_int[:, 1]
    except (IndexError, TypeError):
        batas_bawah = conf_int.iloc[:, 0].values
        batas_atas = conf_int.iloc[:, 1].values

    # ===== Grafik =====
    judul_bagian("Grafik Tren & Prediksi")

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.patch.set_facecolor(WARNA_DASAR)
    ax.set_facecolor("#FFFBF2")

    ax.plot(tahun, data, marker='o', color=WARNA_TEKS, linewidth=2.2, label='Data Aktual', markersize=5)
    ax.plot(tahun_prediksi, hasil_prediksi, marker='^', color=WARNA_AKSEN_HIJAU, linewidth=2.2,
            linestyle='--', label=f'Prediksi {n_prediksi} Tahun', markersize=7)
    ax.fill_between(tahun_prediksi, batas_bawah, batas_atas, color=WARNA_AKSEN_HIJAU, alpha=0.15,
                     label='Interval Kepercayaan 95%')
    ax.axvline(x=max(tahun), color=WARNA_AKSEN_TELUR, linestyle=':', alpha=0.8, linewidth=1.5,
               label='Batas Data Aktual')

    ax.set_xlabel('Tahun', color=WARNA_TEKS, fontsize=10)
    ax.set_ylabel('Produksi (ton)', color=WARNA_TEKS, fontsize=10)
    ax.set_title('Tren Produksi & Prediksi — Telur Ayam Buras Jawa Barat',
                 color=WARNA_TEKS, fontsize=13, fontweight='bold', pad=14)
    ax.tick_params(colors=WARNA_TEKS)
    for spine in ax.spines.values():
        spine.set_color(WARNA_GARIS)
    ax.legend(facecolor="#FFFBF2", edgecolor=WARNA_GARIS, labelcolor=WARNA_TEKS, fontsize=9)
    ax.grid(True, alpha=0.25, color=WARNA_GARIS)

    with st.container(border=True):
        st.pyplot(fig)

    # ===== Tabel hasil prediksi =====
    judul_bagian("Rincian Angka Prediksi")

    df_prediksi = pd.DataFrame({
        'Tahun': tahun_prediksi,
        'Prediksi Produksi (ton)': [round(x, 2) for x in hasil_prediksi],
        'Batas Bawah (95%)': [round(x, 2) for x in batas_bawah],
        'Batas Atas (95%)': [round(x, 2) for x in batas_atas]
    })

    with st.container(border=True):
        st.dataframe(df_prediksi, use_container_width=True, hide_index=True)

    st.markdown(
        "<p class='footer-kecil'>Dikembangkan sebagai bagian dari Penulisan Ilmiah &middot; "
        "Model ARIMA &middot; Data Open Data Jabar 2013–2025</p>",
        unsafe_allow_html=True
    )
