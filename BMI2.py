import streamlit as st

# Constants
PAGES = {
    "home": "Home",
    "next_page": "Next Page"
}

# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Functions for page navigation
def next_page():
    st.session_state.page = "next_page"

def go_home():
    st.session_state.page = "home"

# Functions for BMI and ideal weight calculations
def calculate_ideal_weight(height, gender):
    """Calculate ideal weight based on height and gender."""
    if gender == 'Pria':
        return 0.9 * (height - 100)
    return 0.85 * (height - 100)

def calculate_bmi(weight, height):
    """Calculate BMI using weight and height."""
    return weight / ((height / 100) ** 2)

def get_bmi_category(bmi):
    """Determine BMI category based on BMI value."""
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    return "Obesitas"

# Home Page
if st.session_state.page == "home":
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1; animation: fadeIn 2s;'>
            Aplikasi Pengukur Body Mass Index (BMI)
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Input fields for height, weight, and gender
    height = st.number_input("Tinggi Badan (cm)", min_value=100, max_value=250, value=170)
    weight = st.number_input("Berat Badan (kg)", min_value=30, max_value=200, value=70)
    gender = st.radio("Jenis Kelamin", ['Pria', 'Wanita'])

    # Calculate BMI and ideal weight
    if st.button("Hitung BMI"):
        bmi = calculate_bmi(weight, height)
        ideal_weight = calculate_ideal_weight(height, gender)
        bmi_category = get_bmi_category(bmi)

        # Display results
        st.write(f"BMI Anda: {bmi:.2f}")
        st.write(f"Kategori BMI: {bmi_category}")
        st.write(f"Berat Badan Ideal: {ideal_weight:.2f} kg")

    # Button to navigate to the next page
    if st.button("Lanjut ke Halaman Berikutnya"):
        next_page()

# Next Page
elif st.session_state.page == "next_page":
    st.markdown(
        """
        <h1 style='text-align: center; color: #2E86C1; animation: fadeIn 2s;'>
            Penjelasan tentang BMI
        </h1>
        """,
        unsafe_allow_html=True
    )

    # Explanation about BMI
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
