import streamlit as st

# Inisialisasi session state untuk navigasi halaman
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi untuk menghitung berat badan ideal
def hitung_berat_badan_ideal(tinggi, jenis_kelamin):
    if jenis_kelamin == "Pria":
        return (tinggi - 100) - ((tinggi - 150) / 4)
    elif jenis_kelamin == "Wanita":
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

# Fungsi untuk kembali ke halaman utama
def go_home():
    st.session_state.page = "home"

# Gaya dinamis untuk mendukung mode terang/gelap
def set_dynamic_theme():
    st.markdown(
        """
        <style>
        /* Mode Terang */
        @media (prefers-color-scheme: light) {
            body {
                background-color: #F8F9FA;
                color: #212529;
                font-family: 'Arial', sans-serif;
            }
            .stButton button {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                font-weight: bold;
            }
            .stButton button:hover {
                background-color: #0056b3;
            }
            h1, h2, h3 {
                color: #212529;
            }
        }

        /* Mode Gelap */
        @media (prefers-color-scheme: dark) {
            body {
                background-color: #121212;
                color: #EAEAEA;
                font-family: 'Arial', sans-serif;
            }
            .stButton button {
                background-color: #1F7A8C;
                color: white;
                border-radius: 5px;
                font-weight: bold;
            }
            .stButton button:hover {
                background-color: #145366;
            }
            h1, h2, h3 {
                color: #EAEAEA;
            }
        }

        /* Gaya umum */
        .center {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Halaman Home
def home_page():
    st.markdown(
        """
        <h1 class='center'>Aplikasi Pengukur Body Mass Index (BMI)</h1>
        <h3 class='center'>Solusi Praktis Untuk Pemantauan Kesehatan Anda</h3>
        """,
        unsafe_allow_html=True
    )

    image_url = "https://static.vecteezy.com/system/resources/previews/016/828/833/original/bmi-classification-chart-measurement-woman-colorful-infographic-with-ruler-female-body-mass-index-scale-collection-from-underweight-to-overweight-fit-person-different-weight-level-eps-vector.jpg"
    st.markdown(
        f"""
        <div class='center'>
            <img src="{image_url}" style="width: 100%; max-width: 600px; border-radius: 15px; margin: 20px auto;">
        </div>
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
    st.markdown("<h1 class='center'>Penjelasan tentang BMI</h1>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        """
        ### Apa itu BMI?
        **BMI (Body Mass Index)** adalah ukuran yang digunakan untuk menilai apakah berat badan seseorang 
        sesuai dengan tinggi badannya. BMI dihitung dengan membagi berat badan (dalam kilogram) dengan kuadrat tinggi badan 
        (dalam meter).

        ### Kategori BMI:
        - **Kurus**: BMI < 18.5
        - **Normal**: 18.5 ≤ BMI < 24.9
        - **Gemuk**: 25 ≤ BMI < 29.9
        - **Obesitas**: BMI ≥ 30

        ### Mengapa Penting?
        BMI membantu memahami apakah berat badan berada dalam kisaran sehat. Namun, BMI tidak memperhitungkan 
        massa otot, sehingga hasilnya mungkin tidak sepenuhnya akurat untuk atlet atau individu berotot.

        ### Tips Menjaga BMI Sehat:
        - Konsumsi makanan bergizi.
        - Rutin berolahraga.
        - Hindari kebiasaan tidak sehat.
        - Periksa kesehatan secara berkala.
        """
    )

    st.markdown("---")

    if st.button("Kembali ke Home 🏠"):
        go_home()

# Kalkulator BMI
def kalkulator_bmi():
    st.markdown("<h1 class='center'>Kalkulator Body Mass Index (BMI)</h1>", unsafe_allow_html=True)

    st.markdown("---")

    tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=0.0, format="%.2f", key="tinggi")
    berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, format="%.2f", key="berat")
    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ('Pria', 'Wanita'), key="jenis_kelamin")

    if st.button("Hitung BMI 🧮"):
        if tinggi <= 0 or berat <= 0:
            st.error("Masukkan tinggi dan berat badan yang valid!")
        else:
            berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
            bmi = hitung_bmi(berat, tinggi)
            kategori = kategori_bmi(bmi)

            st.markdown("### Hasil Perhitungan")
            st.markdown(f"**Berat Badan Ideal Anda:** `{berat_ideal:.2f} kg`")
            st.markdown(f"**Indeks Massa Tubuh (BMI):** `{bmi:.2f}`")
            st.markdown(f"**Kategori Berat Badan:** `{kategori}`")

            if kategori == "Kurus":
                st.warning("Anda berada dalam kategori Kurus. Perhatikan asupan nutrisi Anda.")
            elif kategori == "Normal":
                st.success("Selamat! Anda berada dalam kategori Normal.")
            elif kategori == "Gemuk":
                st.warning("Anda berada dalam kategori Gemuk. Mulailah pola hidup sehat.")
            else:
                st.error("Anda berada dalam kategori Obesitas. Konsultasikan dengan ahli gizi.")

    if st.button("Kembali ke Home 🏠"):
        go_home()

# Set Dynamic Theme
set_dynamic_theme()

# Main Logic
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "penjelasan":
    penjelasan_bmi()
elif st.session_state.page == "kalkulator":
    kalkulator_bmi()
