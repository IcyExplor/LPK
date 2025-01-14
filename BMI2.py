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

    # Tombol "Next" untuk berpindah ke tampilan berikutnya
    st.button("Next ➡️", on_click=next_page)
    
# Tampilan Berikutnya
elif st.session_state.page == "next_page":
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        <h3 style='text-align: center; color: #5D6D7E;'>
            Silakan masukkan data Anda untuk menghitung BMI.
        </h3>
        """,
        unsafe_allow_html=True
    )

# Garis pemisah
    st.markdown("---")
    while True:
    try:
        # Input tinggi badan
        tinggi = float(input("\033[1;33mMasukkan tinggi badan Anda (cm): \033[0m"))
        if tinggi <= 0:
            print("\033[1;31mTinggi badan harus lebih dari 0 cm.\033[0m")
            continue
        
        # Input berat badan
        berat = float(input("\033[1;33mMasukkan berat badan Anda (kg): \033[0m"))
        if berat <= 0:
            print("\033[1;31mBerat badan harus lebih dari 0 kg.\033[0m")
            continue
        
        # Input jenis kelamin
        jenis_kelamin = input("\033[1;33mMasukkan jenis kelamin Anda (pria/wanita): \033[0m").lower()
        if jenis_kelamin not in ['pria', 'wanita']:
            print("\033[1;31mJenis kelamin tidak valid. Masukkan 'pria' atau 'wanita'.\033[0m")
            continue
        
        # Hitung berat ideal, BMI, dan kategori
        berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
        bmi = hitung_bmi(berat, tinggi)
        kategori = kategori_bmi(bmi)
        
        # Tampilkan hasil
        print("\n\033[1;32m=== HASIL PERHITUNGAN ===\033[0m")
        print(f"\033[1;34mBerat Badan Ideal Anda: {berat_ideal:.2f} kg\033[0m")
        print(f"\033[1;34mIndeks Massa Tubuh (BMI): {bmi:.2f}\033[0m")
        print(f"\033[1;34mKategori Berat Badan: {kategori}\033[0m")

        # Tampilkan grafik BMI
        tampilkan_grafik_bmi()

        # Berikan saran berdasarkan kategori BMI
        if kategori == "Kurus":
            print("\033[1;33m💡 Tips: Anda berada dalam kategori Kurus. Perhatikan asupan nutrisi dan konsultasikan dengan ahli gizi.\033[0m")
        elif kategori == "Normal":
            print("\033[1;32m🎉 Selamat! Anda berada dalam kategori Normal. Pertahankan gaya hidup sehat!\033[0m")
        elif kategori == "Gemuk":
            print("\033[1;33m💡 Tips: Anda berada dalam kategori Gemuk. Mulailah pola hidup sehat dan olahraga teratur.\033[0m")
        else:
            print("\033[1;31m⚠️ Perhatian: Anda berada dalam kategori Obesitas. Segera konsultasikan dengan dokter atau ahli gizi.\033[0m")

        # Tanya pengguna apakah ingin mengulang
        ulangi = input("\033[1;35mApakah Anda ingin menghitung lagi? (ya/tidak): \033[0m").lower()
        if ulangi != 'ya':
            print("\033[1;36mTerima kasih telah menggunakan aplikasi ini! 😊\033[0m")
            break

    except ValueError:
        print("\033[1;31mInput tidak valid. Harap masukkan angka untuk tinggi dan berat badan.\033[0m")
        
    # Tombol "Kembali" untuk kembali ke tampilan awal
    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"
