import streamlit as st
from streamlit_option_menu import option_menu

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Contoh Program", layout="centered")

# --- CSS KHUSUS MARKAS (TEMA EMAS-NAVY) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {{
        background-color: #0e1117;
        font-family: 'Montserrat', sans-serif;
        color: #ffffff;
    }}

    /* Kotak Profil */
    .profile-box {{
        text-align: center;
        padding: 20px;
        border-bottom: 2px solid #F2C94C;
        margin-bottom: 30px;
    }}

    /* Gaya Tombol Link */
    .stLinkButton > a {{
        background-color: #101820 !important;
        color: #F2C94C !important;
        border: 1px solid #F2C94C !important;
        border-radius: 12px !important;
        padding: 8px 20px !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        transition: 0.3s !important;
        width: 100% !important;
        display: block !important;
        text-align: center !important;
        text-decoration: none !important;
    }}

    .stLinkButton > a:hover {{
        background-color: #F2C94C !important;
        color: #101820 !important;
        box-shadow: 0px 0px 20px rgba(242, 201, 76, 0.4) !important;
        transform: translateY(-3px) !important;
    }}

    /* --- GAYA LACI (EXPANDER) --- */
    
    /* A. Bingkai Utama & Latar Belakang */
    [data-testid="stExpander"] details {{
        border: 1px solid #F2C94C !important;
        border-radius: 12px !important;
        background-color: #101820 !important;
        overflow: hidden !important;
        margin-bottom: 15px !important;
    }}

    /* B. Gagang Laci (Header) */
    [data-testid="stExpander"] summary {{
        background: transparent !important;
        padding: 10px 20px !important; /* Membuat gagang lebih tebal & lega */
        border-bottom: none !important;
    }}

    /* C. Teks Judul Laci */
    [data-testid="stExpander"] summary p {{
        color: #F2C94C !important;
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        letter-spacing: 1px !important;
    }}

    /* D. Ikon Panah (Chevron) */
    [data-testid="stExpander"] summary svg,
    [data-testid="stExpander"] summary [data-testid="stIconMaterial"] {{
        color: #F2C94C !important;
        fill: #F2C94C !important;
    }}

    /* E. Efek Menyala Saat Disorot Kursor */
    [data-testid="stExpander"] summary:hover {{
        background-color: rgba(242, 201, 76, 0.1) !important;
    }}
    
    /* F. Garis pembatas tipis saat laci terbuka */
    [data-testid="stExpander"] details[open] summary {{
        border-bottom: 1px solid rgba(242, 201, 76, 0.2) !important;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ISI HALAMAN ---
st.markdown("""
    <h1 style='color: #F2C94C; text-align: center; font-size: 42px; font-weight: 800;'>
        Contoh Program
    </h1>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- DAFTAR LINK PROGRAM ---

# Program 1: Resto Planner (Model Laci)
with st.expander("MANAJEMEN BAHAN BAKU", expanded=False):
    
    # 1. Penjelasan di dalam laci
    st.markdown("""
        <p style='color: #F2C94C; font-size: 14px; margin-top: 5px; margin-bottom: 15px;'>
            Sistem pintar untuk manajemen stok gudang, kalkulasi bahan baku resep, dan pencatatan produksi harian.
        </p>
    """, unsafe_allow_html=True)
    
    # 2. Tombol peluncuran di dalam laci
    st.link_button(
        "OPEN PROGRAM", 
        "https://kalkulasikebutuhanbahan-r5j7hr9ezh8gdpgiijchbg.streamlit.app",
        use_container_width=True
    )

with st.expander("REKOMENDASI WARNA OUTFIT", expanded=False):
    
    # 1. Penjelasan di dalam laci
    st.markdown("""
        <p style='color: #F2C94C; font-size: 14px; margin-top: 5px; margin-bottom: 15px;'>
            Program yang membantumu untuk memilih kombinasi warna pakaian yang cocok
        </p>
    """, unsafe_allow_html=True)
    
    # 2. Tombol peluncuran di dalam laci
    st.link_button(
        "OPEN PROGRAM", 
        "https://rekomendasiwarna-56k5ufhhzzratuvzrvxpv6.streamlit.app",
        use_container_width=True
    )



# --- FOOTER PREMIUM (DENGAN FONT AWESOME) ---
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<div style="text-align: center; margin-top: 50px; padding-top: 30px; border-top: 1px solid rgba(242, 201, 76, 0.3);">

<p style="color: #F2C94C; font-size: 12px; margin-bottom: 20px; opacity: 0.8;">
Building Smart Data & Web Solutions
</p>

<div style="margin-bottom: 20px;">
<a href="https://wa.me/6281357309862" target="_blank" style="text-decoration: none; margin: 0 15px; font-size: 26px; color: #ffffff; opacity: 0.4; transition: 0.3s;" onmouseover="this.style.color='#F2C94C'; this.style.opacity='1'" onmouseout="this.style.color='#ffffff'; this.style.opacity='0.4'">
<i class="fab fa-whatsapp"></i>
</a>

<a href="https://instagram.com/royhanalkarim1231" target="_blank" style="text-decoration: none; margin: 0 15px; font-size: 26px; color: #ffffff; opacity: 0.4; transition: 0.3s;" onmouseover="this.style.color='#F2C94C'; this.style.opacity='1'" onmouseout="this.style.color='#ffffff'; this.style.opacity='0.4'">
<i class="fab fa-instagram"></i>
</a>

<a href="mailto:email.riyhanalkarim123@gmail.com" style="text-decoration: none; margin: 0 15px; font-size: 26px; color: #ffffff; opacity: 0.4; transition: 0.3s;" onmouseover="this.style.color='#F2C94C'; this.style.opacity='1'" onmouseout="this.style.color='#ffffff'; this.style.opacity='0.4'">
<i class="fas fa-envelope"></i>
</a>
</div>

<p style="color: #F2C94C; font-size: 10px; letter-spacing: 1px; opacity: 0.6;">
© 2026 ALL RIGHTS RESERVED &nbsp; | &nbsp; R O Y SYSTEM v1.0.0
</p>
</div>
""", unsafe_allow_html=True)
