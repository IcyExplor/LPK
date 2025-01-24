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

    # Metode Penyimpanan
    metode_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
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

            # Informasi umum berdasarkan jenis makanan dan bahan
            if jenis_makanan == "Buah-buahan 🍎":
                rekomendasi = {
                    "Pisang": {
                        "Suhu Ruang 🌡️": "3–5 hari. Tidak perlu disimpan di kulkas.",
                        "Kulkas (0–4°C) ❄️": "Hingga 7 hari. Hindari suhu terlalu dingin.",
                        "Freezer (-18°C) 🧊": "Tidak direkomendasikan untuk pisang mentah."
                    },
                    "Mangga": {
                        "Suhu Ruang 🌡️": "2–3 hari. Simpan di kulkas untuk memperpanjang kesegaran.",
                        "Kulkas (0–4°C) ❄️": "5–7 hari. Gunakan wadah tertutup.",
                        "Freezer (-18°C) 🧊": "Hingga 6 bulan jika dibuat puree terlebih dahulu."
                    },
                    "Anggur": {
                        "Suhu Ruang 🌡️": "5–7 hari. Pisahkan anggur busuk.",
                        "Kulkas (0–4°C) ❄️": "2 minggu. Gunakan plastik kedap udara.",
                        "Freezer (-18°C) 🧊": "1 bulan. Jangan dicairkan karena buah menjadi lembek."
                    },
                    "Alpukat": {
                        "Suhu Ruang 🌡️": "3–5 hari. Setelah matang, konsumsilah segera. Jika belum matang, simpan di suhu ruang.",
                        "Kulkas (0–4°C) ❄️": "Tidak disarankan, alpukat akan cepat rusak bahkan di kulkas.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                    },
                    "Jeruk": {
                        "Suhu Ruang 🌡️": "1 minggu. Simpan jeruk di suhu ruang jika akan dimakan dalam waktu dekat.",
                        "Kulkas (0–4°C) ❄️": "2–3 minggu. Jeruk akan tetap segar lebih lama di kulkas.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan, bisa mengubah tekstur buah."
                    },
                    "Melon": {
                        "Suhu Ruang 🌡️": "3–5 hari. Simpan melon di suhu ruang agar tetap segar.",
                        "Kulkas (0–4°C) ❄️": "1 minggu. Setelah dipotong, simpan di kulkas.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                    },
                    "Semangka": {
                        "Suhu Ruang 🌡️": "3–5 hari. Semangka utuh lebih baik disimpan di suhu ruang.",
                        "Kulkas (0–4°C) ❄️": "1 minggu. Setelah dipotong, simpan di kulkas.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                    },
                    "Strawberry": {
                        "Suhu Ruang 🌡️": "1–2 hari. Strawberry lebih baik disimpan di kulkas.",
                        "Kulkas (0–4°C) ❄️": "5–7 hari. Simpan dalam wadah kedap udara.",
                        "Freezer (-18°C) 🧊": "Bisa dibekukan untuk jangka waktu lebih lama, cocok untuk smoothie."
                    },
                    "Buah Potong": {
                        "Suhu Ruang 🌡️": "Tidak disarankan. Buah potong harus segera disimpan di kulkas.",
                        "Kulkas (0–4°C) ❄️": "1–2 hari. Buah potong harus disimpan dalam wadah kedap udara.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan, kecuali untuk smoothie atau jus."
                    },
                    "Pepaya": {
                        "Suhu Ruang 🌡️": "3–5 hari. Simpan pepaya di suhu ruang.",
                        "Kulkas (0–4°C) ❄️": "1 minggu. Jika sudah dipotong, simpan di kulkas.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                    }
                }
                if bahan_makanan in rekomendasi:
                    rekomendasi_bahan = rekomendasi[bahan_makanan].get(metode_penyimpanan, "Tidak ada data.")
                    st.info(rekomendasi_bahan)

            elif jenis_makanan == "Sayuran 🥦":
                rekomendasi = {
                    "Kubis": {
                        "Suhu Ruang 🌡️": "1–2 hari. Simpan di kulkas untuk memperpanjang umur simpan.",
                        "Kulkas (0–4°C) ❄️": "1–2 minggu. Gunakan laci khusus sayur.",
                        "Freezer (-18°C) 🧊": "Tidak direkomendasikan karena merusak tekstur."
                    },
                    "Wortel": {
                        "Suhu Ruang 🌡️": "5–7 hari. Wortel dapat disimpan di suhu ruang jika tidak terlalu lama.",
                        "Kulkas (0–4°C) ❄️": "2–3 minggu. Simpan dalam kantong plastik atau wadah kedap udara di kulkas.",
                        "Freezer (-18°C) 🧊": "3 bulan. Wortel bisa dibekukan setelah dipotong dan disiapkan dengan baik."
                    },
                    "Bayam": {
                        "Suhu Ruang 🌡️": "1 hari. Bayam harus segera disimpan di kulkas karena mudah layu di suhu ruang.",
                        "Kulkas (0–4°C) ❄️": "2–3 hari. Simpan dalam kantong plastik berlubang atau wadah kedap udara.",
                        "Freezer (-18°C) 🧊": "1 bulan. Bayam bisa dibekukan setelah direbus terlebih dahulu."
                    },
                    "Kentang": {
                        "Suhu Ruang 🌡️": "1 minggu. Simpan kentang di suhu ruang di tempat yang sejuk dan gelap.",
                        "Kulkas (0–4°C) ❄️": "Tidak disarankan. Kentang akan berubah rasa dan tekstur jika disimpan di kulkas.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan. Kentang akan kehilangan tekstur setelah dibekukan."
                    },
                    "Mentimun": {
                        "Suhu Ruang 🌡️": "1–2 hari. Mentimun lebih baik disimpan di kulkas untuk menjaga kesegarannya.",
                        "Kulkas (0–4°C) ❄️": "1 minggu. Simpan dalam kantong plastik atau wadah kedap udara.",
                        "Freezer (-18°C) 🧊": "Tidak disarankan. Mentimun akan kehilangan tekstur setelah dibekukan."
                    }
                }
                if bahan_makanan in rekomendasi:
                    rekomendasi_bahan = rekomendasi[bahan_makanan].get(metode_penyimpanan, "Tidak ada data.")
                    st.info(rekomendasi_bahan)

            elif jenis_makanan == "Daging 🍖":
                rekomendasi = {
                    "Daging Sapi": {
                        "Suhu Ruang 🌡️": "Tidak disarankan. Segera masak.",
                        "Kulkas (0–4°C) ❄️": "1–2 hari untuk daging mentah.",
                        "Freezer (-18°C) 🧊": "Hingga 6 bulan jika dikemas kedap udara."
                    },
                    "Daging Ayam": {
                        "Suhu Ruang 🌡️": "2 jam. Daging ayam harus disimpan di suhu ruang tidak lebih dari 2 jam.",
                        "Kulkas (0–4°C) ❄️": "1–2 hari. Simpan di bagian bawah kulkas dalam wadah kedap udara.",
                        "Freezer (-18°C) 🧊": "9–12 bulan. Daging ayam dapat dibekukan dalam plastik kedap udara."
                    },
                    "Ikan": {
                        "Suhu Ruang 🌡️": "1 jam. Ikan tidak boleh dibiarkan lebih dari 1 jam di suhu ruang, terutama dalam suhu panas.",
                        "Kulkas (0–4°C) ❄️": "1–2 hari. Ikan segar sebaiknya disimpan di kulkas dalam wadah tertutup rapat.",
                        "Freezer (-18°C) 🧊": "3–6 bulan. Simpan ikan dalam kantong kedap udara di freezer untuk menjaga kesegaran."
                    }
                }
                if bahan_makanan in rekomendasi:
                    rekomendasi_bahan = rekomendasi[bahan_makanan].get(metode_penyimpanan, "Tidak ada data.")
                    st.info(rekomendasi_bahan)

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
