import streamlit as st

# Inisialisasi session state untuk mengontrol tampilan
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi untuk menghitung berat badan ideal
def hitung_berat_badan_ideal(tinggi, jenis_kelamin):
    if jenis_kelamin == 'Pria':
        return 0.9 * (tinggi - 100)
    else:
        return 0.85 * (tinggi - 100)

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    return berat / ((tinggi / 100) ** 2)

# Fungsi untuk kembali ke halaman utama
def go_home():
    st.session_state.page = "home"

# Gaya Global (Background dan Font)
def set_background():
    st.markdown(
        """
        <style>
        body {
            background-image: url('https://www.teahub.io/photos/full/8-85399_abstract-minimalist-background-hd.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: Arial, sans-serif;
        }
        .stButton button {
            background-color: #2E86C1;
            color: white;
            border-radius: 5px;
            padding: 8px 15px;
            font-weight: bold;
        }
        .stButton button:hover {
            background-color: #1B4F72;
        }
        h1, h2, h3 {
            color: white;
        }
        p, label {
            color: #FDFEFE;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Halaman Home
def home_page():
    st.markdown(
        """
        <h1 style='text-align: center;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        <h3 style='text-align: center; color: #5D6D7E;'>
            Solusi Praktis Untuk Pemantauan Kesehatan
        </h3>
        """,
        unsafe_allow_html=True
    )

    image_url = "https://static.vecteezy.com/system/resources/previews/016/828/833/original/bmi-classification-chart-measurement-woman-colorful-infographic-with-ruler-female-body-mass-index-scale-collection-from-underweight-to-overweight-fit-person-different-weight-level-eps-vector.jpg"
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{image_url}" style="width: 100%; max-width: 600px; border-radius: 15px; transition: transform 0.3s ease;" 
                 onmouseover="this.style.transform='scale(1.05)'" 
                 onmouseout="this.style.transform='scale(1)'">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <h2 style='text-align: center;'>
             Kelompok 5 
        </h2>
        <p style='text-align: Left;'>
            Anggota: <br>
            - Dwinta Syafa Salsabilla (2350086) <br>
            - Fasya Anindya Zahrani (2350089) <br>
            - Ilman Hakim Muhardian (2350099) <br>
            - Muthia Ammara Shafira (2350113) <br>
            - Zahid Nashrulloh Khoerudin (2350141) <br>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Penjelasan tentang BMI 📘"):
            st.session_state.page = "penjelasan"
    with col2:
        if st.button("Mulai Hitung BMI 🧮"):
            st.session_state.page = "kalkulator"

# Halaman Penjelasan BMI
def penjelasan_bmi():
    st.markdown(
        """
        <h1 style='text-align: center;'>
            Penjelasan tentang BMI
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Garis Pemisah
    st.markdown("---")

    st.markdown(
        """
        ### Apa itu BMI?
        **BMI (Body Mass Index)** atau Indeks Massa Tubuh adalah ukuran yang digunakan untuk menilai apakah berat badan seseorang 
        sesuai dengan tinggi badannya. BMI dihitung dengan membagi berat badan (dalam kilogram) dengan kuadrat tinggi badan 
        (dalam meter).

        ### Kategori BMI:
        - **Kurus**: BMI < 18.5
        - **Normal**: 18.5 ≤ BMI < 24.9
        - **Gemuk**: 25 ≤ BMI < 29.9
        - **Obesitas**: BMI ≥ 30

        ### Mengapa BMI Penting?
        BMI membantu Anda memahami apakah berat badan Anda berada dalam kisaran yang sehat. Namun, perlu diingat bahwa BMI 
        tidak memperhitungkan komposisi tubuh (seperti massa otot vs lemak), sehingga hasilnya mungkin tidak selalu akurat 
        untuk semua orang, terutama atlet atau orang dengan massa otot tinggi.

        ### Tips untuk Menjaga BMI Sehat:
        1. Konsumsi makanan bergizi seimbang.
        2. Rutin berolahraga.
        3. Hindari kebiasaan tidak sehat seperti merokok atau konsumsi alkohol berlebihan.
        4. Periksa kesehatan secara berkala.
        """
    )

    # Garis pemisah
    st.markdown("---")

    if st.button("Kembali ke Home 🏠"):
        go_home()

# Kalkulator BMI
def kalkulator_bmi():
    st.markdown(
        """
        <h1 style='text-align: center;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        <h3 style='text-align: center; color: #5D6D7E;'>
            Silakan masukkan data Anda untuk menghitung BMI.
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Garis Pemisah
    st.markdown("---")

    # Input fields dengan validasi
    col1, col2 = st.columns(2)
    with col1:
        tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=0.0, format="%.2f", key="tinggi")
    with col2:
        berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, format="%.2f", key="berat")

    jenis_kelamin = st.radio("Masukkan jenis kelamin Anda:", ('Pria', 'Wanita'), key="jenis_kelamin")
    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=0, format="%d", key="usia")

# Fungsi untuk menghitung berat badan ideal
def hitung_berat_badan_ideal(tinggi, jenis_kelamin):
    if jenis_kelamin == "Laki-laki":
        return (tinggi - 100) - ((tinggi - 150) / 4)
    elif jenis_kelamin == "Perempuan":
        return (tinggi - 100) - ((tinggi - 150) / 2.5)

# Fungsi untuk menghitung BMI
def hitung_bmi(berat, tinggi):
    return berat / (tinggi / 100) ** 2

# Fungsi untuk menentukan kategori BMI
def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Gemuk"
    else:
        return "Obesitas"

# Fungsi untuk menghitung BMI berdasarkan usia
def hitung_bmi_usia(bmi, usia):
    if usia < 18:
        return bmi * 0.9
    elif usia < 30:
        return bmi * 1.0
    elif usia < 50:
        return bmi * 1.1
    else:
        return bmi * 1.2

# Tombol untuk menghitung BMI
if st.button("Hitung BMI ", key="hitung_bmi_button"):
    tinggi = st.session_state.tinggi
    berat = st.session_state.berat
    usia = st.session_state.usia
    jenis_kelamin = st.session_state.jenis_kelamin
    if tinggi <= 0 or berat <= 0 or usia <= 0:
        st.error("Tinggi, berat badan, dan usia harus lebih dari 0.")
    else:
        # Hitung berat ideal, BMI, dan kategori
        berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
        bmi = hitung_bmi(berat, tinggi)
        kategori = kategori_bmi(bmi)

        # Hitung BMI berdasarkan usia
        bmi_usia = hitung_bmi_usia(bmi, usia)

        # Tampilkan hasil dengan styling menarik
        st.markdown("### Hasil Perhitungan")
        st.markdown(f"**Berat Badan Ideal Anda:** `{berat_ideal:.2f} kg`")
        st.markdown(f"**Indeks Massa Tubuh (BMI):** `{bmi:.2f}`")
        st.markdown(f"**BMI Berdasarkan Usia:** `{bmi_usia:.2f}`")
        st.markdown(f"**Kategori Berat Badan:** `{kategori}`")

        # Visualisasi kategori BMI dengan progress bar
        if kategori == "Kurus":
            st.progress(0.25)
            st.warning("Tips: Anda berada dalam kategori Kurus. Perhatikan asupan nutrisi dan konsultasikan dengan ahli gizi.")
        elif kategori == "Normal":
            st.progress(0.5)
            st.success("Selamat! Anda berada dalam kategori Normal. Pertahankan gaya hidup sehat!")
        elif kategori == "Gemuk":
            st.progress(0.75)
            st.warning("Tips: Anda berada dalam kategori Gemuk. Mulailah pola hidup sehat dan olahraga teratur.")
        else:
            st.progress(1.0)
            st.error("Perhatian: Anda berada dalam kategori Obesitas. Segera konsultasikan dengan dokter atau ahli gizi.")

    if st.button("Kembali ke Home 🏠"):
        go_home()

# Set Global Background
set_background()

# Main App Logic
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "penjelasan":
    penjelasan_bmi()
elif st.session_state.page == "kalkulator":
    kalkulator_bmi()
