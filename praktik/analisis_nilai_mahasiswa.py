
# Program Analisis Nilai Mahasiswa

# Fungsi menghitung rata-rata
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Fungsi mencari nilai yang lulus
def nilai_lulus(data, batas=60):
    hasil = []
    for nilai in data:
        if nilai >= batas:
            hasil.append(nilai)
    return hasil


# Data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Analisis nilai mahasiswa
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Data nilai       : {nilai}")
print(f"Banyak data      : {len(nilai)}")
print(f"Total nilai      : {sum(nilai)}")
print(f"Rata-rata        : {rata_rata(nilai):.2f}")
print(f"Nilai minimum    : {min(nilai)}")
print(f"Nilai maksimum   : {max(nilai)}")

lulus = nilai_lulus(nilai)
print(f"Nilai yang lulus : {lulus}")
print(f"Jumlah lulus     : {len(lulus)}")
print(f"Belum lulus      : {len(nilai) - len(lulus)}")


# TEST CASE WAJIB
print("\n=== TEST CASE WAJIB ===")

# Test Case 1: Menghitung rata-rata
data1 = [60, 70, 80]
print("\nTest 1 - Rata-rata")
print(f"Data: {data1}")
print(f"Rata-rata: {rata_rata(data1):.2f}")
print("Hasil yang diharapkan: 70.00")

# Test Case 2: Nilai minimum dan maksimum
print("\nTest 2 - Minimum dan Maksimum")
print(f"Minimum: {min(data1)}")
print(f"Maksimum: {max(data1)}")
print("Hasil yang diharapkan: 60 / 80")

# Test Case 3: Jumlah mahasiswa lulus
print("\nTest 3 - Jumlah Lulus")
print(f"Jumlah lulus: {len(nilai_lulus(data1))}")
print("Hasil yang diharapkan: 3")

# Test Case 4: Batas kelulusan 60
data4 = [59, 60, 61]
print("\nTest 4 - Batas Kelulusan")
print(f"Nilai lulus: {nilai_lulus(data4)}")
print(f"Jumlah lulus: {len(nilai_lulus(data4))}")
print("Hasil yang diharapkan: 2 lulus")

# Test Case 5: List kosong
data5 = []
print("\nTest 5 - List Kosong")
print(f"Rata-rata: {rata_rata(data5)}")
print("Hasil yang diharapkan: Tidak error")
