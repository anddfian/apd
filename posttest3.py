import os
import time

stock = [25,35]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("----------------------------------------")
    print("\tAplikasi Kasir Toko Sule")
    print("----------------------------------------")
    print("[1] Kasir")
    print("[2] Stock")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        kasir()
    elif (selected_menu == "2"):
        stocks()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
        
def close_app():
    clear_screen()
    print("-------------------------------------------------------------")
    print("Terima kasih telah menggunakan Aplikasi Kasir Toko Sule")
    print("-------------------------------------------------------------")
    time.sleep(3)
    exit()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()

def back_to_kasir():
    print("\n")
    input("Tekan Enter untuk kembali...")
    kasir()

def back_to_stock():
    print("\n")
    input("Tekan Enter untuk kembali...")
    stocks()

def kasir():
    clear_screen()
    print("---------------------------------------------")
    print("Menu Kue:")
    print("[1] Kue Keju Rp. 6000 (Stok: %d)" % (stock[0]))
    print("[2] Kue Coklat Rp. 3500 (Stok: %d)" % (stock[1]))
    print("Promo:")
    print("[+] Diskon 10% untuk pembelian 4-15 Kue Keju")
    print("[+] Diskon 15% untuk pembelian 16-25 Kue Keju")
    print("[+] Diskon 7% untuk pembelian 5-20 Kue Coklat")
    print("[+] Diskon 12% untuk pembelian 21-35 Kue Coklat")
    try:
        jumlah_kue_keju = int(input("Jumlah Kue Keju> "))
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        back_to_kasir()

    if(jumlah_kue_keju > stock[0]):
        print("Stok Kue Keju tidak mencukupi!")
        back_to_kasir()
    elif(jumlah_kue_keju < 0):
        print("Input salah!")
        back_to_kasir()

    try:
        jumlah_kue_coklat = int(input("Jumlah Kue Coklat> "))
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        back_to_kasir()

    if(jumlah_kue_coklat > stock[1]):
        print("Stok Kue Coklat tidak mencukupi!")
        back_to_kasir()
    elif(jumlah_kue_coklat < 0):
        print("Input salah!")
        back_to_kasir()
    
    clear_screen()
    print("---------------------------------------------")
    if(jumlah_kue_keju >= 0 and jumlah_kue_keju <= 3):
        harga = 6000*jumlah_kue_keju
        total_harga_kue_keju = harga
        print("Produk: Kue Keju\nHarga: Rp. 6000 x %d = Rp. %d" % (jumlah_kue_keju, harga))
        print("Sub Total: Rp. %d" % (total_harga_kue_keju))
    elif(jumlah_kue_keju >= 4 and jumlah_kue_keju <= 15):
        harga = 6000*jumlah_kue_keju
        diskon = 10/100
        harga_diskon_kue_keju = harga * diskon
        total_harga_kue_keju = harga-harga_diskon_kue_keju
        print("Produk: Kue Keju\nHarga: Rp. 6000 x %d = Rp. %d" % (jumlah_kue_keju, harga))
        print("Diskon: Rp. %d" % (harga_diskon_kue_keju))
        print("Sub Total: Rp. %d" % (total_harga_kue_keju))
    elif(jumlah_kue_keju >= 16 and jumlah_kue_keju <= 25):
        harga = 6000*jumlah_kue_keju
        diskon = 15/100
        harga_diskon_kue_keju = harga * diskon
        total_harga_kue_keju = harga-harga_diskon_kue_keju
        print("Produk: Kue Keju\nHarga: Rp. 6000 x %d = Rp. %d" % (jumlah_kue_keju, harga))
        print("Diskon: Rp. %d" % (harga_diskon_kue_keju))
        print("Sub Total: Rp. %d" % (total_harga_kue_keju))

    if(jumlah_kue_coklat >= 0 and jumlah_kue_coklat <= 4):
        harga = 3500*jumlah_kue_coklat
        total_harga_kue_coklat = harga
        print("Produk: Kue Coklat\nHarga: Rp. 3500 x %d = Rp. %d" % (jumlah_kue_coklat, harga))
        print("Sub Total: Rp. %d" % (total_harga_kue_coklat))
    elif(jumlah_kue_coklat >= 5 and jumlah_kue_coklat <= 20):
        harga = 3500*jumlah_kue_coklat
        diskon = 7/100
        harga_diskon_kue_coklat = harga * diskon
        total_harga_kue_coklat = harga-harga_diskon_kue_coklat
        print("Produk: Kue Coklat\nHarga: Rp. 3500 x %d = Rp. %d" % (jumlah_kue_coklat, harga))
        print("Diskon: Rp. %d" % (harga_diskon_kue_coklat))
        print("Sub Total: Rp. %d" % (total_harga_kue_coklat))
    elif(jumlah_kue_coklat >= 21 and jumlah_kue_coklat <= 35):
        harga = 3500*jumlah_kue_coklat
        diskon = 12/100
        harga_diskon_kue_coklat = harga * diskon
        total_harga_kue_coklat = harga-harga_diskon_kue_coklat
        print("Produk: Kue Coklat\nHarga: Rp. 3500 x %d = Rp. %d" % (jumlah_kue_coklat, harga))
        print("Diskon: Rp. %d" % (harga_diskon_kue_coklat))
        print("Sub Total: Rp. %d" % (total_harga_kue_coklat))
    
    total_harga_kue = total_harga_kue_keju+total_harga_kue_coklat
    print("Total: Rp. %d" % (total_harga_kue))
    try:
        bayar = float(input("Bayar> "))
    except ValueError:
        print("Ups! Itu bukan jumlah yang valid. Coba lagi...")
        back_to_kasir()

    if(bayar >= total_harga_kue):
        stock[0] -= jumlah_kue_keju
        stock[1] -= jumlah_kue_coklat
        print("Kembalian: Rp. %d" % (bayar-total_harga_kue))
        back_to_menu()
    else:
        print("Error: Uang tidak cukup!")
        back_to_kasir()

def stocks():
    clear_screen()
    print("---------------------------------------------")
    print("Stock Kue Keju: %d" % (stock[0]))
    print("Stock Kue Cokelat: %d" % (stock[1]))
    try:
        stock_kue_keju = int(input("Masukkan Jumlah Kue Keju> "))
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        back_to_stock()

    if(stock_kue_keju+stock[0] > 25):
        print("Jumlah Stock Kue Keju Hanya 25")
        back_to_menu()
    else:
        stock[0] += stock_kue_keju
        print("Stock Kue Keju menjadi: %d" % (stock[0]))

    try:
        stock_kue_coklat = int(input("Masukkan Jumlah Kue Coklat> "))
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        back_to_stock()

    if(stock_kue_coklat+stock[1] > 35):
        print("Jumlah Stock Kue Coklat Hanya 35")
        back_to_menu()
    else:
        stock[1] += stock_kue_coklat
        print("Stock Kue Coklat menjadi: %d" % (stock[1]))
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()
