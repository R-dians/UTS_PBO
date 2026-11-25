from rekening_tabungan import RekeningTabungan
from rekening_giro import RekeningGiro
from transaksi import Transaksi

def tampilkan_menu():
    print("\n" + "=" * 40)
    print("      APLIKASI REKENING BANK MINI      ")
    print("=" * 40)
    print("1. Tambah Data Rekening")
    print("2. Tampilkan Data Rekening")
    print("3. Cari Data Rekening")
    print("4. Ubah Data Rekening")
    print("5. Cek Status Data & Transaksi")
    print("6. Keluar dari Program")
    print("=" * 40)

def main():
    # Penyimpanan objek rekening dalam memori aplikasi
    daftar_rekening = {}
    daftar_transaksi = []
    id_transaksi_counter = 1

    # Inisialisasi data awal sebagai contoh pengujian
    rek_awal1 = RekeningTabungan("1001", "Ahmad Fauzi", 500000)
    rek_awal2 = RekeningGiro("2001", "PT Berkah Abadi", 1500000)
    daftar_rekening[rek_awal1.get_nomor_rekening()] = rek_awal1
    daftar_rekening[rek_awal2.get_nomor_rekening()] = rek_awal2

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        # ----------------------------------------------------
        # MENU 1: Tambah Data
        # ----------------------------------------------------
        if pilihan == "1":
            print("\n--- Tambah Data Rekening Baru ---")
            print("1. Rekening Tabungan")
            print("2. Rekening Giro")
            tipe = input("Pilih tipe rekening (1/2): ").strip()

            no_rek = input("Masukkan Nomor Rekening: ").strip()
            if no_rek in daftar_rekening:
                print("[Gagal] Nomor rekening sudah terdaftar!")
                continue

            nama = input("Masukkan Nama Pemilik: ").strip()
            try:
                saldo = float(input("Masukkan Saldo Awal (Rp): ").strip())
                if saldo < 0:
                    print("[Gagal] Saldo awal tidak boleh bernilai negatif.")
                    continue
            except ValueError:
                print("[Gagal] Nominal saldo harus berupa angka.")
                continue

            if tipe == "1":
                rekening_baru = RekeningTabungan(no_rek, nama, saldo)
                daftar_rekening[no_rek] = rekening_baru
                print("[Berhasil] Rekening Tabungan berhasil ditambahkan.")
            elif tipe == "2":
                rekening_baru = RekeningGiro(no_rek, nama, saldo)
                daftar_rekening[no_rek] = rekening_baru
                print("[Berhasil] Rekening Giro berhasil ditambahkan.")
            else:
                print("[Gagal] Pilihan jenis rekening tidak valid.")

        # ----------------------------------------------------
        # MENU 2: Tampilkan Data
        # ----------------------------------------------------
        elif pilihan == "2":
            print("\n--- Daftar Semua Rekening ---")
            if not daftar_rekening:
                print("Belum ada data rekening yang tersimpan.")
            else:
                for idx, (no_rek, rek) in enumerate(daftar_rekening.items(), start=1):
                    print(f"\n[Data ke-{idx}]")
                    rek.tampilkan_info()

        # ----------------------------------------------------
        # MENU 3: Cari Data
        # ----------------------------------------------------
        elif pilihan == "3":
            print("\n--- Cari Data Rekening ---")
            no_rek = input("Masukkan Nomor Rekening yang dicari: ").strip()
            if no_rek in daftar_rekening:
                print("\n[Data Ditemukan]")
                daftar_rekening[no_rek].tampilkan_info()
            else:
                print(f"[Tidak Ditemukan] Rekening dengan nomor '{no_rek}' tidak ada.")

        # ----------------------------------------------------
        # MENU 4: Ubah Data
        # ----------------------------------------------------
        elif pilihan == "4":
            print("\n--- Ubah Data Rekening ---")
            no_rek = input("Masukkan Nomor Rekening yang ingin diubah: ").strip()
            if no_rek in daftar_rekening:
                rek = daftar_rekening[no_rek]
                print(f"Nama saat ini: {rek.get_nama_pemilik()}")
                nama_baru = input("Masukkan Nama Pemilik Baru: ").strip()
                if rek.ubah_nama_pemilik(nama_baru):
                    print("[Berhasil] Nama pemilik rekening berhasil diperbarui.")
                else:
                    print("[Gagal] Nama pemilik tidak boleh kosong.")
            else:
                print(f"[Tidak Ditemukan] Rekening dengan nomor '{no_rek}' tidak ada.")

        # ----------------------------------------------------
        # MENU 5: Cek Status Data & Transaksi
        # ----------------------------------------------------
        elif pilihan == "5":
            print("\n--- Cek Status Data & Transaksi ---")
            no_rek = input("Masukkan Nomor Rekening: ").strip()
            if no_rek not in daftar_rekening:
                print(f"[Tidak Ditemukan] Rekening dengan nomor '{no_rek}' tidak ada.")
                continue

            rek = daftar_rekening[no_rek]
            print("\nStatus Rekening Terkini:")
            rek.tampilkan_info()

            print("\nFitur Transaksi:")
            print("1. Setor Tunai")
            print("2. Tarik Tunai")
            print("3. Kembali")
            opsi = input("Pilih transaksi (1-3): ").strip()

            if opsi in ("1", "2"):
                jenis = "Setor" if opsi == "1" else "Tarik"
                try:
                    jumlah = float(input(f"Masukkan jumlah {jenis} (Rp): ").strip())
                    kode_tr = f"TRX{id_transaksi_counter:03d}"
                    id_transaksi_counter += 1

                    # Membuat objek Transaksi berelasi dengan objek Rekening
                    transaksi = Transaksi(kode_tr, rek, jenis, jumlah)
                    hasil = transaksi.proses_transaksi()
                    daftar_transaksi.append(transaksi)

                    if hasil:
                        print(f"\n[Berhasil] Transaksi {jenis} sukses diproses.")
                    else:
                        print(f"\n[Gagal] Transaksi {jenis} ditolak (saldo tidak mencukupi atau jumlah tidak valid).")

                    transaksi.tampilkan_rincian()
                    print(f"Saldo akhir: Rp{rek.get_saldo():,.2f}")
                except ValueError as e:
                    print(f"[Gagal] Input salah: {e}")
            elif opsi == "3":
                continue
            else:
                print("[Gagal] Opsi tidak valid.")

        # ----------------------------------------------------
        # MENU 6: Keluar dari Program
        # ----------------------------------------------------
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan Aplikasi Rekening Bank Mini.")
            break
        else:
            print("[Perhatian] Pilihan menu tidak valid. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()
