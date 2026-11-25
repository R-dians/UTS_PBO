# Nama: Ardian Subakti
# NIM: 25552011083

class Rekening:
    def __init__(self, nomor_rekening, nama_pemilik, saldo=0):
        # Validasi saldo awal agar tidak bernilai negatif
        if saldo < 0:
            raise ValueError("Saldo awal tidak boleh negatif")

        # Penerapan Enkapsulasi: 3 atribut private
        self.__nomor_rekening = nomor_rekening
        self.__nama_pemilik = nama_pemilik
        self.__saldo = saldo

    # Getter untuk membaca atribut private
    def get_nomor_rekening(self):
        return self.__nomor_rekening

    def get_nama_pemilik(self):
        return self.__nama_pemilik

    def get_saldo(self):
        return self.__saldo

    # Method tambahan 1: Mengubah nama pemilik dengan validasi
    def ubah_nama_pemilik(self, nama_baru):
        if not nama_baru or len(nama_baru.strip()) == 0:
            return False
        self.__nama_pemilik = nama_baru.strip()
        return True

    # Method tambahan 2: Menambah saldo (setor) dengan validasi
    def setor(self, jumlah):
        if jumlah <= 0:
            return False
        self.__saldo += jumlah
        return True

    # Method tambahan 3: Mengurangi saldo (tarik) dengan validasi
    def tarik(self, jumlah):
        if jumlah <= 0 or jumlah > self.__saldo:
            return False
        self.__saldo -= jumlah
        return True

    # Method tambahan 4: Menampilkan informasi rekening
    def tampilkan_info(self):
        print(f"Nomor Rekening : {self.__nomor_rekening}")
        print(f"Nama Pemilik   : {self.__nama_pemilik}")
        print(f"Saldo          : Rp{self.__saldo:,.2f}")
