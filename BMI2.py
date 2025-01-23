import streamlit as st

# Inisialisasi session state untuk navigasi halaman
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

# Fungsi untuk menyesuaikan BMI berdasarkan usia
def sesuaikan_bmi_berdasarkan_usia(bmi, usia):
    if usia < 18:
        return bmi * 0.9  # Penyesuaian untuk remaja
    elif usia <= 30:
        return bmi * 1.0  # Usia dewasa muda (tidak ada perubahan)
    elif usia <= 50:
        return bmi * 1.1  # Penyesuaian untuk usia dewasa
    else:
        return bmi * 1.2  # Penyesuaian untuk lansia

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
        <h1 style='text-align: center;'>Aplikasi Pengukur Body Mass Index (BMI)</h1>
        <h3 style='text-align: center; color: #5D6D7E;'>Solusi Praktis Untuk Pemantauan Kesehatan</h3>
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
    st.markdown("<h1 style='text-align: center;'>Penjelasan tentang BMI</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        """
        ### Apa itu BMI?
        **BMI (Body Mass Index)** adalah ukuran untuk menilai apakah berat badan Anda sesuai dengan tinggi badan Anda. 
        BMI dihitung dengan membagi berat badan (kg) dengan kuadrat tinggi badan (m).

        ### Pengaruh Usia pada BMI
        Dengan bertambahnya usia, komposisi tubuh berubah. Penyesuaian BMI berdasarkan usia memastikan hasil yang lebih relevan.

        ### Kategori BMI
        - **Kurus**: BMI < 18.5
        - **Normal**: 18.5 ≤ BMI < 24.9
        - **Gemuk**: 25 ≤ BMI < 29.9
        - **Obesitas**: BMI ≥ 30
        """
    )
    st.markdown("---")
    if st.button("Kembali ke Home 🏠"):
        go_home()

# Kalkulator BMI
def kalkulator_bmi():
    st.markdown("<h1 style='text-align: center;'>Kalkulator BMI dengan Penyesuaian Usia</h1>", unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0, format="%.2f", key="tinggi")
    with col2:
        berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0, format="%.2f", key="berat")

    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ('Pria', 'Wanita'), key="jenis_kelamin")
    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=1, format="%d", key="usia")

    if st.button("Hitung BMI 🧮"):
        if tinggi <= 0 or berat <= 0 or usia <= 0:
            st.error("Masukkan data yang valid!")
        else:
            # Hitung berat ideal, BMI, dan penyesuaian
            berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
            bmi = hitung_bmi(berat, tinggi)
            bmi_disesuaikan = sesuaikan_bmi_berdasarkan_usia(bmi, usia)
            kategori = kategori_bmi(bmi_disesuaikan)

            # Tampilkan hasil
            st.markdown("### 🎯 Hasil Perhitungan")
            st.markdown(f"**Berat Badan Ideal Anda:** `{berat_ideal:.2f} kg`")
            st.markdown(f"**BMI Anda:** `{bmi:.2f}`")
            st.markdown(f"**BMI Setelah Penyesuaian Usia:** `{bmi_disesuaikan:.2f}`")
            st.markdown(f"**Kategori Berat Badan Anda:** `{kategori}`")

            # Progress bar sesuai kategori BMI
            if kategori == "Kurus":
                st.progress(0.25)
                st.warning("Anda dalam kategori Kurus. Konsultasikan dengan ahli gizi.")
            elif kategori == "Normal":
                st.progress(0.5)
                st.success("Selamat! Anda berada dalam kategori Normal.")
            elif kategori == "Gemuk":
                st.progress(0.75)
                st.warning("Anda dalam kategori Gemuk. Perhatikan pola hidup sehat.")
            else:
                st.progress(1.0)
                st.error("Anda dalam kategori Obesitas. Segera konsultasikan dengan ahli kesehatan.")

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
