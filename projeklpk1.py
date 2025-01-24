import streamlit as st
from PIL import Image
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(page_title="Food Freshness App", page_icon="🍎", layout="wide")

# Palet Warna
PRIMARY_COLOR = "#4CAF50"
SECONDARY_COLOR = "#F44336"
BACKGROUND_COLOR_LIGHT = "#E3F2FD"  # Biru muda untuk mode terang
BACKGROUND_COLOR_DARK = "#121212"  # Gelap untuk mode gelap
TEXT_COLOR_LIGHT = "#333333"
TEXT_COLOR_DARK = "#FFFFFF"
ACCENT_COLOR = "#FFC107"

# CSS Kustom
st.markdown(f"""
    <style>
    /* Menyesuaikan tema berdasarkan preferensi pengguna */
    @media (prefers-color-scheme: light) {{
        .main {{
            background-color: {BACKGROUND_COLOR_LIGHT} !important;
            color: {TEXT_COLOR_LIGHT};
            font-family: 'Poppins', sans-serif;
        }}
        .stApp {{
            background-color: {BACKGROUND_COLOR_LIGHT} !important;
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
    }}

    @media (prefers-color-scheme: dark) {{
        .main {{
            background-color: {BACKGROUND_COLOR_DARK} !important;
            color: {TEXT_COLOR_DARK};
            font-family: 'Poppins', sans-serif;
        }}
        .stApp {{
            background-color: {BACKGROUND_COLOR_DARK} !important;
        }}
        .stButton>button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-size: 16px;
            transition: 0.3s;
            box-shadow: 2px 2px 5px rgba(255, 255, 255, 0.2);
        }}
        .stButton>button:hover {{
            background-color: {SECONDARY_COLOR};
            transform: scale(1.05);
        }}
        .sidebar .sidebar-content {{
            background-color: #333333;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.3);
        }}
        h1, h2, h3 {{
            color: {ACCENT_COLOR};
        }}
    }}
    </style>
""", unsafe_allow_html=True)

# --- Efek Animasi Balon dan Salju ---
def animation_effect():
    st.balloons()
    for _ in range(3):
        st.markdown('<div class="snowflake">❄️</div>', unsafe_allow_html=True)

# --- Navigasi Sidebar ---
menu = st.sidebar.selectbox("📂 Menu", [
    "🏠 Beranda", 
    "🧮 Penilaian Kelayakan Makanan", 
    "ℹ️ Info"
])

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

    # Pilih Jenis Makanan Utama
    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", [
        "Sayuran 🥦",
        "Buah-buahan 🍎",
        "Daging 🍖"
    ])

    # Pilihan bahan makanan berdasarkan kategori
    if jenis_makanan == "Buah-buahan 🍎":
        bahan_makanan = st.selectbox("🍏 Pilih Buah", [
            "Anggur", "Mangga", "Alpukat", "Pisang", "Jeruk",
            "Melon", "Semangka", "Strawberry", "Buah Potong", "Pepaya"
        ])
    elif jenis_makanan == "Sayuran 🥦":
        bahan_makanan = st.selectbox("🥦 Pilih Sayuran", [
            "Kubis", "Wortel", "Bayam", "Kentang", "Mentimun"
        ])
    elif jenis_makanan == "Daging 🍖":
        bahan_makanan = st.selectbox("🍖 Pilih Daging", [
            "Daging Sapi", "Daging Ayam", "Ikan"
        ])

    # Input Tanggal Pembelian
    tanggal_input = st.date_input("📅 Tanggal Pembelian")

    # Kondisi Penyimpanan
    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
        "Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"
    ])

    # Perubahan Fisik
    perubahan_fisik = st.multiselect("⚠️ Perubahan Fisik", [
        "Perubahan warna 🎨", "Bau tidak sedap 🤢",
        "Tekstur berlendir 🦠"
    ])

    # Tombol untuk Cek Kelayakan
    if st.button("🔎 Cek Kelayakan"):
        # Validasi Tanggal
        hari_ini = datetime.now().date()
        if tanggal_input > hari_ini:
            st.error("❗ Tanggal yang Anda masukkan tidak valid. Harap masukkan tanggal sebelum hari ini.")
        else:
            # Hitung Lama Penyimpanan
            lama_simpan = (hari_ini - tanggal_input).days

            # Tampilkan Informasi Berdasarkan Kategori dan Kondisi
            st.write(f"### Informasi untuk: {bahan_makanan}")
            if jenis_makanan == "Buah-buahan 🍎":
                if bahan_makanan == "Pisang":
                    st.warning("🍌 Pisang yang muncul titik coklat masih layak dimakan, namun jika kulit menghitam bisa jadi sudah terlalu matang.")
                    if kondisi_penyimpanan == "Suhu Ruang 🌡️":
                        st.info(f"Suhu Ruang: 3–5 hari. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Kulkas ❄️":
                        st.info(f"Kulkas: Hingga 7 hari. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Freezer 🧊":
                        st.info("Tidak direkomendasikan untuk menyimpan pisang mentah di freezer.")

                elif bahan_makanan == "Mangga":
                    st.warning("🥭 Mangga yang berubah warna menjadi kuning/oranye menunjukkan kematangan.")
                    if kondisi_penyimpanan == "Suhu Ruang 🌡️":
                        st.info(f"Suhu Ruang: 2–3 hari. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Kulkas ❄️":
                        st.info(f"Kulkas: 5–7 hari. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Freezer 🧊":
                        st.info("Freezer: Hingga 6 bulan jika dibuat puree terlebih dahulu.")

                # Tambahkan logika serupa untuk buah lainnya...

            elif jenis_makanan == "Sayuran 🥦":
                if bahan_makanan == "Kubis":
                    st.warning("🥬 Kubis yang lembek atau layu menunjukkan kehilangan kesegaran.")
                    if kondisi_penyimpanan == "Suhu Ruang 🌡️":
                        st.info(f"Suhu Ruang: 1–2 hari. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Kulkas ❄️":
                        st.info(f"Kulkas: 1–2 minggu. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Freezer 🧊":
                        st.info("Tidak direkomendasikan untuk membekukan kubis.")

                # Tambahkan logika serupa untuk sayuran lainnya...

            elif jenis_makanan == "Daging 🍖":
                if bahan_makanan == "Daging Sapi":
                    st.warning("🥩 Daging sapi yang berwarna kecoklatan atau berlendir menunjukkan mulai rusak.")
                    if kondisi_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("Daging sapi tidak boleh disimpan di suhu ruang lebih dari 2 jam.")
                    elif kondisi_penyimpanan == "Kulkas ❄️":
                        st.info(f"Kulkas: 1–2 hari. Anda telah menyimpan selama {lama_simpan} hari.")
                    elif kondisi_penyimpanan == "Freezer 🧊":
                        st.info("Freezer: Hingga 6 bulan dalam kemasan kedap udara.")

                # Tambahkan logika serupa untuk daging lainnya...

            # Evaluasi Perubahan Fisik
            if perubahan_fisik:
                st.error(f"Perubahan fisik terdeteksi: {', '.join(perubahan_fisik)}. Makanan kemungkinan tidak layak konsumsi.")
            else:
                st.success("✅ Tidak ada perubahan fisik terdeteksi. Makanan kemungkinan masih layak dimakan.")


# --- Info ---
if menu == "ℹ️ Info":
    st.title("ℹ️ Informasi Pengembang")
    st.markdown("""
    **Aplikasi ini dikembangkan oleh:**

    - 👩‍💻 **Azzahra Sadrina Nadzifa (2350080)**
    - 👩‍💻 **Dhyza Aulia Shabirah (2350084)**
    - 👩‍💻 **Diyan Theda Mufarrihah (2350085)** 
    - 👩‍💻 **Haija Nafiah (2350094)**
    - 👨‍💻 **Irsan Abdurrahman (2350100)**

    Dibuat dengan ❤️ oleh **Kelompok 10**

    Program Studi D-IV Nanoteknologi Pangan  
    Politeknik AKA Bogor
    """)


# --- Footer ---
st.markdown("---")
st.caption("🥗 *Dirancang untuk mendukung gaya hidup sehat dan aman setiap hari.*")
