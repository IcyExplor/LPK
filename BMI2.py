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
    Mengembalikan nilai BMI yang disesuaikan berdasarkan usia.
    """
    if usia < 18:
        return bmi * 0.9  # Faktor penyesuaian untuk remaja
    elif usia <= 30:
        return bmi * 1.0  # Usia dewasa muda tidak ada perubahan
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
            body { background-color: #F8F9FA; color: #212529; }
        }
        @media (prefers-color-scheme: dark) {
            body { background-color: #121212; color: #EAEAEA; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Halaman Home
def home_page():
    st.markdown("<h1 style='text-align: center;'>Aplikasi Pengukur BMI</h1>", unsafe_allow_html=True)
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
        BMI dihitung dengan membagi berat badan (kg) dengan kuadrat tinggi badan (meter).

        ### Pengaruh Usia terhadap BMI
        Dengan bertambahnya usia, komposisi tubuh berubah. Oleh karena itu, nilai BMI perlu disesuaikan agar lebih relevan.
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
    tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=0.0, format="%.2f", key="tinggi")
    berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, format="%.2f", key="berat")
    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ('Pria', 'Wanita'), key="jenis_kelamin")
    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=0, format="%d", key="usia")

    if st.button("Hitung BMI 🧮"):
        if tinggi <= 0 or berat <= 0 or usia <= 0:
            st.error("Masukkan semua data dengan benar!")
        else:
            # Hitung BMI
            bmi = hitung_bmi(berat, tinggi)
            bmi_disesuaikan = sesuaikan_bmi_berdasarkan_usia(bmi, usia)
            berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
            kategori = kategori_bmi(bmi_disesuaikan)

            # Tampilkan hasil
            st.markdown("### Hasil Perhitungan")
            st.markdown(f"- **Berat Badan Ideal Anda:** `{berat_ideal:.2f} kg`")
            st.markdown(f"- **BMI Anda:** `{bmi:.2f}`")
            st.markdown(f"- **BMI Setelah Penyesuaian Usia:** `{bmi_disesuaikan:.2f}`")
            st.markdown(f"- **Kategori Berat Badan:** `{kategori}`")

            if kategori == "Kurus":
                st.warning("Anda berada dalam kategori Kurus. Perhatikan asupan nutrisi Anda.")
            elif kategori == "Normal":
                st.success("Selamat! Anda berada dalam kategori Normal.")
            elif kategori == "Gemuk":
                st.warning("Anda berada dalam kategori Gemuk. Mulai pola hidup sehat.")
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
