import streamlit as st
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Fungsi untuk mengirim email notifikasi
def kirim_notifikasi_email(email_pengguna, jenis_makanan, hari_tanggal):
    try:
        # Setup email
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

# Fungsi untuk memeriksa perubahan fisik
def periksa_perubahan_fisik(jenis_makanan, bahan_makanan):
    if jenis_makanan == "Buah-buahan 🍎":
        if bahan_makanan == "Pisang":
            st.warning("🍌 Pisang yang muncul titik coklat masih layak dimakan, namun rasanya lebih manis. Jika kulit menghitam, bisa jadi sudah sangat matang.")
        elif bahan_makanan == "Mangga":
            st.warning("🥭 Mangga yang berubah warna dari hijau ke kuning/oranye adalah tanda kematangan dan tetap layak dikonsumsi.")
        # Add more checks for fruits
    elif jenis_makanan == "Sayuran 🥦":
        if bahan_makanan == "Kubis":
            st.warning("🥬 Kubis yang lembek atau layu menunjukkan kehilangan kesegaran. Jika berlendir, sebaiknya dibuang.")
        # Add more checks for vegetables
    elif jenis_makanan == "Daging 🍖":
        if bahan_makanan == "Daging Sapi":
            st.warning("🥩 Daging sapi yang berwarna kecoklatan atau berlendir bisa menunjukkan mulai rusak. Pastikan tidak berbau busuk.")
        # Add more checks for meats

# Validasi email dan input pengguna
def validasi_input(email_pengguna, tanggal_input, perubahan_fisik):
    if not email_pengguna or "@" not in email_pengguna:
        st.error("❗ Mohon masukkan alamat email yang valid.")
        return False
    if tanggal_input == "":
        st.error("❗ Mohon masukkan tanggal pembelian yang valid.")
        return False
    if not perubahan_fisik:
        st.warning("⚠️ Periksa kembali apakah ada perubahan fisik pada makanan.")
        return False
    return True

# --- Navigasi Sidebar ---
menu = st.sidebar.selectbox("📂 Menu", [
    "🏠 Beranda", 
    "🧮 Penilaian Kelayakan Makanan", 
    "ℹ️ Info"
])

# --- Penilaian Kelayakan Makanan ---
if menu == "🧮 Penilaian Kelayakan Makanan":
    st.title("🔍 Penilaian Kelayakan Makanan")

    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", [
        "Sayuran 🥦", 
        "Buah-buahan 🍎", 
        "Daging 🍖"
    ])

    if jenis_makanan == "Buah-buahan 🍎":
        bahan_makanan = st.selectbox("🍏 Pilih Buah", [
            "Anggur", "Mangga", "Kiwi", "Nanas", 
            "Alpukat", "Pisang", "Jeruk", "Melon", 
            "Semangka", "Strawberry", "Buah Potong", "Pepaya"
        ])
    elif jenis_makanan == "Sayuran 🥦":
        bahan_makanan = st.selectbox("🥦 Pilih Sayuran", [
            "Kubis", "Wortel", "Kembang Kol", "Selada", 
            "Jamur", "Bayam", "Kentang", "Mentimun", 
            "Terong", "Jagung"
        ])
    elif jenis_makanan == "Daging 🍖":
        bahan_makanan = st.selectbox("🍖 Pilih Daging", [
            "Daging Sapi", "Daging Ayam", "Ikan"
        ])

    # Input tanggal pembelian
    tanggal_input = st.date_input("📅 Tanggal Pembelian")

    # Pilih kondisi penyimpanan
    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
        "Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"
    ])

    # Pilih perubahan fisik
    perubahan_fisik = st.checkbox("⚠️ Apakah terdapat perubahan fisik pada makanan?", key="perubahan_fisik")

    email_pengguna = st.text_input("📧 Masukkan Email Anda untuk Notifikasi", "")

    if st.button("🔎 Cek Kelayakan"):
        # Validasi input
        if validasi_input(email_pengguna, tanggal_input, perubahan_fisik):
            hari_ini = datetime.now().date()
            lama_simpan = (hari_ini - tanggal_input).days

            if tanggal_input > hari_ini:
                st.error("❗ Tanggal yang Anda masukkan tidak valid. Silakan masukkan tanggal yang logis.")
            else:
                # Menangani kelayakan berdasarkan perubahan fisik dan lama simpan
                periksa_perubahan_fisik(jenis_makanan, bahan_makanan)
                # Mengirimkan email notifikasi
                kirim_notifikasi_email(email_pengguna, bahan_makanan, tanggal_input)

