import streamlit as st
from PIL import Image
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Konfigurasi halaman
st.set_page_config(page_title="Food Freshness App", page_icon="🍎", layout="wide")

# Palet Warna
PRIMARY_COLOR = "#4CAF50"
SECONDARY_COLOR = "#F44336"
BACKGROUND_COLOR = "#E3F2FD"  # Biru muda
TEXT_COLOR = "#333333"
ACCENT_COLOR = "#FFC107"

# CSS Kustom
st.markdown(f"""
    <style>
    .main {{
        background-color: {BACKGROUND_COLOR} !important;
        color: {TEXT_COLOR};
        font-family: 'Poppins', sans-serif;
    }}
    .stApp {{
        background-color: {BACKGROUND_COLOR} !important;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }}
    .stButton>button:hover {{
        background-color: {SECONDARY_COLOR};
        transform: scale(1.05);
    }}
    .sidebar .sidebar-content {{
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }}
    h1, h2, h3 {{
        color: {PRIMARY_COLOR};
    }}
    .title {{
        font-size: 36px;
        font-weight: bold;
        color: {PRIMARY_COLOR};
    }}
    .subtitle {{
        font-size: 24px;
        color: {TEXT_COLOR};
        margin-bottom: 20px;
    }}
    .image-container {{
        text-align: center;
        margin: 20px 0;
    }}
    </style>
""", unsafe_allow_html=True)

# --- Efek Animasi Balon dan Salju ---
def animation_effect():
    st.balloons()
    for _ in range(3):
        st.markdown('<div class="snowflake">❄️</div>', unsafe_allow_html=True)

# --- Navigasi Sidebar ---
menu = st.sidebar.selectbox("📂 Menu", ["🏠 Beranda", "🧮 Penilaian Kelayakan Makanan", "ℹ️ Info"])

# --- Beranda ---
if menu == "🏠 Beranda":
    st.title("🍎 FRESH CHECK - Pendeteksi Kelayakan Konsumsi Makanan")

    # Gambar lebih menarik mencakup semua kategori makanan
    st.image("https://www.ybkb.or.id/wp-content/uploads/2024/03/shopping-bag-full-fresh-fruits-vegetables-with-assorted-ingredients-min-825x551_yUwnK.jpg", width=700)

    # Deskripsi aplikasi dengan ikon dan bullet point yang lebih menarik
    st.markdown("""
    ### 🌟 Selamat Datang di **Pendeteksi Kelayakan Konsumsi Makanan**!  
    Aplikasi ini dirancang untuk membantu Anda mengonsumsi makanan yang **sehat** dan **aman** dengan fitur menarik berikut:

    - 📅 **Pengecekan Tanggal Kedaluwarsa**: Pantau masa simpan makanan agar tetap aman.  
    """)

    # Catatan di bagian bawah
    st.markdown("---")
    st.info("💡 **Tips:** Jaga kesehatan dengan memilih makanan bergizi dan mengolahnya dengan cara yang tepat!")

# --- Penilaian Kelayakan Makanan ---
if menu == "🧮 Penilaian Kelayakan Makanan":
    st.title("🔍 Penilaian Kelayakan Makanan")

    # Pilih jenis makanan utama
    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", ["Sayuran 🥦", "Buah-buahan 🍎", "Daging 🍖"])

    # Menampilkan pilihan bahan makanan berdasarkan kategori yang dipilih
    if jenis_makanan == "Buah-buahan 🍎":
        bahan_makanan = st.selectbox("🍏 Pilih Buah", ["Anggur", "Mangga", "Kiwi", "Nanas", "Alpukat", "Pisang", "Jeruk", "Melon", "Semangka", "Strawberry", "Buah Potong", "Pepaya"])
    elif jenis_makanan == "Sayuran 🥦":
        bahan_makanan = st.selectbox("🥦 Pilih Sayuran", ["Kubis", "Wortel", "Kembang Kol", "Selada", "Jamur", "Bayam", "Kentang", "Mentimun", "Terong", "Jagung"])
    elif jenis_makanan == "Daging 🍖":
        bahan_makanan = st.selectbox("🍖 Pilih Daging", ["Daging Sapi", "Daging Ayam", "Ikan"])

    # Menampilkan pilihan yang dipilih
    st.write(f"Anda memilih: {bahan_makanan}")

    # Input tanggal pembelian
    tanggal_input = st.date_input("📅 Tanggal Pembelian")

    # Pilih kondisi penyimpanan
    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", ["Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"])

    # Pilih perubahan fisik
    perubahan_fisik = st.multiselect("⚠️ Perubahan Fisik", ["Perubahan warna 🎨", "Bau tidak sedap 🤢", "Tekstur berlendir 🦠"])

    # Cek kelayakan
    if st.button("🔎 Cek Kelayakan"):
        animation_effect()
        hari_ini = datetime.now().date()
        lama_simpan = (hari_ini - tanggal_input).days

        if tanggal_input > hari_ini:
            st.error("❗ Tanggal yang Anda masukkan tidak valid. Silakan masukkan tanggal yang logis.")
        else:
            # Menangani kelayakan berdasarkan perubahan fisik dan lama simpan
            if perubahan_fisik:
                if jenis_makanan == "Buah-buahan 🍎":
                    if bahan_makanan == "Pisang":
                        st.warning("🍌 Pisang yang muncul titik coklat masih layak dimakan, namun rasanya lebih manis. Jika kulit menghitam, bisa jadi sudah sangat matang.")
                    elif bahan_makanan == "Mangga":
                        st.warning("🥭 Mangga yang berubah warna dari hijau ke kuning/oranye adalah tanda kematangan dan tetap layak dikonsumsi.")
                    elif bahan_makanan == "Pepaya":
                        st.warning("🍈 Pepaya yang mengubah warna dari hijau ke oranye menandakan kematangan, namun jika sangat lembek bisa mulai rusak.")
                    elif bahan_makanan == "Jeruk":
                        st.warning("🍊 Jeruk dengan kulit keriput masih bisa dimakan, tapi teksturnya sudah berkurang.")
                    elif bahan_makanan == "Semangka":
                        st.warning("🍉 Semangka yang mulai lembek atau berair menandakan kerusakan, lebih baik tidak dimakan.")
                
                elif jenis_makanan == "Sayuran 🥦":
                    if bahan_makanan == "Kubis":
                        st.warning("🥬 Kubis yang lembek atau layu menunjukkan kehilangan kesegaran. Jika berlendir, sebaiknya dibuang.")
                    elif bahan_makanan == "Wortel":
                        st.warning("🥕 Wortel yang keriput masih bisa dimakan, tetapi rasanya kurang segar.")
                    elif bahan_makanan == "Kembang Kol":
                        st.warning("🌸 Kembang kol yang menguning atau terlalu lembek menandakan kerusakan.")
                    elif bahan_makanan == "Selada":
                        st.warning("🥗 Selada yang layu atau kering masih bisa dimakan, tetapi kualitasnya berkurang.")
                    elif bahan_makanan == "Jamur":
                        st.warning("🍄 Jamur yang berlendir atau berair sudah mulai rusak dan sebaiknya tidak dimakan.")
                
                elif jenis_makanan == "Daging 🍖":
                    if bahan_makanan == "Daging Sapi":
                        st.warning("🥩 Daging sapi yang berwarna kecoklatan atau berlendir bisa menunjukkan mulai rusak. Pastikan tidak berbau busuk.")
                    elif bahan_makanan == "Daging Ayam":
                        st.warning("🍗 Daging ayam yang berubah warna menjadi abu-abu atau berlendir bisa menunjukkan pembusukan.")
                    elif bahan_makanan == "Ikan":
                        st.warning("🐟 Ikan yang berbau tajam atau kulitnya berlendir menandakan bahwa ikan sudah tidak layak dimakan.")

            # --- Info ---
if menu == "ℹ️ Info":
    st.title("ℹ️ Informasi Pembuat Aplikasi")
    st.markdown("""
    **Aplikasi ini dikembangkan oleh:**

    - 👩‍💻 **Azzahra Sadrina Nadzifa (2350080)**
    - 👩‍💻 **Dhyza Aulia Shabirah (2350084)**
    - 👩‍💻 **Diyan Theda Mufarrihah (2350085)** 
    - 👩‍💻 **Haija Nafiah (2350094)**
    - 👨‍💻 **Irsan Abdurrahman (2350100)**

    Dibuat dengan ❤️ oleh Kelompok 10

    D-IV Nanoteknologi Pangan
    
    Politeknik AKA Bogor
    """)


# --- Footer ---
st.markdown("---")
st.caption("🥗 *Dirancang untuk mendukung gaya hidup sehat dan aman setiap hari.*")
   
