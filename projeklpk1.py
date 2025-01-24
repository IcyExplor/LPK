import streamlit as st
from PIL import Image

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


# Menampilkan pilihan bahan makanan berdasarkan kategori yang dipilih
if menu == "🧮 Penilaian Kelayakan Makanan":
    st.title("🔍 Penilaian Kelayakan Makanan")

    # Pilih jenis makanan utama
    jenis_makanan = st.selectbox("🍽️ Pilih Jenis Makanan", [
        "Sayuran 🥦", 
        "Buah-buahan 🍎", 
        "Daging 🍖"
    ])

    # Menampilkan pilihan bahan makanan berdasarkan kategori yang dipilih
    if jenis_makanan == "Buah-buahan 🍎":
        bahan_makanan = st.selectbox("🍏 Pilih Buah", [
            "Anggur", "Mangga","Alpukat", "Pisang", "Jeruk", "Melon", 
            "Semangka", "Strawberry", "Buah Potong", "Pepaya"
        ])
    elif jenis_makanan == "Sayuran 🥦":
        bahan_makanan = st.selectbox("🥦 Pilih Sayuran", [
            "Kubis", "Wortel", "Bayam", "Kentang", "Mentimun"
        ])
    elif jenis_makanan == "Daging 🍖":
        bahan_makanan = st.selectbox("🍖 Pilih Daging", [
            "Daging Sapi", "Daging Ayam", "Ikan"
        ])

    # Menampilkan pilihan yang dipilih
    st.write(f"Anda memilih: {bahan_makanan}")

    # Input tanggal pembelian
    tanggal_input = st.date_input("📅 Tanggal Pembelian")

    # Pilih kondisi penyimpanan
    kondisi_penyimpanan = st.selectbox("❄️ Kondisi Penyimpanan", [
        "Suhu Ruang 🌡️", "Kulkas (0–4°C) ❄️", "Freezer (-18°C) 🧊"
    ])

    # Pilih perubahan fisik
    perubahan_fisik = st.multiselect("⚠️ Perubahan Fisik", [
        "Perubahan warna 🎨", "Bau tidak sedap 🤢", 
        "Tekstur berlendir 🦠"
    ])

import streamlit as st
from datetime import datetime

# Menampilkan pilihan bahan makanan berdasarkan kategori yang dipilih
if menu == "🧮 Penilaian Kelayakan Makanan":
    perubahan_fisik = st.button("🔎 Cek Kelayakan"):
        animation_effect()
    hari_ini = datetime.now().date()
    lama_simpan = (hari_ini - tanggal_input).days

    if tanggal_input > hari_ini:
        st.error("❗ Tanggal yang Anda masukkan tidak valid. Silakan masukkan tanggal yang logis.")
    else:
        # Menangani kelayakan berdasarkan perubahan fisik dan lama simpan
        metode_penyimpanan = st.selectbox("📦 Pilih Metode Penyimpanan:", ["Suhu Ruang 🌡️", "Kulkas ❄️", "Freezer 🧊"])

        if perubahan_fisik:
            if jenis_makanan == "Buah-buahan 🍎":
                if bahan_makanan == "Pisang":
                    st.warning("🍌 Pisang yang muncul titik coklat masih layak dimakan, namun rasanya lebih manis. Jika kulit menghitam, bisa jadi sudah sangat matang.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 3–5 hari. Pisang tidak perlu disimpan di kulkas.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: Hingga 7 hari, namun pastikan tidak terlalu dingin agar tidak mempercepat kerusakan.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak direkomendasikan untuk pisang mentah.")
                
                # Continue similar logic for other food types

                elif bahan_makanan == "Mangga":
                    st.warning("🥭 Mangga yang berubah warna dari hijau ke kuning/oranye adalah tanda kematangan dan tetap layak dikonsumsi.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 2–3 hari. Simpan di kulkas untuk memperpanjang kesegaran.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 5–7 hari. Simpan dalam wadah tertutup untuk mempertahankan kelembapan.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Hingga 6 bulan jika dibuat puree terlebih dahulu.")

                elif bahan_makanan == "Anggur 🍇":
                    st.warning("🍇 Anggur yang lembek atau mulai berair menandakan kerusakan. Sebaiknya buang bagian yang busuk untuk mencegah kontaminasi.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 5–7 hari. Pisah anggur yang masih baik dengan anggur yang sudah membusuk. Jauhkan dari bahan makanan lain dengan aroma menyengat.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 2 minggu. Simpan dalam plastik kedap udara atau wadah tertutup, pisahkan anggur yang busuk.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: 1 bulan. Jangan dicairkan karena buah akan menjadi lembek setelah beku.")

                elif bahan_makanan == "Alpukat 🥑":
                    st.warning("🥑 Alpukat yang berubah warna menjadi terlalu coklat atau lembek menandakan bahwa buah sudah tidak segar.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 3–5 hari. Setelah matang, konsumsilah segera. Jika belum matang, simpan di suhu ruang.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: Tidak disarankan, alpukat akan cepat rusak bahkan di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan untuk dibekukan.")

                elif bahan_makanan == "Jeruk 🍊":
                    st.warning("🍊 Jeruk dengan kulit yang keriput tetap layak dimakan tetapi teksturnya mungkin kurang segar.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1 minggu. Simpan jeruk di suhu ruang jika akan dimakan dalam waktu dekat.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 2–3 minggu. Jeruk akan tetap segar lebih lama di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan, bisa mengubah tekstur buah.")

                elif bahan_makanan == "Melon 🍉":
                    st.warning("🍈 Melon yang terlalu lembek atau berair menandakan mulai rusak.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 3–5 hari. Simpan melon di suhu ruang agar tetap segar.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1 minggu. Setelah dipotong, simpan di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan untuk dibekukan.")

                elif bahan_makanan == "Semangka 🍉":
                    st.warning("🍉 Semangka yang mulai lembek atau berair sebaiknya tidak dikonsumsi.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 3–5 hari. Semangka utuh lebih baik disimpan di suhu ruang.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1 minggu. Setelah dipotong, simpan di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan untuk dibekukan.")

                elif bahan_makanan == "Strawberry 🍓":
                    st.warning("🍓 Strawberry yang berjamur atau terlalu lembek sebaiknya tidak dimakan.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1–2 hari. Strawberry lebih baik disimpan di kulkas.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 5–7 hari. Simpan dalam wadah kedap udara.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Bisa dibekukan untuk jangka waktu lebih lama, cocok untuk smoothie.")

                elif bahan_makanan == "Buah Potong 🍉":
                    st.warning("🍉 Buah potong sangat mudah rusak, sebaiknya segera dimakan atau disimpan dengan baik.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: Tidak disarankan. Buah potong harus segera disimpan di kulkas.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1–2 hari. Buah potong harus disimpan dalam wadah kedap udara.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan, kecuali untuk smoothie atau jus.")

                elif bahan_makanan == "Pepaya 🍈":
                    st.warning("🍈 Pepaya yang terlalu lembek atau berair menandakan mulai rusak.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 3–5 hari. Simpan pepaya di suhu ruang.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1 minggu. Jika sudah dipotong, simpan di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan untuk dibekukan.")

                # Tambahkan logika yang sama untuk bahan makanan lainnya

            elif jenis_makanan == "Sayuran 🥦":
                if bahan_makanan == "Kubis":
                    st.warning("🥬 Kubis yang lembek atau layu menunjukkan kehilangan kesegaran. Jika berlendir, sebaiknya dibuang.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1–2 hari. Simpan di kulkas untuk memperpanjang umur simpan.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1–2 minggu. Simpan di laci khusus sayur agar lebih segar.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak direkomendasikan karena dapat merusak tekstur kubis.")

                elif bahan_makanan == "Wortel 🥕":
                    st.warning("🥕 Wortel yang mulai lembek atau berjamur sebaiknya tidak dikonsumsi.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 5–7 hari. Wortel dapat disimpan di suhu ruang jika tidak terlalu lama.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 2–3 minggu. Simpan dalam kantong plastik atau wadah kedap udara di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: 3 bulan. Wortel bisa dibekukan setelah dipotong dan disiapkan dengan baik.")

                elif bahan_makanan == "Bayam 🌿":
                    st.warning("🌿 Bayam yang menguning atau berlendir sudah tidak layak dikonsumsi.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1 hari. Bayam harus segera disimpan di kulkas karena mudah layu di suhu ruang.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 2–3 hari. Simpan dalam kantong plastik berlubang atau wadah kedap udara.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: 1 bulan. Bayam bisa dibekukan setelah direbus terlebih dahulu.")

                elif bahan_makanan == "Kentang 🥔":
                    st.warning("🥔 Kentang yang bertunas atau hijau tidak layak konsumsi karena mengandung solanin.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1 minggu. Simpan kentang di suhu ruang di tempat yang sejuk dan gelap.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: Tidak disarankan. Kentang akan berubah rasa dan tekstur jika disimpan di kulkas.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan. Kentang akan kehilangan tekstur setelah dibekukan.")

                elif bahan_makanan == "Mentimun 🥒":
                    st.warning("🥒 Mentimun yang lembek atau berlendir menandakan sudah tidak segar.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1–2 hari. Mentimun lebih baik disimpan di kulkas untuk menjaga kesegarannya.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1 minggu. Simpan dalam kantong plastik atau wadah kedap udara.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Tidak disarankan. Mentimun akan kehilangan tekstur setelah dibekukan.")

                # Tambahkan logika yang sama untuk bahan makanan lainnya

            elif jenis_makanan == "Daging 🍖":
                if bahan_makanan == "Daging Sapi":
                    st.warning("🥩 Daging sapi yang berwarna kecoklatan atau berlendir bisa menunjukkan mulai rusak. Pastikan tidak berbau busuk.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: Tidak disarankan. Daging sapi harus segera dimasak.")
                    elif metode_penyimpanan == "Kulkas ❄️":
                        st.info("**Kulkas ❄️**: 1–2 hari untuk daging mentah. Simpan di wadah tertutup.")
                    elif metode_penyimpanan == "Freezer 🧊":
                        st.info("**Freezer 🧊**: Hingga 6 bulan jika disimpan dalam kemasan kedap udara.")

                elif bahan_makanan == "Daging Ayam 🍗":
                    st.warning("🍗 Daging ayam harus ditangani dengan hati-hati untuk menjaga kualitasnya.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 2 jam. Daging ayam harus disimpan di suhu ruang tidak lebih dari 2 jam.")
                    elif metode_penyimpanan == "Kulkas (0–4°C) ❄️":
                        st.info("**Kulkas (0–4°C) ❄️**: 1–2 hari. Simpan di bagian bawah kulkas dalam wadah kedap udara.")
                    elif metode_penyimpanan == "Freezer (-18°C) 🧊":
                        st.info("**Freezer (-18°C) 🧊**: 9–12 bulan. Daging ayam dapat dibekukan dalam plastik kedap udara.")

                elif bahan_makanan == "Ikan 🐟":
                    st.warning("🐟 Ikan harus segera disimpan untuk menjaga kesegaran dan mencegah kerusakan.")
                    if metode_penyimpanan == "Suhu Ruang 🌡️":
                        st.info("**Suhu Ruang 🌡️**: 1 jam. Ikan tidak boleh dibiarkan lebih dari 1 jam di suhu ruang, terutama dalam suhu panas.")
                    elif metode_penyimpanan == "Kulkas (0–4°C) ❄️":
                        st.info("**Kulkas (0–4°C) ❄️**: 1–2 hari. Ikan segar sebaiknya disimpan di kulkas dalam wadah tertutup rapat.")
                    elif metode_penyimpanan == "Freezer (-18°C) 🧊":
                        st.info("**Freezer (-18°C) 🧊**: 3–6 bulan. Simpan ikan dalam kantong kedap udara di freezer untuk menjaga kesegaran.")


                # Tambahkan logika yang sama untuk bahan makanan lainnya

        else:
            st.success("✅ Tidak ada perubahan fisik. Makanan kemungkinan masih layak dimakan.")

                
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



