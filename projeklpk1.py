import streamlit as st
from PIL import Image
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Konfigurasi halaman
st.set_page_config(page_title="Food Freshness App", page_icon="🍎", layout="wide")

# Warna untuk mode terang dan gelap
LIGHT_BACKGROUND = "#E3F2FD"
DARK_BACKGROUND = "#121212"
LIGHT_TEXT_COLOR = "#333333"
DARK_TEXT_COLOR = "#FFFFFF"
PRIMARY_COLOR = "#4CAF50"
SECONDARY_COLOR = "#F44336"
ACCENT_COLOR = "#FFC107"

# CSS Kustom dengan deteksi mode terang/gelap
st.markdown(f"""
    <style>
    :root {{
        --light-background: {LIGHT_BACKGROUND};
        --dark-background: {DARK_BACKGROUND};
        --light-text: {LIGHT_TEXT_COLOR};
        --dark-text: {DARK_TEXT_COLOR};
        --primary-color: {PRIMARY_COLOR};
        --secondary-color: {SECONDARY_COLOR};
        --accent-color: {ACCENT_COLOR};
    }}
    body {{
        background-color: var(--light-background);
        color: var(--light-text);
        transition: background-color 0.3s, color 0.3s;
    }}
    [data-theme="dark"] body {{
        background-color: var(--dark-background);
        color: var(--dark-text);
    }}
    .stButton>button {{
        background-color: var(--primary-color);
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 16px;
        transition: 0.3s;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }}
    .stButton>button:hover {{
        background-color: var(--secondary-color);
        transform: scale(1.05);
    }}
    h1, h2, h3 {{
        color: var(--primary-color);
    }}
    </style>
""", unsafe_allow_html=True)

# JavaScript untuk mendeteksi preferensi mode gelap/terang
st.markdown("""
    <script>
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    const rootElement = document.documentElement;

    if (prefersDarkScheme.matches) {
        rootElement.setAttribute('data-theme', 'dark');
    } else {
        rootElement.setAttribute('data-theme', 'light');
    }

    // Listen for changes
    prefersDarkScheme.addEventListener('change', (event) => {
        if (event.matches) {
            rootElement.setAttribute('data-theme', 'dark');
        } else {
            rootElement.setAttribute('data-theme', 'light');
        }
    });
    </script>
""", unsafe_allow_html=True)

# --- Fungsi Animasi ---
def animation_effect():
    st.balloons()

# --- Fungsi Kirim Email ---
def kirim_notifikasi_email(email_pengguna, jenis_makanan, hari_tanggal):
    try:
        pengirim_email = "your_email@example.com"  # Ganti dengan email pengirim
        password_email = "your_password"  # Ganti dengan password pengirim
        penerima_email = email_pengguna

        # Buat pesan email
        msg = MIMEMultipart()
        msg['From'] = pengirim_email
        msg['To'] = penerima_email
        msg['Subject'] = f"Peringatan Kedaluwarsa {jenis_makanan}"

        body = f"""
        Hallo,

        Kami ingin mengingatkan Anda bahwa {jenis_makanan} Anda hampir kedaluwarsa pada {hari_tanggal}.
        Harap pastikan untuk segera mengonsumsinya atau memeriksanya kembali.

        Terima kasih,
        Pendeteksi Kelayakan Makanan
        """
        msg.attach(MIMEText(body, 'plain'))

        # Kirim email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(pengirim_email, password_email)
            server.sendmail(pengirim_email, penerima_email, msg.as_string())

        st.success("Notifikasi email berhasil dikirim!")
    except Exception as e:
        st.error(f"Error mengirim email: {e}")

# --- Navigasi Sidebar ---
menu = st.sidebar.selectbox("📂 Menu", [
    "🏠 Beranda",
    "🧮 Penilaian Kelayakan Makanan",
    "ℹ️ Info"
])

# --- Beranda ---
if menu == "🏠 Beranda":
    st.title("🍎 FRESH CHECK - Pendeteksi Kelayakan Konsumsi Makanan")

    st.image("https://www.ybkb.or.id/wp-content/uploads/2024/03/shopping-bag-full-fresh-fruits-vegetables-with-assorted-ingredients-min-825x551_yUwnK.jpg", width=700)

    st.markdown("""
    ### 🌟 Selamat Datang di **Pendeteksi Kelayakan Konsumsi Makanan**!  
    Aplikasi ini dirancang untuk membantu Anda mengonsumsi makanan yang **sehat** dan **aman** dengan fitur menarik berikut:

    - 📅 **Pengecekan Tanggal Kedaluwarsa**: Pantau masa simpan makanan agar tetap aman.  
    """)
    st.markdown("---")
    st.info("💡 **Tips:** Jaga kesehatan dengan memilih makanan bergizi dan mengolahnya dengan cara yang tepat!")

# --- Penilaian Kelayakan ---
elif menu == "🧮 Penilaian Kelayakan Makanan":
    st.title("🔍 Penilaian Kelayakan Makanan")

    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", [
        "Sayuran 🥦",
        "Buah-buahan 🍎",
        "Daging 🍖"
    ])

    if jenis_makanan == "Buah-buahan 🍎":
        bahan_makanan = st.selectbox("🍏 Pilih Buah", ["Anggur", "Mangga", "Kiwi", "Pisang"])
    elif jenis_makanan == "Sayuran 🥦":
        bahan_makanan = st.selectbox("🥦 Pilih Sayuran", ["Wortel", "Kubis", "Bayam"])
    elif jenis_makanan == "Daging 🍖":
        bahan_makanan = st.selectbox("🍖 Pilih Daging", ["Daging Sapi", "Daging Ayam", "Ikan"])

    tanggal_input = st.date_input("📅 Tanggal Pembelian")
    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", ["Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"])
    perubahan_fisik = st.checkbox("⚠️ Apakah terdapat perubahan fisik pada makanan?", key="perubahan_fisik")

    email_pengguna = st.text_input("📧 Masukkan Email Anda untuk Notifikasi", "")

    if st.button("🔎 Cek Kelayakan"):
        animation_effect()
        hari_ini = datetime.now().date()
        lama_simpan = (hari_ini - tanggal_input).days

        if tanggal_input > hari_ini:
            st.error("❗ Tanggal yang Anda masukkan tidak valid.")
        else:
            st.success(f"Data kelayakan untuk {bahan_makanan}: {lama_simpan} hari sejak pembelian.")
            if email_pengguna:
                kirim_notifikasi_email(email_pengguna, bahan_makanan, tanggal_input)

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
