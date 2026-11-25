from rekening import Rekening

class RekeningTabungan(Rekening):
    def __init__(self, nomor_rekening, nama_pemilik, saldo=0, bunga_persen=2.5, biaya_admin=5000, status_aktif=True):
        # Memanggil constructor superclass
        super().__init__(nomor_rekening, nama_pemilik, saldo)

        # Validasi atribut khusus
        if bunga_persen < 0 or biaya_admin < 0:
            raise ValueError("Bunga dan biaya admin tidak boleh negatif")

        # 3 atribut private khusus subclass
        self.__bunga_persen = bunga_persen
        self.__biaya_admin = biaya_admin
        self.__status_aktif = status_aktif

    # Getter untuk membaca atribut private
    def get_bunga_persen(self):
        return self.__bunga_persen

    def get_biaya_admin(self):
        return self.__biaya_admin

    def get_status_aktif(self):
        return self.__status_aktif

    # Method tambahan 1: Menghitung bunga dan menambahkannya ke saldo
    def hitung_dan_tambah_bunga(self):
        nominal_bunga = (self.get_saldo() * self.__bunga_persen) / 100
        if nominal_bunga > 0:
            self.setor(nominal_bunga)
            return nominal_bunga
        return 0

    # Method tambahan 2: Memotong biaya administrasi bulanan
    def potong_biaya_admin(self):
        if self.get_saldo() >= self.__biaya_admin:
            return self.tarik(self.__biaya_admin)
        return False

    # Method tambahan 3: Menampilkan informasi lengkap rekening tabungan
    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Jenis Rekening : Rekening Tabungan")
        print(f"Bunga Tahunan  : {self.__bunga_persen}%")
        print(f"Biaya Admin    : Rp{self.__biaya_admin:,.2f}")
        print(f"Status Rekening: {'Aktif' if self.__status_aktif else 'Non-Aktif'}")
