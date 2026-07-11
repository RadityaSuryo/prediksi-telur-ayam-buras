"""
halaman/tentang_model.py
Halaman penjelasan metodologi: ARIMA, CRISP-DM, dan metrik evaluasi.
"""

import streamlit as st
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

from utilitas import muat_model, muat_data, judul_bagian


def tampilkan():
    st.markdown("<h1>📖 Tentang Model</h1>", unsafe_allow_html=True)
    st.markdown(
        "<div class='subjudul'>Metodologi di balik prediksi ini</div>",
        unsafe_allow_html=True
    )

    model = muat_model()
    df = muat_data()
    data = df['total_produksi'].tolist()

    judul_bagian("Kerangka Kerja CRISP-DM")
    with st.container(border=True):
        st.markdown("""
        Penelitian ini menggunakan kerangka kerja **CRISP-DM** (*Cross-Industry Standard
        Process for Data Mining*), yang terdiri dari beberapa tahap berurutan:

        1. **Business Understanding** — memahami kebutuhan prediksi produksi telur ayam buras
        2. **Data Understanding** — eksplorasi data dari Open Data Jabar (2013–2025)
        3. **Data Preparation** — pembersihan dan agregasi data ke total tahunan Jawa Barat
        4. **Modeling** — pelatihan model ARIMA dengan iterasi manual 27 kombinasi (p,d,q)
        5. **Evaluation** — pengujian validitas model lewat Walk-Forward Validation
        6. **Deployment** — penerapan model ke aplikasi web ini
        """)

    judul_bagian("Mengapa ARIMA?")
    with st.container(border=True):
        st.markdown("""
        **ARIMA** (*AutoRegressive Integrated Moving Average*) dipilih karena cocok untuk
        data time series dengan jumlah observasi terbatas (13 titik data tahunan), tanpa
        memerlukan variabel eksternal tambahan seperti pendekatan ARIMAX. Model ini juga
        lebih mudah diinterpretasikan dibandingkan pendekatan deep learning.

        Pemilihan kombinasi parameter (p, d, q) dilakukan secara **manual** dengan menguji
        27 kombinasi (masing-masing bernilai 0, 1, atau 2), dibandingkan berdasarkan nilai
        AIC dan BIC terkecil.
        """)

    judul_bagian("Metrik Evaluasi Model")

    prediksi_insample = model.fittedvalues
    mae = mean_absolute_error(data, prediksi_insample)
    rmse = np.sqrt(mean_squared_error(data, prediksi_insample))

    with st.container(border=True):
        kolom1, kolom2 = st.columns(2)
        with kolom1:
            st.metric("MAE (Mean Absolute Error)", f"{mae:,.2f} ton")
        with kolom2:
            st.metric("RMSE (Root Mean Squared Error)", f"{rmse:,.2f} ton")

        st.caption(
            "MAE menunjukkan rata-rata selisih absolut antara nilai aktual dan prediksi. "
            "RMSE memberi bobot lebih besar pada selisih yang besar, sehingga lebih sensitif "
            "terhadap outlier dibandingkan MAE."
        )

    judul_bagian("Batasan Model")
    with st.container(border=True):
        st.markdown("""
        - Model dilatih dari data tahunan agregat Jawa Barat (2013–2025), bukan per kabupaten/kota
        - Prediksi pada web ini dibatasi maksimal 5 tahun ke depan, mengikuti horizon yang
          diuji pada tahap Walk-Forward Validation (periode pengujian 2021–2025)
        - Model tidak memperhitungkan faktor eksternal seperti wabah penyakit, kebijakan
          pemerintah, atau perubahan harga pakan
        """)