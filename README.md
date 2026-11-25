# Nama: Ardian Subakti
# NIM: 25552011083

# Aplikasi Rekening Bank Mini (Studi Kasus UTS PBO - NIM Akhir 3)

Aplikasi CLI sederhana berbasis Python yang dibangun sesuai dengan instruksi Ujian Tengah Semester (UTS) mata kuliah Pemrograman Berorientasi Objek I.

---

## 1. Struktur File Proyek
```text
UTS_PBO/
├── rekening.py           # Superclass Rekening
├── rekening_tabungan.py  # Subclass RekeningTabungan (extends Rekening)
├── rekening_giro.py      # Subclass RekeningGiro (extends Rekening)
├── transaksi.py          # Class Asosiasi Transaksi (terkait ke Rekening)
├── main.py               # Main file untuk menjalankan aplikasi CLI
└── README.md             # Dokumentasi penjelasan proyek
```

---

## 2. Pemenuhan Ketentuan Teknis UTS
1. **Class dan Object**:
   - Class dibuat sebagai blueprint (`Rekening`, `RekeningTabungan`, `RekeningGiro`, `Transaksi`).
   - Objek diinstansiasi secara dinamis melalui interaksi pengguna di `main.py`.
2. **Atribut dan Method**:
   - Setiap class domain memiliki **minimal 3 atribut private** (menggunakan prefix dua garis bawah `__`).
   - Memiliki **minimal 2 method tambahan** selain constructor.
3. **Constructor Berparameter**:
   - Setiap class memiliki `__init__()` dengan parameter wajib untuk menginisialisasi state objek.
4. **Encapsulation**:
   - Atribut dilindungi dengan nama mangling/private (`__`).
   - Pembacaan data menggunakan method getter (`get_saldo()`, `get_nomor_rekening()`, dsb.).
   - Perubahan data dikontrol melalui method dengan validasi (`setor()`, `tarik()`, `ubah_nama_pemilik()`).
5. **Inheritance**:
   - Superclass: `Rekening`
   - Subclass: `RekeningTabungan` dan `RekeningGiro`
   - Pemanggilan constructor induk menggunakan `super().__init__(...)`.
6. **Relasi Antar Kelas (Association)**:
   - Class `Transaksi` memiliki relasi association dengan `Rekening` (*Has-A relationship*).
7. **Menu Berbasis Teks (CLI)**:
   - 1. Tambah data
   - 2. Tampilkan data
   - 3. Cari data
   - 4. Ubah data
   - 5. Cek status data & transaksi
   - 6. Keluar dari program

---

## 3. Cara Menjalankan Program
Jalankan perintah berikut di terminal:
```bash
python main.py
```
