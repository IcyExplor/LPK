import streamlit as st
from PIL import Image
from datetime import datetime

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

# Efek Animasi Balon dan Salju
def animation_effect():
    st.balloons()
    for _ in range(3):
        st.markdown('<div class="snowflake">❄️</div>', unsafe_allow_html=True)

# Navigasi Sidebar
menu = st.sidebar.selectbox("📂 Menu", [
    "🏠 Beranda", 
    "🧮 Penilaian Kelayakan Makanan", 
    "ℹ️ Info"
])

# Beranda
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

# Penilaian Kelayakan Makanan
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

    tanggal_input = st.date_input("📅 Tanggal Pembelian")
    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
        "Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"
    ])
    perubahan_fisik = st.multiselect("⚠️ Perubahan Fisik", [
        "Perubahan warna 🎨", "Bau tidak sedap 🤢", 
        "Tekstur berlendir 🦠"
    ])

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

            # Menampilkan saran penyimpanan
            saran_penyimpanan = {
                "Anggur 🍇": {
                    "Suhu Ruang 🌡️": "5–7 hari. Pisah anggur yang masih baik dengan anggur yang sudah membusuk. Jauhkan dari bahan makanan lain dengan aroma menyengat.",
                    "Kulkas (0–4°C) ❄️": "2 minggu. Simpan dalam plastik kedap udara atau wadah tertutup, pisahkan anggur yang busuk.",
                    "Freezer (-18°C) 🧊": "1 bulan. Jangan dicairkan karena buah akan menjadi lembek."
                },
                "Mangga 🥭": {
                    "Suhu Ruang 🌡️": "3–5 hari. Jangan simpan terlalu lama karena dapat mengurangi kesegaran.",
                    "Kulkas (0–4°C) ❄️": "2-3 hari. Jangan simpan di kulkas terlalu lama untuk menjaga rasa dan kesegaran.",
                    "Freezer (-18°C) 🧊": "> 1 minggu. Jika sudah dipotong, simpan di freezer dalam wadah kedap udara."
                },
                "Kiwi 🥝": {
                    "Suhu Ruang 🌡️": "3–5 hari. Simpan di suhu ruang agar tetap matang dan lezat.",
                    "Kulkas (0–4°C) ❄️": "1–2 minggu. Jika sudah matang, simpan di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                },
                "Nanas 🍍": {
                    "Suhu Ruang 🌡️": "3–5 hari. Nanas utuh sebaiknya disimpan di suhu ruang.",
                    "Kulkas (0–4°C) ❄️": "1 minggu. Setelah dipotong, simpan di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                },
                "Alpukat 🥑": {
                    "Suhu Ruang 🌡️": "3–5 hari. Setelah matang, konsumsilah segera. Jika belum matang, simpan di suhu ruang.",
                    "Kulkas (0–4°C) ❄️": "Tidak disarankan, alpukat akan cepat rusak bahkan di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                },
                "Pisang 🍌": {
                    "Suhu Ruang 🌡️": "3–5 hari. Pisang tidak perlu disimpan di kulkas.",
                    "Kulkas (0–4°C) ❄️": "Tidak disarankan. Pisang akan berubah menjadi coklat dan tidak matang.",
                    "Freezer (-18°C) 🧊": "Dapat dibekukan untuk konsumsi smoothie, tetapi teksturnya akan berubah."
                },
                "Jeruk 🍊": {
                    "Suhu Ruang 🌡️": "1 minggu. Simpan jeruk di suhu ruang jika akan dimakan dalam waktu dekat.",
                    "Kulkas (0–4°C) ❄️": "2–3 minggu. Jeruk akan tetap segar lebih lama di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan, bisa mengubah tekstur buah."
                },
                "Melon 🍉": {
                    "Suhu Ruang 🌡️": "3–5 hari. Simpan melon di suhu ruang agar tetap segar.",
                    "Kulkas (0–4°C) ❄️": "1 minggu. Setelah dipotong, simpan di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                },
                "Semangka 🍉": {
                    "Suhu Ruang 🌡️": "3–5 hari. Semangka utuh lebih baik disimpan di suhu ruang.",
                    "Kulkas (0–4°C) ❄️": "1 minggu. Setelah dipotong, simpan di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                },
                "Strawberry 🍓": {
                    "Suhu Ruang 🌡️": "1–2 hari. Strawberry lebih baik disimpan di kulkas.",
                    "Kulkas (0–4°C) ❄️": "5–7 hari. Simpan dalam wadah kedap udara.",
                    "Freezer (-18°C) 🧊": "Bisa dibekukan untuk jangka waktu lebih lama, cocok untuk smoothie."
                },
                "Buah Potong 🍉": {
                    "Suhu Ruang 🌡️": "Tidak disarankan. Buah potong harus segera disimpan di kulkas.",
                    "Kulkas (0–4°C) ❄️": "1–2 hari. Buah potong harus disimpan dalam wadah kedap udara.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan, kecuali untuk smoothie atau jus."
                },
                "Pepaya 🍈": {
                    "Suhu Ruang 🌡️": "3–5 hari. Simpan pepaya di suhu ruang.",
                    "Kulkas (0–4°C) ❄️": "1 minggu. Jika sudah dipotong, simpan di kulkas.",
                    "Freezer (-18°C) 🧊": "Tidak disarankan untuk dibekukan."
                }
            }
            if bahan_makanan in saran_penyimpanan:
                st.info("📦 **Saran Penyimpanan untuk {}**".format(bahan_makanan))
                for tipe_penyimpanan, saran in saran_penyimpanan[bahan_makanan].items():
                    st.write(f"{tipe_penyimpanan}: {saran}")

# Info
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

# Footer
st.markdown("---")
st.caption("🥗 *Dirancang untuk mendukung gaya hidup sehat dan aman setiap hari.*")
