import streamlit as st

# Inisialisasi session state untuk mengontrol tampilan
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi untuk berpindah ke tampilan berikutnya
def next_page():
    st.session_state.page = "next_page"

# Fungsi untuk kembali ke halaman utama
def go_home():
    st.session_state.page = "home"

# Fungsi untuk menuju halaman penjelasan BMI
def go_to_explanation():
    st.session_state.page = "explanation"

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

# Home Page
if st.session_state.page == "home":
    # Title dengan Markdown Styling dan animasi sederhana
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1; animation: fadeIn 2s;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        <style>
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Menyisipkan gambar dari URL dengan efek hover
    image_url = "https://static.vecteezy.com/system/resources/previews/016/828/833/original/bmi-classification-chart-measurement-woman-colorful-infographic-with-ruler-female-body-mass-index-scale-collection-from-underweight-to-overweight-fit-person-different-weight-level-eps-vector.jpg"
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="{image_url}" style="width: 100%; max-width: 600px; border-radius: 15px; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<p style='text-align: center; color: #5D6D7E;'>BMI Calculator</p>", unsafe_allow_html=True)

    # Subtitle dengan Markdown Styling
    st.markdown(
        """
        <h3 style='text-align: center; color: #5D6D7E;'>
            Solusi Praktis Untuk Pemantauan Kesehatan
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Garis pemisah untuk estetika
    st.markdown("---")

    # List kontributor dengan styling menarik
    st.markdown(
        """
        <h2 style='text-align: center; color: #2E86C1;'>
             Kelompok 5 
        </h2>
        <p style='text-align: Left; color: #5D6D7E;'>
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

    # Garis pemisah di akhir
    st.markdown("---")
