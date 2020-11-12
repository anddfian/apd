import os
import time
import random

biodata = []
mahasiswa = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("-----------------------------------------------")
    print("\t\tAplikasi X")
    print("\tDibuat oleh Andi Alfian Bahtiar")
    print("-----------------------------------------------")
    print("[1] Biodata SIM C")
    print("[2] Daftar Mahasiswa")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        biodata_ktp()
    elif(selected_menu == "2"):
        daftar_mahasiswa()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
        
def close_app():
    clear_screen()
    print("-------------------------------------------------------------")
    print("\tTerima kasih telah menggunakan Aplikasi X")
    print("-------------------------------------------------------------")
    time.sleep(3)
    exit()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()
    
def back_to_menu_mahasiswa():
    print("\n")
    input("Tekan Enter untuk kembali...")
    daftar_mahasiswa()

def biodata_ktp():
    clear_screen()
    print("------------------------------")
    print("Biodata SIM C")
    print("------------------------------")
    nama = str(input("Masukkan Nama Anda: "))
    biodata.insert(0,nama)
    alamat = str(input("Masukkan Alamat Anda: "))
    biodata.insert(1,alamat)
    ttl = str(input("Masukkan Tempat, Tanggal Lahir Anda: "))
    biodata.insert(2,ttl)
    tinggi = float(input("Masukkan Tinggi Anda: "))
    biodata.insert(3,tinggi)
    pekerjaan = str(input("Masukkan Pekerjaan Anda: "))
    biodata.insert(4,pekerjaan)
    print("Mohon Tunggu Sebentar...")
    time.sleep(5)
    clear_screen()
    print("------------------------------")
    print("Biodata SIM C")
    print("------------------------------")
    print("Nama: %s" % (biodata[0]))
    print("Alamat: %s" % (biodata[1]))
    print("Tempat, Tanggal Lahir: %s" % (biodata[2]))
    print("Tinggi: %0.1f" % (biodata[3]))
    print("Pekerjaan: %s" % (biodata[4]))
    print("No. SIM: 00%d" % (random.randint(1,9)))
    print("Berlaku s/d: 12/11/2025")
    print("Samarinda, 12/11/2020")
    print("KAPOLRESTA - AKBP. Andi Alfian Bahtiar")
    back_to_menu()

def daftar_mahasiswa():
    clear_screen()
    print("------------------------------")
    print("Daftar Mahasiswa")
    print("------------------------------")
    print("[1] Tambah Data")
    print("[2] Tampilkan Data")
    print("[3] Kembali")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        tambah_daftar_mahasiswa()
    elif(selected_menu == "2"):
        hasil_daftar_mahasiswa()
    elif (selected_menu == "3"):
        show_menu()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
    

def tambah_daftar_mahasiswa():
    nama = str(input("Masukkan Nama Mahasiswa: "))
    mahasiswa.insert(0,nama)
    nim = int(input("Masukkan NIM Mahasiswa: "))
    mahasiswa.insert(1,nim)
    alamat = str(input("Masukkan Alamat Mahasiswa: "))
    mahasiswa.insert(2,alamat)
    no_hp = int(input("Masukkan No HP Mahasiswa: "))
    mahasiswa.insert(3,no_hp)
    print("Mohon Tunggu Sebentar...")
    time.sleep(5)
    print("Data Berhasil Ditambahkan!")
    back_to_menu_mahasiswa()

def hasil_daftar_mahasiswa():
    if len(mahasiswa) <= 0:
        print("Data Belum Tersedia")
        back_to_menu_mahasiswa()
    else:
        print("Nama: %s" % (mahasiswa[0]))
        print("NIM: %d" % (mahasiswa[1]))
        print("Alamat: %s" % (mahasiswa[2]))
        print("No HP: %d" % (mahasiswa[3]))
        back_to_menu_mahasiswa()

if __name__ == "__main__":
    while True:
        show_menu()
