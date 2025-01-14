import streamlit as st

# Inisialisasi session state untuk mengontrol tampilan
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi untuk berpindah ke tampilan berikutnya
def next_page():
    st.session_state.page = "next_page"

# Tampilan Home
if st.session_state.page == "home":
    # Judul aplikasi dengan styling menggunakan markdown
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        <h3 style='text-align: center; color: #5D6D7E;'>
            Solusi Praktis Untuk Pemantauan Kesehatan
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Garis pemisah untuk estetika
    st.markdown("---")

    # Display an image (replace 'image_url' with the actual image URL or file path)
    st.markdown(
        """
        <div style='text-align: center; margin-top: 20px; margin-bottom: 20px;'>
            <img src='https://static.vecteezy.com/system/resources/previews/016/828/833/original/bmi-classification-chart-measurement-woman-colorful-infographic-with-ruler-female-body-mass-index-scale-collection-from-underweight-to-overweight-fit-person-different-weight-level-eps-vector.jpg' alt='Team Photo' style='border-radius: 10px; width: 100%; max-width: 400px;'>
        </div>
        """,
        unsafe_allow_html=True
    )

    # List kontributor dengan styling menarik
    st.markdown(
        """
        <h2 style='text-align: center; color: #2E86C1;'>
            🧑‍💻 Kelompok 5 🧑‍💻
        </h2>
        """,
        unsafe_allow_html=True
    )

    # Daftar kontributor dengan bullet points dan warna teks
    contributors = [
        "Dwinta Syafa Salsabilla (2350086)",
        "Fasya Anindya Zahrani (2350089)",
        "Ilman Hakim Muhardian (2350099)",
        "Muthia Ammara Shafira (2350113)",
        "Zahid Nashrulloh Khoerudin (2350141)"
    ]

    # Menampilkan daftar kontributor dengan styling
    st.markdown(
        """
        <div style='background-color: #0e1117; padding: 10px; border-radius: 10px;'>
            <ul style='color: #2E86C1; font-size: 16px;'>
        """ +
        "".join([f"<li>{contributor}</li>" for contributor in contributors]) +
        """
            </ul>
        </div>
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

    # Form input untuk menghitung BMI
    with st.form("bmi_form"):
        st.write("Masukkan data Anda:")
        weight = st.number_input("Berat Badan (kg)", min_value=0.0, format="%.2f")
        height = st.number_input("Tinggi Badan (cm)", min_value=0.0, format="%.2f")
        submitted = st.form_submit_button("Hitung BMI")

        if submitted:
            if weight > 0 and height > 0:
                height_in_meters = height / 100
                bmi = weight / (height_in_meters ** 2)
                st.success(f"BMI Anda adalah: {bmi:.2f}")
            else:
                st.error("Masukkan berat dan tinggi yang valid!")

    # Tombol "Kembali" untuk kembali ke tampilan awal
    if st.button("⬅️ Kembali"):
        st.session_state.page = "home"

# YANG PENTING KELAR

def hitung_berat_badan_ideal(tinggi, jenis_kelamin):
    """
    Menghitung berat badan ideal berdasarkan tinggi dan jenis kelamin.

    :param tinggi: Tinggi badan dalam cm (float)
    :param jenis_kelamin: Jenis kelamin ('pria' atau 'wanita') (str)
    :return: Berat badan ideal (float)
    """
    if jenis_kelamin.lower() == 'pria':
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.10)
    elif jenis_kelamin.lower() == 'wanita':
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.15)
    else:
        return None
    return berat_ideal


def hitung_bmi(berat, tinggi):
    """
    Menghitung BMI (Body Mass Index) berdasarkan berat dan tinggi.

    :param berat: Berat badan dalam kg (float)
    :param tinggi: Tinggi badan dalam cm (float)
    :return: Nilai BMI (float)
    """
    tinggi_meter = tinggi / 100
    bmi = berat / (tinggi_meter ** 2)
    return bmi


def kategori_bmi(bmi):
    """
    Menentukan kategori BMI berdasarkan nilai BMI.

    :param bmi: Nilai BMI (float)
    :return: Kategori BMI (str)
    """
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"


def tampilkan_grafik_bmi():
    """
    Menampilkan grafik kategori BMI dalam bentuk ASCII.
    """
    print("\n\033[1;36m=== GRAFIK KATEGORI BMI ===\033[0m")
    print("\033[1;34mKurus: BMI < 18.5\033[0m")
    print("\033[1;32mNormal: 18.5 <= BMI < 24.9\033[0m")
    print("\033[1;33mGemuk: 25 <= BMI < 29.9\033[0m")
    print("\033[1;31mObesitas: BMI >= 30\033[0m")
    print("\033[1;36m===========================\033[0m\n")


def main():
    print("\033[1;36m=============================================\033[0m")
    print("\033[1;36m|    APLIKASI PENGUKUR BERAT BADAN IDEAL    |\033[0m")
    print("\033[1;36m=============================================\033[0m")
    
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


if __name__ == "__main__":
    main()
