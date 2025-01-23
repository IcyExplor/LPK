import streamlit as st

def hitung_bmi(berat, tinggi):
    tinggi_meter = tinggi / 100  # Mengubah tinggi dari cm ke meter
    bmi = berat / (tinggi_meter ** 2)
    return bmi

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Gemuk"
    else:
        return "Obesitas"

def rekomendasi(usia, jenis_kelamin):
    if usia >= 18:
        if jenis_kelamin == "Pria":
            return "Untuk pria, pastikan diet seimbang dan rutin berolahraga."
        else:
            return "Untuk wanita, pastikan konsumsi makanan bergizi dan perhatikan pola makan."
    else:
        return "Untuk usia di bawah 18, konsultasikan dengan dokter atau ahli gizi untuk rekomendasi yang tepat."

def kalkulator_bmi():
    print("Selamat datang di Kalkulator BMI!")
    
    # Input dari pengguna
    berat = float(input("Masukkan berat badan (kg): "))
    tinggi = float(input("Masukkan tinggi badan (cm): "))
    usia = int(input("Masukkan usia (tahun): "))
    jenis_kelamin = input("Masukkan jenis kelamin (Pria/Wanita): ").capitalize()
    
    # Hitung BMI
    bmi = hitung_bmi(berat, tinggi)
    print(f"BMI Anda adalah: {bmi:.2f}")
    
    # Kategori BMI
    kategori = kategori_bmi(bmi)
    print(f"Kategori BMI Anda: {kategori}")
    
    # Rekomendasi berdasarkan usia dan jenis kelamin
    print(rekomendasi(usia, jenis_kelamin))

# Menjalankan kalkulator BMI
kalkulator_bmi()
