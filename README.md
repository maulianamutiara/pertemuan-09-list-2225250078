# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Mauliana Mutiara  
**NIM:** 2225250078  
**Kelas:** 3A

## Tujuan

Mempelajari penggunaan list dalam Python untuk menyimpan dan mengolah kumpulan data numerik. Kegiatan ini meliputi pembuatan list, akses indeks dan slicing, manipulasi elemen, pengolahan statistik sederhana, serta penyaringan nilai kelulusan.

## Struktur Program

Repository ini terdiri dari file README.md, .gitignore, folder latihan, dan folder praktik.

Folder `latihan` berisi enam program:
1. `01_buat_list.py` untuk membuat list dan menghitung banyak data.
2. `02_indeks_slicing.py` untuk mengambil elemen menggunakan indeks dan slicing.
3. `03_manipulasi_list.py` untuk mengubah, menambah, menyisipkan, dan menghapus elemen.
4. `04_agregasi_nilai.py` untuk menghitung total, rata-rata, minimum, dan maksimum.
5. `05_filter_kelulusan.py` untuk menampilkan nilai yang memenuhi batas kelulusan.
6. `06_fungsi_statistik.py` untuk membuat fungsi penghitung rata-rata.

Folder `praktik` berisi `analisis_nilai_mahasiswa.py`, yaitu program untuk menganalisis nilai mahasiswa dan menampilkan ringkasan statistik serta informasi kelulusan.

## Cara Menjalankan

Program dijalankan melalui terminal Visual Studio Code. Pastikan terminal berada di folder utama repository.

Untuk menjalankan program praktik:

```bash
python praktik/analisis_nilai_mahasiswa.py
```

Untuk menjalankan salah satu latihan, misalnya latihan pertama:

```bash
python latihan/01_buat_list.py
```

## Test Case

Pengujian dilakukan untuk memeriksa perhitungan statistik, batas kelulusan, dan penanganan list kosong.

| No. | Data | Yang Diperiksa | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `[60, 70, 80]` | Rata-rata | 70.00 | 70.00 | Sesuai |
| 2 | `[60, 70, 80]` | Minimum/maksimum | 60 / 80 | 60 / 80 | Sesuai |
| 3 | `[60, 70, 80]` | Jumlah lulus | 3 | 3 | Sesuai |
| 4 | `[59, 60, 61]` | Batas kelulusan 60 | 2 lulus | 2 lulus | Sesuai |
| 5 | `[]` | Rata-rata list kosong | Tidak error | 0 | Sesuai |

## Refleksi

Dari kegiatan ini, saya memahami bahwa list memudahkan penyimpanan dan pengolahan banyak data dalam satu variabel. Saya juga belajar menggunakan indeks dan slicing, memanipulasi elemen list, menghitung statistik sederhana, serta menggunakan fungsi untuk mengolah data. Kesalahan yang perlu diperhatikan adalah pembagian dengan nol ketika list kosong, sehingga data perlu diperiksa sebelum rata-rata dihitung.
