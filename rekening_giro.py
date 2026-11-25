# Nama: Ardian Subakti
# NIM: 25552011083

from rekening import Rekening

class RekeningGiro(Rekening):
    def __init__(self, nomor_rekening, nama_pemilik, saldo=0, limit_overdraft=500000, biaya_transaksi=2500, status_giro="Aktif"):
        # Memanggil constructor superclass
        super().__init__(nomor_rekening, nama_pemilik, saldo)

        # Validasi atribut khusus
        if limit_overdraft < 0 or biaya_transaksi < 0:
            raise ValueError("Limit overdraft dan biaya transaksi tidak boleh negatif")

        # 3 atribut private khusus subclass
        self.__limit_overdraft = limit_overdraft
        self.__biaya_transaksi = biaya_transaksi
        self.__status_giro = status_giro

    # Getter untuk membaca atribut private
    def get_limit_overdraft(self):
        return self.__limit_overdraft

    def get_biaya_transaksi(self):
        return self.__biaya_transaksi

    def get_status_giro(self):
        return self.__status_giro

    # Method tambahan 1: Penarikan giro dengan memanfaatkan limit overdraft
    def tarik_dengan_overdraft(self, jumlah):
        total_kebutuhan = jumlah + self.__biaya_transaksi
        dana_tersedia = self.get_saldo() + self.__limit_overdraft

        if jumlah <= 0 or total_kebutuhan > dana_tersedia:
            return False

        # Jika saldo utama mencukupi
        if self.get_saldo() >= total_kebutuhan:
            return self.tarik(total_kebutuhan)
        else:
            # Saldo utama ditarik habis, sisanya memotong limit overdraft
            sisa_kurang = total_kebutuhan - self.get_saldo()
            self.tarik(self.get_saldo())
            self.__limit_overdraft -= sisa_kurang
            return True

    # Method tambahan 2: Menampilkan sisa informasi fasilitas overdraft
    def info_overdraft(self):
        return f"Sisa Limit Overdraft: Rp{self.__limit_overdraft:,.2f}"

    # Method tambahan 3: Menampilkan informasi lengkap rekening giro
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis Rekening : Rekening Giro")
        print(f"Limit Overdraft: Rp{self.__limit_overdraft:,.2f}")
        print(f"Biaya Transaksi: Rp{self.__biaya_transaksi:,.2f}")
        print(f"Status Rekening: {self.__status_giro}")
