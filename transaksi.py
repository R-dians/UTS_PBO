# Nama: Ardian Subakti
# NIM: 25552011083

class Transaksi:
    def __init__(self, kode_transaksi, rekening, jenis_transaksi, jumlah):
        # Validasi nilai transaksi
        if jumlah <= 0:
            raise ValueError("Jumlah transaksi harus bernilai lebih dari 0")

        # 4 atribut private
        self.__kode_transaksi = kode_transaksi
        self.__rekening = rekening  # Relasi Association (Has-A: Transaksi merujuk ke Rekening)
        self.__jenis_transaksi = jenis_transaksi
        self.__jumlah = jumlah
        self.__status = "Pending"

    # Getter untuk membaca atribut private
    def get_kode_transaksi(self):
        return self.__kode_transaksi

    def get_rekening(self):
        return self.__rekening

    def get_jenis_transaksi(self):
        return self.__jenis_transaksi

    def get_jumlah(self):
        return self.__jumlah

    def get_status(self):
        return self.__status

    # Method tambahan 1: Memproses transaksi pada rekening terkait
    def proses_transaksi(self):
        # Jika transaksi sudah selesai, cegah proses ulang
        if self.__status == "Berhasil":
            return False

        berhasil = False
        if self.__jenis_transaksi.lower() == "setor":
            berhasil = self.__rekening.setor(self.__jumlah)
        elif self.__jenis_transaksi.lower() == "tarik":
            berhasil = self.__rekening.tarik(self.__jumlah)

        if berhasil:
            self.__status = "Berhasil"
        else:
            self.__status = "Gagal"

        return berhasil

    # Method tambahan 2: Menampilkan rincian transaksi
    def tampilkan_rincian(self):
        print("----- Rincian Transaksi -----")
        print(f"Kode Transaksi : {self.__kode_transaksi}")
        print(f"No. Rekening   : {self.__rekening.get_nomor_rekening()}")
        print(f"Nama Nasabah   : {self.__rekening.get_nama_pemilik()}")
        print(f"Jenis Transaksi: {self.__jenis_transaksi.capitalize()}")
        print(f"Nominal        : Rp{self.__jumlah:,.2f}")
        print(f"Status         : {self.__status}")
        print("-----------------------------")
