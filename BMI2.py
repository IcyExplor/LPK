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

# Halaman Home
def home_page():
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

    st.markdown("<p style='text-align: center; color: #5D6D7E;'>BMI Calculator</p>", unsafe_allow_html=True)

    st.markdown("---")

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
        <h1 style='text-align: center; color: #2E86C1; animation: fadeIn 2s;'>
            Penjelasan tentang BMI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        ### Apa itu BMI?
        **BMI (Body Mass Index)** atau Indeks Massa Tubuh adalah ukuran yang digunakan untuk menilai apakah berat badan seseorang 
        sesuai dengan tinggi badannya. BMI dihitung dengan membagi berat badan (dalam kilogram) dengan kuadrat tinggi badan 
        (dalam meter).

        ### Rumus BMI:
        \[
        BMI = \frac{Berat\ Badan\ (kg)}{(Tinggi\ Badan\ (m))^2}
        \]

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

    st.markdown("---")

    if st.button("Kembali ke Home 🏠"):
        go_home()

# Kalkulator BMI
def kalkulator_bmi():
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        tinggi = st.number_input("Masukkan tinggi badan Anda (cm):", min_value=1.0, format="%.2f")
    with col2:
        berat = st.number_input("Masukkan berat badan Anda (kg):", min_value=1.0, format="%.2f")

    jenis_kelamin = st.radio("Masukkan jenis kelamin Anda:", ('Pria', 'Wanita'))

    if st.button("Hitung BMI 🧮"):
        if tinggi > 0 and berat > 0:
            berat_ideal = hitung_berat_badan_ideal(tinggi, jenis_kelamin)
            bmi = hitung_bmi(berat, tinggi)
            kategori = kategori_bmi(bmi)

            st.markdown("### 🎯 Hasil Perhitungan")
            st.markdown(f"**Berat Badan Ideal Anda:** `{berat_ideal:.2f} kg`")
            st.markdown(f"**Indeks Massa Tubuh (BMI):** `{bmi:.2f}`")
            st.markdown(f"**Kategori Berat Badan:** `{kategori}`")

            if kategori == "Kurus":
                st.progress(0.25)
                st.warning("💡 Anda berada dalam kategori Kurus.")
            elif kategori == "Normal":
                st.progress(0.5)
                st.success("🎉 Anda berada dalam kategori Normal.")
            elif kategori == "Gemuk":
                st.progress(0.75)
                st.warning("💡 Anda berada dalam kategori Gemuk.")
            else:
                st.progress(1.0)
                st.error("⚠️ Anda berada dalam kategori Obesitas.")

    if st.button("Kembali ke Home 🏠"):
        go_home()

# Main App Logic
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "penjelasan":
    penjelasan_bmi()
elif st.session_state.page == "kalkulator":
    kalkulator_bmi()
