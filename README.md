# Sudoku Solver


## Latar Belakang
Anda adalah Mr. Khun, saat ini Anda tergabung bersama tim Sweet & Sour untuk mencapai puncak menara. Agar dapat mencapai puncak menara, ada harus melalui serangkaian tes untuk dapat naik ke lantai selanjutnya. Saat ini Anda berada di lantai 18 dan administrator lantai tersebut, yaitu Mr. Le Leo ingin sekali menguji kecerdasan tim Anda dalam membuat strategi. Area permainan pada lantai ini dibagi menjadi 81 area, berbentuk seperti matriks berukuran 9x9. Setiap area ditandai dengan angka, dalam satu kolom maupun satu baris tidak boleh ada angka berulang (seperti pada permainan sudoku). Untuk lolos dari tes ini, tim Anda harus mengumpulkan kristal yang ada pada area bernomor 5. Anda yang bertugas sebagai light bearer (bertugas mengawasi seluruh area permainan dan memberikan petunjuk serta menyusun strategi untuk seluruh anggota tim). Anda bisa berkomunikasi dengan seluruh anggota dan melihat seluruh area permainan melalui lighthouse, tugas Anda adalah mencari tahu nomor untuk semua area permainan dan memberitahukan koordinat (x,y) area-area yang ditandai dengan nomor 5 kepada anggota tim Anda.

## Spesifikasi

#### Spesifikasi untuk program yang dibuat :
| No | Spesifikasi Program |
| ---- | ---- |
| 1 | Program dibuat dalam bahasa Python |
| 2 | Program menerima input berupa file eksternal yang berisi matriks area permainan (disediakan pada repository) dengan lambang '#' yang menandai area belum diketahui nomornya | 
| 3 | Program melengkapi area-area yang nomornya belum diketahui |
| 4 | Hasil dari sepesifikasi (3) ditulis pada command prompt/terminal dan disimpan dalam file eksternal. | 
| 5 | Tuliskan semua koordinat dari area bernomor 5, tuliskan pada command prompt/terminal dan simpan pada file eksternal yang sama dengan spesifikasi nomor (4). Koordinat dituliskan setelah area permainan |
| 6 | Program dapat membaca inputan dari gambar. **Program hanya perlu dapat membaca gambar spesifik yang ada pada repository**. Library yang digunakan adalah tesseract |
| 7 | Program diletakkan pada directory src, kemudian file pengujian diletakkan pada directory test, dan hasil pengujian berupa screenshot diletakkan pada directory result | 
| ---- | ---- |

## Requirements
1. Phyton 3.8 https://www.python.org/downloads/
2. Tesseract https://github.com/UB-Mannheim/tesseract/wiki (jangan lupa install juga dengan pip)
3. PIL (pip install PIL)

## How to Use
1. Buka CMD dan pergi ke direktori anda menyimpan main.py
2. buka main.py dengan command : "py main.py"

## Strategi dan Kompleksitas Algoritma:

Strategi yang saya gunakan disini adalah algoritma backtracking dengan pendekatan sederhana. Saya mencoba semua konfigurasi dari sudoku yang mungkin hingga ada solusi yang ditemukan, dengan mencoba meletakkan angka satu persatu pada sel yang kosong dan bisa diletakkan (tidak ada yang sebaris, sekolom dan sekotak 3x3). Saya memilih penggunaan algoritma ini karena pernah diajarkan dan praktis digunakan.

Komplekstitas Waktu: O(9^(n*n)).
Kompleksitas Ruang: O(n*n)

## Library yang digunakan:
Library yang saya gunakan adalah Tesseract. Menurut saya, library ini sangat praktis untuk digunakan, namun sayangnya sangat sensitif dalam pre-processing sehingga kadang merepotkan untuk cropping gambar sudoku tersebut.

## Referensi:
1. https://www.geeksforgeeks.org/sudoku-backtracking-7/
2. https://github.com/UB-Mannheim/tesseract/wiki

