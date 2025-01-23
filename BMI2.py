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

# Fungsi untuk menyesuaikan BMI berdasarkan usia
def sesuaikan_bmi_berdasarkan_usia(bmi, usia):
    """
    Penyesuaian nilai BMI berdasarkan usia.
    """
    if usia < 18:
        return bmi * 0.9  # Faktor penyesuaian untuk remaja
    elif usia <= 30:
        return bmi * 1.0  # Tidak ada perubahan untuk usia dewasa muda
    elif usia <= 50:
        return bmi * 1.1  # Penyesuaian kecil untuk usia dewasa
    else:
        return bmi * 1.2  # Penyesuaian lebih besar untuk lansia

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
        @media (prefers-color-scheme: light) {
            body { background-color: #F8F9FA; color: #212529; font-family: 'Arial', sans-serif; }
            .stButton button { background-color: #007BFF; color: white; border-radius: 5px; font-weight: bold; }
            .stButton button:hover { background-color: #0056b3; }
        }
        @media (prefers-color-scheme: dark) {
            body { background-color: #121212; color: #EAEAEA; font-family: 'Arial', sans-serif; }
            .stButton button { background-color: #1F7A8C; color: white; border-radius: 5px; font-weight: bold; }
            .stButton button:hover { background-color: #145366; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Halaman Home
def home_page():
    st.markdown("<h1 style='text-align: center;'>Kalkulator BMI dengan Penyesuaian Usia</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Hitung BMI Anda dengan penyesuaian berdasarkan usia untuk hasil yang lebih akurat.</p>", unsafe_allow_html=True)
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
        **BMI (Body Mass Index)** adalah ukuran yang digunakan untuk menilai apakah berat badan seseorang 
        sesuai dengan tinggi badannya. BMI dihitung dengan membagi berat badan (dalam kilogram) dengan kuadrat tinggi badan 
        (dalam meter).

        ### Pengaruh Usia terhadap BMI
        Dengan bertambahnya usia, komposisi tubuh berubah. Oleh karena itu, nilai BMI perlu disesuaikan agar lebih relevan.

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
    st.markdown("<h1 style='text-align: center;'>Kalkulator BMI</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Input data
    tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0, format="%.2f", key="tinggi")
    berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0, format="%.2f", key="berat")
    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ('Pria', 'Wanita'), key="jenis_kelamin")
    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=1, format="%d", key="usia")

    if st.button("Hitung BMI 🧮"):
        if tinggi <= 0 or berat <= 0 or usia <= 0:
            st.error("Pastikan semua input telah diisi dengan benar!")
        else:
            # Hitung BMI dan berat badan ideal
            bmi = hitung_bmi(berat, tinggi)
            bmi_disesuaikan = sesuaikan_bmi_berdasarkan_usia(bmi, usia)
            berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
            kategori = kategori_bmi(bmi_disesuaikan)

            # Tampilkan hasil
            st.markdown("### Hasil Perhitungan")
            st.markdown(f"- **Berat Badan Ideal Anda:** `{berat_ideal:.2f} kg`")
            st.markdown(f"- **BMI Anda:** `{bmi:.2f}`")
            st.markdown(f"- **BMI Setelah Penyesuaian Usia:** `{bmi_disesuaikan:.2f}`")
            st.markdown(f"- **Kategori Berat Badan Anda:** `{kategori}`")

            # Tampilan kategori
            if kategori == "Kurus":
                st.warning("Kategori: Kurus. Perhatikan asupan nutrisi untuk mencapai berat badan ideal.")
            elif kategori == "Normal":
                st.success("Kategori: Normal. Selamat, Anda memiliki berat badan yang ideal!")
            elif kategori == "Gemuk":
                st.warning("Kategori: Gemuk. Mulailah pola makan sehat dan olahraga teratur.")
            else:
                st.error("Kategori: Obesitas. Disarankan untuk berkonsultasi dengan ahli gizi atau dokter.")

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
