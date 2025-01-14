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

# Home Page
if st.session_state.page == "home":
    # Title dengan Markdown Styling dan animasi sederhana
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1; animation: fadeIn 2s;'>
            🏋️‍♂️ Aplikasi Pengukur Body Mass Index (BMI) 🏋️‍♀️
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
    st.markdown("<p style='text-align: center; color: #5D6D7E;'>Ilustrasi Kesehatan</p>", unsafe_allow_html=True)

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
            🧑‍💻 Kelompok 5 🧑‍💻
        </h2>
        <p style='text-align: center; color: #5D6D7E;'>
            Anggota: <br>
            - Nama Anggota 1 <br>
            - Nama Anggota 2 <br>
            - Nama Anggota 3 <br>
        </p>
        """,
        unsafe_allow_html=True
    )

    # Tombol untuk melanjutkan ke halaman berikutnya
    st.markdown(
        """
        <div style="text-align: center;">
            <button style="background-color: #2E86C1; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
                Mulai Sekarang
            </button>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.button("Mulai Sekarang", key="start_button"):
        next_page()

# Halaman berikutnya (Next Page)
elif st.session_state.page == "next_page":
    # Judul halaman berikutnya
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1;'>
            🧮 Hitung BMI Anda
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Input untuk berat badan dan tinggi badan
    berat = st.number_input("Masukkan Berat Badan (kg):", min_value=0.0, format="%.2f")
    tinggi = st.number_input("Masukkan Tinggi Badan (cm):", min_value=0.0, format="%.2f")

    # Tombol untuk menghitung