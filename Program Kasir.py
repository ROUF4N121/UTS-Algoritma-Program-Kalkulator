class Item:
    def __init__(self, nama, harga, jumlah):
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

    def total_harga(self):
        return self.harga * self.jumlah


class Keranjang:
    def __init__(self):
        self.items = []

    def add_item(self, nama, harga, jumlah):
        item = Item(nama, harga, jumlah)
        self.items.append(item)

    def display_items(self):
        if not self.items:
            print("Keranjang masih kosong.")
        else:
            print("Daftar Barang dalam Keranjang:")
            for index, item in enumerate(self.items, start=1):
                print(f"{index}. {item.nama} - {item.jumlah} x Rp{item.harga} = Rp{item.total_harga()}")

    def calculate_total(self):
        return sum(item.total_harga() for item in self.items)

    def print_receipt(self):
        print("\nStruk Belanja")
        print("=" * 20)
        self.display_items()
        print("=" * 20)
        print(f"Total Harga: Rp{self.calculate_total()}")
        print("Terima kasih sudah berbelanja!\n")


def main():
    cart = Keranjang()

    while True:
        print("\nPilih opsi:")
        print("1. Tambah barang ke keranjang")
        print("2. Tampilkan daftar barang")
        print("3. Hitung total harga")
        print("4. Cetak struk")
        print("5. Keluar")
        
        choice = input("Masukkan pilihan (1-5): ")

        if choice == '1':
            nama = input("Masukkan nama barang: ")
            harga = float(input("Masukkan harga barang: "))
            jumlah = int(input("Masukkan jumlah barang: "))
            cart.add_item(nama, harga, jumlah)
            print(f"{nama} berhasil ditambahkan ke keranjang.")

        elif choice == '2':
            cart.display_items()

        elif choice == '3':
            total = cart.calculate_total()
            print(f"Total harga: Rp{total}")

        elif choice == '4':
            cart.print_receipt()

        elif choice == '5':
            print("Terima kasih! Program berakhir.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
