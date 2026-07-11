"""
proteksi.py
Modul deterrent sederhana untuk mempersulit klik kanan, seleksi teks,
dan tombol download bawaan Streamlit pada tabel/grafik.

CATATAN PENTING:
Ini HANYA deterrent (mempersulit), BUKAN pencegahan keamanan yang absolut.
Screenshot, Developer Tools (F12), dan cara teknis lain tetap bisa melewati ini.
"""

import streamlit as st


def aktifkan_proteksi_tampilan():
    """
    Menyuntikkan CSS + JavaScript untuk:
    1. Menonaktifkan klik kanan (mencegah menu 'Save image as' / 'Inspect' lewat klik kanan biasa)
    2. Menonaktifkan seleksi/copy teks (mencegah drag-select pada tabel)
    3. Menyembunyikan tombol download bawaan Streamlit pada tabel & grafik
    """
    st.markdown("""
    <style>
    /* 2. Nonaktifkan seleksi teks di seluruh halaman */
    .stApp {
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    /* 3. Sembunyikan tombol download/toolbar bawaan pada dataframe & grafik */
    div[data-testid="stElementToolbar"] {
        display: none !important;
    }
    </style>

    <script>
    // 1. Nonaktifkan klik kanan (context menu)
    document.addEventListener('contextmenu', function(e) {
        e.preventDefault();
    });

    // Cegah shortcut umum untuk save/inspect/view-source
    document.addEventListener('keydown', function(e) {
        // Ctrl+S (save), Ctrl+U (view source), F12 (devtools)
        if ((e.ctrlKey && (e.key === 's' || e.key === 'S' || e.key === 'u' || e.key === 'U')) || e.key === 'F12') {
            e.preventDefault();
        }
    });
    </script>
    """, unsafe_allow_html=True)