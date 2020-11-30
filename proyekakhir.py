#
#     /$$$$$$   /$$$$$$  /$$    /$$ /$$$$$$ /$$$$$$$          /$$    /$$$$$$ 
#    /$$__  $$ /$$__  $$| $$   | $$|_  $$_/| $$__  $$       /$$$$   /$$__  $$
#   | $$  \__/| $$  \ $$| $$   | $$  | $$  | $$  \ $$      |_  $$  | $$  \ $$
#   | $$      | $$  | $$|  $$ / $$/  | $$  | $$  | $$ /$$$$$$| $$  |  $$$$$$$
#   | $$      | $$  | $$ \  $$ $$/   | $$  | $$  | $$|______/| $$   \____  $$
#   | $$    $$| $$  | $$  \  $$$/    | $$  | $$  | $$        | $$   /$$  \ $$
#   |  $$$$$$/|  $$$$$$/   \  $/    /$$$$$$| $$$$$$$/       /$$$$$$|  $$$$$$/
#    \______/  \______/     \_/    |______/|_______/       |______/ \______/ 
#
#//--------------------------------[MAIN DETEKSI.PY]--------------------------------
#
#							Deteksi Dini Mandiri COVID-19
#				(created by Deteksi Dini Mandiri COVID-19 Team)
#
#
#				Credits to alternate sources
# *
# * Copyright (c) 2020, Deteksi Dini Mandiri COVID-19
# *
# * All rights reserved.
# *
# * Redistribution and use in source and binary forms, with or without modification,
# * are not permitted in any case.
# *
# *
# * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# * "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# * LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# * A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# * LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import time
import datetime
import csv

data_akun = []
data_deteksi = ['','','','','','','','']

csv_filename_account = 'account.csv'
csv_filename_covid = 'covid.csv'
csv_filename_deteksi = 'deteksi.csv'
txt_filename_deteksi = 'deteksi.txt'
csv_filename_kritiksaran = 'kritiksaran.csv'

def check_file():
    if not os.path.exists(csv_filename_account):
        with open(csv_filename_account, 'w') as csv_file:
            akuns = []
            fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in akuns:
                writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
    if not os.path.exists(csv_filename_covid):
        with open(csv_filename_covid, 'w') as csv_file:
            covids = []
            fieldnames = ['JENIS','TANGGAL','TERKONFIRMASI','KASUS_AKTIF','SEMBUH','MENINGGAL','SUSPEK','DISCARDED','PROBABLE','MENUNGGU_HASIL_LAB']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in covids:
                writer.writerow({'JENIS': new_data['JENIS'], 'TANGGAL': new_data['TANGGAL'], 'TERKONFIRMASI': new_data['TERKONFIRMASI'], 'KASUS_AKTIF': new_data['KASUS_AKTIF'], 'SEMBUH': new_data['SEMBUH'], 'MENINGGAL': new_data['MENINGGAL'], 'SUSPEK': new_data['SUSPEK'], 'DISCARDED': new_data['DISCARDED'], 'PROBABLE': new_data['PROBABLE'], 'MENUNGGU_HASIL_LAB': new_data['MENUNGGU_HASIL_LAB']})
    if not os.path.exists(csv_filename_deteksi):
        with open(csv_filename_deteksi, 'w') as csv_file:
            deteksis = []
            fieldnames = ['NO', 'TIMESTAMP', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2', 'STATUS', 'KETERANGAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in deteksis:
                writer.writerow({'NO': new_data['NO'], 'TIMESTAMP': new_data['TIMESTAMP'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2'], 'STATUS': new_data['STATUS'], 'KETERANGAN': new_data['KETERANGAN']})
    if not os.path.exists(txt_filename_deteksi):
        with open(txt_filename_deteksi, 'w') as csv_file:
            file_detekesi = open(txt_filename_deteksi, "w")
            file_detekesi.write("1")
            file_detekesi.close()
    if not os.path.exists(csv_filename_kritiksaran):
        with open(csv_filename_kritiksaran, 'w') as csv_file:
            krisan = []
            fieldnames = ['JENIS','NAMA','KRITIK','SARAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in krisan:
                writer.writerow({'JENIS': new_data['JENIS'], 'NAMA': new_data['NAMA'], 'KRITIK': new_data['KRITIK'], 'SARAN': new_data['SARAN']})

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_auth():
    clear_screen()
    print("========================================================================")
    print("|                            SELAMAT DATANG                            |")
    print("|                                  DI                                  |")
    print("|                APLIKASI DETEKSI DINI MANDIRI COVID-19                |")
    print("|                                 OLEH                                 |")
    print("|       KELOMPOK 1 - INFORMATIKA A 2020 - UNIVERSITAS MULAWARMAN       |")
    print("========================================================================")
    print("| [1] Daftar Akun                                                      |")
    print("| [2] Masuk Akun                                                       |")
    print("| [0] Keluar Aplikasi                                                  |")
    print("========================================================================")
    selected_login = str(input("Masukkan Pilihan> "))
    if(selected_login == "1"):
        auth_register()
    elif(selected_login == "2"):
        show_login()
    elif(selected_login == "0"):
        close_app()
    else:
        print("========================================================================")
        print("| Error: Pilihan salah!                                                |")
        print("========================================================================")
        back_to_auth()

def auth_register():
    clear_screen()
    print("========================================================================")
    print("|                              DAFTAR AKUN                             |")
    print("========================================================================")
    print("| [1] Isi Biodata                                                      |")
    print("| [2] Kembali                                                          |")
    print("========================================================================")
    selected_register = str(input("Masukkan Pilihan> "))
    if(selected_register == "1"):
        clear_screen()
        print("========================================================================")
        print("|                              DAFTAR AKUN                             |")
        print("========================================================================")
        print("| Info: Silakan isi Nama, Umur, No. HP, Alamat, Kelurahan / Desa,      |")
        print("|       Username, Password, dan Kode Unik (jika ada) akun anda         |")
        print("========================================================================")
        nama = str(input("Nama                   : "))
        if(len(nama) < 1):
            print("========================================================================")
            print("| Error: Anda tidak dapat mengkosongkan nama                           |")
            print("========================================================================")
            back_to_auth_register()
        try:
            umur = int(input("Umur (Contoh: 18)      : "))
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            back_to_auth_register()
        try:
            nohp = int(input("No. HP/WA              : "))
        except ValueError:
            print("========================================================================")
            print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
            print("========================================================================")
            back_to_auth_register()
        alamat = str(input("Alamat                 : "))
        if(len(alamat) < 1):
            print("========================================================================")
            print("| Error: Anda tidak dapat mengkosongkan alamat                         |")
            print("========================================================================")
            back_to_auth_register()
        alamat2 = str(input("Kelurahan / Desa       : "))
        if(len(alamat2) < 1):
            print("========================================================================")
            print("| Error: Anda tidak dapat mengkosongkan kelurahan / desa               |")
            print("========================================================================")
            back_to_auth_register()
        username = str(input("Username               : "))
        if(len(username) < 4):
            print("========================================================================")
            print("| Error: Username minimal 4 huruf/angka!                               |")
            print("========================================================================")
            back_to_auth_register()
        password = str(input("Password               : "))
        if(len(password) < 8):
            print("========================================================================")
            print("| Error: Password minimal 8 huruf/angka!                               |")
            print("========================================================================")
            back_to_auth_register()
        kodeunik = str(input("Kode Unik (jika ada)   : "))
        akun = []
        with open(csv_filename_account, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                akun.append(row)
        data_found = []
        indeks = 0
        for data in akun:
            if (data['USERNAME'] == username):
                data_found = akun[indeks]
            indeks = indeks + 1
            if(len(data_found) > 0):
                print("========================================================================")
                print("| Error: Akun tersebut telah didaftarkan!                              |")
                print("========================================================================")
                back_to_auth()
        with open(csv_filename_account, mode='a') as csv_file:
            fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if(kodeunik == "admin"):
                writer.writerow({'USERNAME': username, 'PASSWORD': password, 'LEVEL': 'admin', 'NAMA': nama, 'UMUR': umur, 'NOHP': nohp, 'ALAMAT': alamat, 'ALAMAT2': alamat2})
            elif(kodeunik == "dinkes"):
                writer.writerow({'USERNAME': username, 'PASSWORD': password, 'LEVEL': 'dinkes', 'NAMA': nama, 'UMUR': umur, 'NOHP': nohp, 'ALAMAT': alamat, 'ALAMAT2': alamat2})
            else:
                writer.writerow({'USERNAME': username, 'PASSWORD': password, 'LEVEL': 'user', 'NAMA': nama, 'UMUR': umur, 'NOHP': nohp, 'ALAMAT': alamat, 'ALAMAT2': alamat2})
        print("========================================================================")
        print("| Sukses: Akun berhasil dibuat dan disimpan!                           |")
        print("========================================================================")
        back_to_login()
    elif(selected_register == "2"):
        show_auth()
    else:
        print("========================================================================")
        print("| Error: Pilihan salah!                                                |")
        print("========================================================================")
        back_to_auth_register()

def back_to_auth():
    input("\nTekan Enter untuk kembali...")
    show_auth()

def back_to_auth_register():
    input("\nTekan Enter untuk kembali...")
    auth_register()

def show_login():
    clear_screen()
    print("======================================================================")
    print("|                                LOGIN                               |")
    print("======================================================================")
    print("| [1] Guest                                                          |")
    print("| [2] User                                                           |")
    print("| [3] Dinkes                                                         |")
    print("| [4] Admin                                                          |")
    print("| [5] Kembali                                                        |")
    print("| [0] Keluar Aplikasi                                                |")
    print("======================================================================")
    selected_login = str(input("Masukkan Pilihan> "))
    if(selected_login == "1"):
        data_akun.insert(0,"guest")
        print("======================================================================")
        print("| Sukses: Anda akan dialihkan ke menu Guest                          |")
        print("======================================================================")
        time.sleep(1.5)
        show_menu()
    elif(selected_login == "2"):
        auth_login("user")
    elif(selected_login == "3"):
        auth_login("dinkes")
    elif(selected_login == "4"):
        auth_login("admin")
    elif(selected_login == "5"):
        show_auth()
    elif(selected_login == "0"):
        close_app()
    else:
        print("======================================================================")
        print("| Error: Pilihan salah!                                              |")
        print("======================================================================")
        back_to_login()

def auth_login(level):
    clear_screen()
    print("======================================================================")
    print("|               Aplikasi Deteksi Mandiri Dini COVID-19               |")
    print("======================================================================")
    print("| Info: Masukkan Username dan Password Anda                          |")
    print("======================================================================")
    akun = []
    with open(csv_filename_account, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = []
    indeks = 0
    Username = str(input("Username: "))
    Password = str(input("Password: "))
    if(level == "user"):
        for data in akun:
            if (data['USERNAME'] == Username and data['LEVEL'] == "user"):
                data_found = akun[indeks]
            indeks = indeks + 1
        if(len(data_found) > 0):
            if(data_found['PASSWORD'] == Password and data_found['LEVEL'] == "user"):
                data_akun.insert(0,"user")
                data_akun.insert(1,data_found['NAMA'])
                data_akun.insert(2,data_found['UMUR'])
                data_akun.insert(3,data_found['NOHP'])
                data_akun.insert(4,data_found['ALAMAT'])
                data_akun.insert(5,data_found['ALAMAT2'])
                data_akun.insert(6,data_found['PASSWORD'])
                print("======================================================================")
                print("| Sukses: Anda akan dialihkan ke menu User                           |")
                print("======================================================================")
                time.sleep(1.5)
                show_menu()
            else :
                print("======================================================================")
                print("| Error: Username dan Password salah!                                |")
                print("======================================================================")
                back_to_login()
        else:
            print("======================================================================")
            print("| Error: Data akun tidak ditemukan!                                  |")
            print("======================================================================")
            back_to_login()
    elif(level == "dinkes"):
        for data in akun:
            if (data['USERNAME'] == Username and data['LEVEL'] == "dinkes"):
                data_found = akun[indeks]
            indeks = indeks + 1
        if(len(data_found) > 0):
            if(data_found['PASSWORD'] == Password and data_found['LEVEL'] == "dinkes"):
                data_akun.insert(0,"dinkes")
                data_akun.insert(1,data_found['NAMA'])
                data_akun.insert(2,data_found['PASSWORD'])
                print("======================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Dinkes                         |")
                print("======================================================================")
                time.sleep(1.5)
                show_menu()
            else :
                print("======================================================================")
                print("| Error: Username dan Password salah!                                |")
                print("======================================================================")
                back_to_login()
        else:
            print("======================================================================")
            print("| Error: Data akun tidak ditemukan!                                  |")
            print("======================================================================")
            back_to_login()
    elif(level == "admin"):
        for data in akun:
            if (data['USERNAME'] == Username and data['LEVEL'] == "admin"):
                data_found = akun[indeks]
            indeks = indeks + 1
        if(len(data_found) > 0):
            if(data_found['PASSWORD'] == Password and data_found['LEVEL'] == "admin"):
                data_akun.insert(0,"admin")
                data_akun.insert(1,data_found['USERNAME'])
                data_akun.insert(2,data_found['PASSWORD'])
                print("======================================================================")
                print("| Sukses: Anda akan dialihkan ke menu Admin                          |")
                print("======================================================================")
                time.sleep(1.5)
                show_menu()
            else :
                print("======================================================================")
                print("| Error: Username dan Password salah!                                |")
                print("======================================================================")
                back_to_login()
        else:
            print("======================================================================")
            print("| Error: Data akun tidak ditemukan!                                  |")
            print("======================================================================")
            back_to_login()

def back_to_login():
    input("\nTekan Enter untuk kembali...")
    show_login()

def show_menu():
    clear_screen()
    print("======================================================================")
    print("|               APLIKASI DETEKSI DINI MANDIRI COVID-19               |")
    print("======================================================================")
    if(data_akun[0] == "guest"):
        print("| Info: Anda masuk sebagai Guest                                     |")
        print("======================================================================")
        print("| [1]  Perkembangan COVID-19 di Dunia                                |")
        print("| [2]  Perkembangan COVID-19 di Indonesia                            |")
        print("| [3]  Perkembangan COVID-19 di Provinsi Kalimantan Timur            |")
        print("| [4]  Perkembangan COVID-19 di Kota Samarinda                       |")
        print("| [5]  Cara Pencegahan COVID-19                                      |")
        print("| [6]  Call Center 10 Kab/Kota Provinsi Kalimantan Timur             |")
        print("| [7]  Rumah Sakit Rujukan COVID-19 Provinsi Kalimantan Timur        |")
        print("| [8]  Pertanyaan yang sering ditanyakan terkait COVID-19 (FAQ)      |")
        print("| [9]  Tentang Aplikasi                                              |")
        print("| [10] Kritik dan Saran                                              |")
        print("| [11] Logout                                                        |")
        print("| [0]  Keluar Aplikasi                                               |")
    elif(data_akun[0] == "user"):
        print("| Info: Anda masuk sebagai User                                      |")
        print("======================================================================")
        print("| [1]  Perkembangan COVID-19 di Dunia                                |")
        print("| [2]  Perkembangan COVID-19 di Indonesia                            |")
        print("| [3]  Perkembangan COVID-19 di Provinsi Kalimantan Timur            |")
        print("| [4]  Perkembangan COVID-19 di Kota Samarinda                       |")
        print("| [5]  Deteksi Dini Mandiri COVID-19                                 |")
        print("| [6]  Riwayat Deteksi Dini Mandiri COVID-19                         |")
        print("| [7]  Cara Pencegahan COVID-19                                      |")
        print("| [8]  Call Center 10 Kab/Kota Provinsi Kalimantan Timur             |")
        print("| [9]  Rumah Sakit Rujukan COVID-19 Provinsi Kalimantan Timur        |")
        print("| [10] Pertanyaan yang sering ditanyakan terkait COVID-19 (FAQ)      |")
        print("| [11] Tentang Aplikasi                                              |")
        print("| [12] Kritik dan Saran                                              |")
        print("| [13] Pengaturan Akun                                               |")
        print("| [14] Logout                                                        |")
        print("| [0]  Keluar Aplikasi                                               |")
    elif(data_akun[0] == "dinkes"):
        print("| Info: Anda masuk sebagai Dinkes                                    |")
        print("======================================================================")
        print("| [1]  Data Perkembangan COVID-19 di Dunia                           |")
        print("| [2]  Data Perkembangan COVID-19 di Indonesia                       |")
        print("| [3]  Data Perkembangan COVID-19 di Provinsi Kalimantan Timur       |")
        print("| [4]  Data Perkembangan COVID-19 di Kota Samarinda                  |")
        print("| [5]  Data Deteksi Dini Mandiri COVID-19                            |")
        print("| [6]  Tentang Aplikasi                                              |")
        print("| [7]  Lihat Daftar Kritik dan Saran                                 |")
        print("| [8]  Kritik dan Saran                                              |")
        print("| [9]  Pengaturan Akun                                               |")
        print("| [10] Logout                                                        |")
        print("| [0]  Keluar Aplikasi                                               |")
    elif(data_akun[0] == "admin"):
        print("| Info: Anda masuk sebagai Admin                                     |")
        print("======================================================================")
        print("| [1] Lihat Daftar Pengguna                                          |")
        print("| [2] Buat Pengguna Baru                                             |")
        print("| [3] Edit Pengguna                                                  |")
        print("| [4] Hapus Pengguna                                                 |")
        print("| [5] Cari Pengguna                                                  |")
        print("| [6] Lihat Data Deteksi Dini Mandiri COVID-19                       |")
        print("| [7] Lihat Daftar Kritik dan Saran                                  |")
        print("| [8] Pengaturan Akun                                                |")
        print("| [9] Logout                                                         |")
        print("| [0] Keluar Aplikasi                                                |")
    print("======================================================================")
    selected_menu = str(input("Pilih menu> "))
    if(data_akun[0] == "guest"):
        if(selected_menu == "1"):
            covid_dunia()
        elif(selected_menu == "2"):
            covid_indonesia()
        elif(selected_menu == "3"):
            covid_kaltim()
        elif(selected_menu == "4"):
            covid_samarinda()
        elif(selected_menu == "5"):
            pencegahan_covid()
        elif(selected_menu == "6"):
            call_center()
        elif(selected_menu == "7"):
            rs_covid()
        elif(selected_menu == "8"):
            faq_covid()
        elif(selected_menu == "9"):
            tentang_aplikasi()
        elif(selected_menu == "10"):
            kritikdansaran()
        elif(selected_menu == "11"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_menu()
    elif(data_akun[0] == "user"):
        if(selected_menu == "1"):
            covid_dunia()
        elif(selected_menu == "2"):
            covid_indonesia()
        elif(selected_menu == "3"):
            covid_kaltim()
        elif(selected_menu == "4"):
            covid_samarinda()
        elif(selected_menu == "5"):
            deteksi_pembuka()
        elif(selected_menu == "6"):
            riwayat_deteksi()
        elif(selected_menu == "7"):
            pencegahan_covid()
        elif(selected_menu == "8"):
            call_center()
        elif(selected_menu == "9"):
            rs_covid()
        elif(selected_menu == "10"):
            faq_covid()
        elif(selected_menu == "11"):
            tentang_aplikasi()
        elif(selected_menu == "12"):
            kritikdansaran()
        elif(selected_menu == "13"):
            pengaturan_akun()
        elif(selected_menu == "14"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_menu()
    elif(data_akun[0] == "dinkes"):
        if(selected_menu == "1"):
            update_data_covid("Dunia")
        elif(selected_menu == "2"):
            update_data_covid("Indonesia")
        elif(selected_menu == "3"):
            update_data_covid("Kaltim")
        elif(selected_menu == "4"):
            update_data_covid("Samarinda")
        elif(selected_menu == "5"):
            deteksi_data()
        elif(selected_menu == "6"):
            tentang_aplikasi()
        elif(selected_menu == "7"):
            show_kritiksaran()
        elif(selected_menu == "8"):
            kritikdansaran()
        elif(selected_menu == "9"):
            pengaturan_akun()
        elif(selected_menu == "10"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_menu()
    elif(data_akun[0] == "admin"):
        if(selected_menu == "1"):
            show_account()
        elif(selected_menu == "2"):
            create_account()
        elif(selected_menu == "3"):
            edit_account()
        elif(selected_menu == "4"):
            delete_account()
        elif(selected_menu == "5"):
            search_account()
        elif(selected_menu == "6"):
            deteksi_data()
        elif(selected_menu == "7"):
            show_kritiksaran()
        elif(selected_menu == "8"):
            pengaturan_akun()
        elif(selected_menu == "9"):
            show_login()
        elif(selected_menu == "0"):
            close_app()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_menu()

def back_to_menu():
    input("\nTekan Enter untuk kembali...")
    show_menu()

def close_app():
    clear_screen()
    print("=========================================================================")
    print("|                            KELUAR APLIKASI                            |")
    print("=========================================================================")
    print("| Info: Terima kasih telah menggunakan Aplikasi Deteksi Dini Mandiri    |")
    print("|       COVID-19                                                        |")
    print("=========================================================================")
    time.sleep(3)
    exit()

def covid_dunia():
    clear_screen()
    covids = []
    with open(csv_filename_covid, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            covids.append(row)
    data_found = []
    indeks = 0
    for data in covids:
        if (data['JENIS'] == "Dunia"):
            data_found = covids[indeks]
        indeks = indeks + 1
    print("===================================================")
    print("|       DATA HARIAN KASUS COVID-19 DI DUNIA       |")
    print("===================================================")
    print("| Sumber           : WHO                          |")
    print("| Update Terakhir  : %s" % data_found["TANGGAL"])
    print("| Terkonfirmasi    : %d" % int(data_found["TERKONFIRMASI"]))
    print("| Meninggal        : %d" % int(data_found["MENINGGAL"]))
    print("===================================================")
    back_to_menu()

def covid_indonesia():
    clear_screen()
    covids = []
    with open(csv_filename_covid, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            covids.append(row)
    data_found = []
    indeks = 0
    for data in covids:
        if (data['JENIS'] == "Indonesia"):
            data_found = covids[indeks]
        indeks = indeks + 1
    print("=======================================================")
    print("|       DATA HARIAN KASUS COVID-19 DI INDONESIA       |")
    print("=======================================================")
    print("| Sumber           : https://covid19.go.id/           |")
    print("| Update Terakhir  : %s" % data_found["TANGGAL"])
    print("| Terkonfirmasi    : %d" % int(data_found["TERKONFIRMASI"]))
    print("| Kasus Aktif      : %d" % int(data_found["KASUS_AKTIF"]))
    print("| Sembuh           : %d" % int(data_found["SEMBUH"]))
    print("| Meninggal        : %d" % int(data_found["MENINGGAL"]))
    print("| Suspek           : %d" % int(data_found["SUSPEK"]))
    print("| Probable         : %d" % int(data_found["PROBABLE"]))
    print("=======================================================")
    back_to_menu()

def covid_kaltim():
    clear_screen()
    covids = []
    with open(csv_filename_covid, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            covids.append(row)
    data_found = []
    indeks = 0
    for data in covids:
        if (data['JENIS'] == "Kaltim"):
            data_found = covids[indeks]
        indeks = indeks + 1
    print("=======================================================================")
    print("|       DATA HARIAN KASUS COVID-19 DI PROVINSI KALIMANTAN TIMUR       |")
    print("=======================================================================")
    print("| Sumber               : https://covid19.kaltimprov.go.id/            |")
    print("| Update Terakhir      : %s" % data_found["TANGGAL"])
    print("| Terkonfirmasi        : %d" % int(data_found["TERKONFIRMASI"]))
    print("| Dirawat              : %d" % int(data_found["KASUS_AKTIF"]))
    print("| Sembuh               : %d" % int(data_found["SEMBUH"]))
    print("| Meninggal            : %d" % int(data_found["MENINGGAL"]))
    print("| Suspek               : %d" % int(data_found["SUSPEK"]))
    print("| Discarded            : %d" % int(data_found["DISCARDED"]))
    print("| Probable             : %d" % int(data_found["PROBABLE"]))
    print("| Menunggu Hasil Lab   : %d" % int(data_found["MENUNGGU_HASIL_LAB"]))
    print("=======================================================================")
    back_to_menu()

def covid_samarinda():
    clear_screen()
    covids = []
    with open(csv_filename_covid, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            covids.append(row)
    data_found = []
    indeks = 0
    for data in covids:
        if (data['JENIS'] == "Samarinda"):
            data_found = covids[indeks]
        indeks = indeks + 1
    print("==============================================================")
    print("|        DATA HARIAN KASUS COVID-19 DI KOTA SAMARINDA        |")
    print("==============================================================")
    print("| Sumber               : https://corona.samarindakota.go.id/ |")
    print("| Update Terakhir      : %s" % data_found["TANGGAL"])
    print("| Terkonfirmasi        : %d" % int(data_found["TERKONFIRMASI"]))
    print("| Dirawat              : %d" % int(data_found["KASUS_AKTIF"]))
    print("| Sembuh               : %d" % int(data_found["SEMBUH"]))
    print("| Meninggal            : %d" % int(data_found["MENINGGAL"]))
    print("| Suspek               : %d" % int(data_found["SUSPEK"]))
    print("| Discarded            : %d" % int(data_found["DISCARDED"]))
    print("| Probable             : %d" % int(data_found["PROBABLE"]))
    print("| Menunggu Hasil Lab   : %d" % int(data_found["MENUNGGU_HASIL_LAB"]))
    print("============================================================")
    back_to_menu()

def deteksi_pembuka():
    clear_screen()
    print("===========================================================================================================")
    print("|                                      DETEKSI DINI MANDIRI COVID-19                                      |")
    print("===========================================================================================================")
    print("| Deteksi Mandiri Dini COVID-19 adalah salah satu cara untuk membantu mempercepat tindakan penanggulangan |")
    print("| dan penyelidikan terhadap penyebaran COVID-19 di Samarinda, dengan partisipasi anda mengisi formulir    |")
    print("| kuisioner anda membantu Dinas Kesehatan dalam melakukan screening awal untuk menemukan penyebaran       |")
    print("| COVID-19 dengan pengujian lebih lanjut                                                                  |")
    print("===========================================================================================================")
    print("| [1] Lanjutkan                                                                                           |")
    print("| [2] Kembali                                                                                             |")
    print("===========================================================================================================")
    selected_menu = str(input("Masukkan Pilihan> "))
    if(selected_menu == "1"):
        riwayats = []
        with open(csv_filename_deteksi, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                riwayats.append(row)
        data_found = []
        indeks = 0
        for data in riwayats:
            if (data['NAMA'] == data_akun[1]):
                data_found = riwayats[indeks]
            indeks = indeks + 1
        if(len(data_found) > 0 and data_found['STATUS'] == "Belum diperiksa"):
            print("===========================================================================================================")
            print("| Error: Anda masih belum diperiksa, Silakan tunggu sampai diperiksa!                                     |")
            print("===========================================================================================================")
            back_to_menu()
        else:
            deteksi_lanjutan()
    elif(selected_menu == "2"):
        show_menu
    else:
        back_to_deteksi_pembuka()

def back_to_deteksi_pembuka():
    input("\nTekan Enter untuk kembali...")
    deteksi_pembuka()

def deteksi_lanjutan():
    clear_screen()
    print("==================================================================================")
    print("|                          DETEKSI DINI MANDIRI COVID-19                         |")
    print("==================================================================================")
    print("| Info: Silahkan Menjawab Pertanyaan berikut dengan jujur sesuai kondisi anda    |")
    print("|       saat ini                                                                 |")
    print("|       Isi 'q' untuk membatalkan deteksi dini mandiri COVID-19                  |")
    print("==================================================================================")
    print("|                              GEJALA YANG DIRASAKAN                             |")
    print("==================================================================================")
    print("| Saat ini saya sedang merasakan demam?                                          |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    DEMAM = str(input("Pilihan anda> "))
    data_deteksi.pop(0)
    data_deteksi.insert(0,DEMAM)
    cekpilihan("DEMAM")
    print("==================================================================================")
    print("| Saat ini saya sedang merasakan batuk / pilek?                                  |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    BATUK = str(input("Pilihan anda> "))
    data_deteksi.pop(1)
    data_deteksi.insert(1,BATUK)
    cekpilihan("BATUK")
    print("==================================================================================")
    print("| Saat ini saya merasa kesulitan bernafas atau sesak nafas?                      |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    NAFAS = str(input("Pilihan anda> "))
    data_deteksi.pop(2)
    data_deteksi.insert(2,NAFAS)
    cekpilihan("NAFAS")
    print("==================================================================================")
    print("| Saat ini saya sedang mengalami nyeri tenggorokan?                              |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    NYERI = str(input("Pilihan anda> "))
    data_deteksi.pop(3)
    data_deteksi.insert(3,NYERI)
    cekpilihan("NYERI")
    print("==================================================================================")
    print("| Lama penyakit kurang dari 14 hari?                                             |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    LAMA = str(input("Pilihan anda> "))
    data_deteksi.pop(4)
    data_deteksi.insert(4,LAMA)
    cekpilihan("LAMA")
    print("==================================================================================")
    print("|                                 RIWAYAT KONTAK                                 |")
    print("==================================================================================")
    print("| Melakukan kontak fisik atau berada dalam satu ruangan, atau berkunjung berada  |")
    print("| dalam radius 1 meter dengan kasus pasien dalam pengawasan, probable atau       |")
    print("| konfirmasi dalam 2 hari sebelum kasus timbul gejala dan hingga 14 hari setelah |")
    print("| kasus timbul gejala?                                                           |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    KONTAK = str(input("Pilihan anda> "))
    data_deteksi.pop(5)
    data_deteksi.insert(5,KONTAK)
    cekpilihan("KONTAK")
    print("==================================================================================")
    print("|                                RIWAYAT MOBILITAS                                ")
    print("==================================================================================")
    print("| Memiliki riwayat perjalanan atau tinggal diluar negeri yang melakukan          |")
    print("| penularan lokal?                                                               |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    JALAN = str(input("Pilihan anda> "))
    data_deteksi.pop(6)
    data_deteksi.insert(6,JALAN)
    cekpilihan("JALAN")
    print("==================================================================================")
    print("| Memiliki riwayat perjalanan atau tinggal di area penularan lokal di Indonesia? |")
    print("| [1] Ya                                                                         |")
    print("| [2] Tidak                                                                      |")
    print("==================================================================================")
    AREA = str(input("Pilihan anda> "))
    data_deteksi.pop(7)
    data_deteksi.insert(7,AREA)
    cekpilihan("AREA")
    if(data_deteksi[0] == "1" or data_deteksi[1] == "1" or data_deteksi[2] == "1" or data_deteksi[3] == "1" or data_deteksi[4] == "1" or data_deteksi[5] == "1" or data_deteksi[6] == "1" or data_deteksi[7] == "1"):
        deteksi_biodata()
    else:
        deteksi_penutup("tidakterindikasi")

def riwayat_deteksi():
    clear_screen()
    riwayats = []
    with open(csv_filename_deteksi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            riwayats.append(row)
    data_found = []
    indeks = 0
    for data in riwayats:
        if (data['NAMA'] == data_akun[1]):
            data_found = riwayats[indeks]
        indeks = indeks + 1
    print("===============================================================================")
    print("|                                   BIODATA                                   |")
    print("===============================================================================")
    if(len(data_found) > 0):
        print("| Timestamp          : %s" % (data_found['TIMESTAMP']))
        print("| Nama               : %s" % (data_found['NAMA']))
        print("| Umur               : %d" % int(data_found['UMUR']))
        print("| No. HP/WA          : %d" % int(data_found['NOHP']))
        print("| Alamat             : %s" % (data_found['ALAMAT']))
        print("| Kelurahan / Desa   : %s" % (data_found['ALAMAT2']))
        print("| Status             : %s" % (data_found['STATUS']))
        print("| Keterangan         : %s" % (data_found['KETERANGAN']))
        print("===============================================================================")
    else:
        print("===============================================================================")
        print("| Error: Anda belum melakukan deteksi dini!                                   |")
        print("===============================================================================")
    back_to_menu()

def deteksi_biodata():
    clear_screen()
    now = datetime.datetime.now()
    timestamp = "%d/%d/%d %d:%d:%d" % (now.day,now.month,now.year,now.hour,now.minute,now.second)
    print("===============================================================================")
    print("|                                   BIODATA                                   |")
    print("===============================================================================")
    print("| Timestamp          : %s" % (timestamp))
    print("| Nama               : %s" % (data_akun[1]))
    print("| Umur               : %s" % (data_akun[2]))
    print("| No. HP/WA          : %s" % (data_akun[3]))
    print("| Alamat             : %s" % (data_akun[4]))
    print("| Kelurahan / Desa   : %s" % (data_akun[5]))
    print("===============================================================================")
    file_deteksi_in = open(txt_filename_deteksi, "r")
    no = file_deteksi_in.read()
    file_deteksi_in.close()
    with open(csv_filename_deteksi, mode='a') as csv_file:
        fieldnames = ['NO', 'TIMESTAMP', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2', 'STATUS', 'KETERANGAN']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'NO': int(no), 'TIMESTAMP': timestamp, 'NAMA': data_akun[1], 'UMUR': data_akun[2], 'NOHP': data_akun[3], 'ALAMAT': data_akun[4], 'ALAMAT2': data_akun[5], 'STATUS': "Belum diperiksa", 'KETERANGAN': "-"})
    no_int = int(no)
    no_int += 1
    file_deteksi_in = open(txt_filename_deteksi, "w")
    file_deteksi_in.write(str(no_int))
    file_deteksi_in.close()
    input("Tekan Enter untuk melanjutkan...")
    deteksi_penutup("terindikasi")

def deteksi_penutup(tipe):
    clear_screen()
    if(tipe == "terindikasi"):
        print("================================================================================================")
        print("|                                 DETEKSI DINI MANDIRI COVID-19                                |")
        print("================================================================================================")
        print("| Terimakasih telah berpartisipasi bersama dalam Penanggulangan COVID-19, anda disarankan      |")
        print("| mengubungi Call Center Posko Tanggap COVID-19 di nomor 112 (Samarinda) untuk konsultasi      |")
        print("| terhadap keluhan anda dan Pemeriksaan Lebih Lanjut, atau kami yang akan menghubungi Anda     |")
        print("| melalui Telepon / WA berdasarkan entry biodata yang telah anda lakukan.                      |")
        print("================================================================================================")
        print("| Tetap jaga kondisi tubuh anda dengan menerapkan Perilaku Hidup Bersih dan Sehat serta        |")
        print("| tindakan pencegahan sebagai berikut :                                                        |")
        print("| 1. Bersihkan benda yang sering disentuh / digunakan karena beresiko sebagai media perantara  |")
        print("|    virus.                                                                                    |")
        print("| 2. Gunakan Masker saat batuk atau terapkan etika batuk dengan menutup mulut menggunakan      |")
        print("|    lengan / tisue jangan menggunakan telapak tangan.                                         |")
        print("| 3. Hindari Menyentuh Wajah                                                                   |")
        print("| 4. Sering Cuci Tangan Pakai Sabun Menggunakan Air Mengalir                                   |")
        print("| 5. Konsumsi Makanan Bergizi Seperti Buah dan Sayur, Olahraga Secara Rutin                    |")
        print("| 6. Hindari Menutup Mulut Menggunakan Tangan Saat Batuk (Terapkan Etika Batuk)                |")
        print("================================================================================================")
    elif(tipe == "tidakterindikasi"):
        print("=================================================================================================")
        print("|                                 DETEKSI DINI MANDIRI COVID-19                                 |")
        print("=================================================================================================")
        print("| Terimakasih telah berpartisipasi bersama dalam Penanggulangan COVID-19, anda tidak menunjukan |")
        print("| gejala terinfeksi Virus Corona, tetapi tetap waspada dengan menerapkan perilaku Hidup Bersih  |")
        print("| dan Sehat serta tindakan pencegahan sebagai berikut :                                         |")
        print("| 1. Bersihkan benda yang sering disentuh / digunakan karena beresiko sebagai media perantara   |")
        print("|    virus.                                                                                     |")
        print("| 2. Gunakan Masker saat batuk atau terapkan etika batuk dengan menutup mulut menggunakan       |")
        print("|    lengan / tisue jangan menggunakan telapak tangan.                                          |")
        print("| 3. Hindari Menyentuh Wajah                                                                    |")
        print("| 4. Sering Cuci Tangan Pakai Sabun Menggunakan Air Mengalir                                    |")
        print("| 5. Konsumsi Makanan Bergizi Seperti Buah dan Sayur, Olahraga Secara Rutin                     |")
        print("| 6. Hindari Menutup Mulut Menggunakan Tangan Saat Batuk (Terapkan Etika Batuk)                 |")
        print("=================================================================================================")
    back_to_menu()

def deteksi_data():
    clear_screen()
    print("==============================================================")
    print("|             DATA DETEKSI DINI MANDIRI COVID-19             |")
    print("==============================================================")
    riwayats = []
    with open(csv_filename_deteksi, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            riwayats.append(row)
    for data in riwayats:
        print("| Data ke-%d" % int(data['NO']))
        print("| Timestamp          : %s " % (data['TIMESTAMP']))
        print("| Nama               : %s " % (data['NAMA']))
        print("| Umur               : %s " % (data['UMUR']))
        print("| No HP              : %s " % (data['NOHP']))
        print("| Alamat             : %s " % (data['ALAMAT']))
        print("| Kelurahan / Desa   : %s " % (data['ALAMAT2']))
        print("| Status             : %s " % (data['STATUS']))
        print("| Keterangan         : %s " % (data['KETERANGAN']))
        print("==============================================================")
    if not(len(riwayats) > 0):
        print("==============================================================")
        print("| Error: Tidak ada data yang tersedia                        |")
        print("==============================================================")
        back_to_menu()
    if(data_akun[0] == "dinkes"):
        no = str(input("\nMasukkan No Data> "))
        if not(data['NO'] == no):
            print("==============================================================")
            print("| Error: Nomor Data tersebut tidak ditemukan!                |")
            print("==============================================================")
        indeks = 0
        for data in riwayats:
            if (data['NO'] == no):
                print("==============================================================")
                print("| Sukses: Data ditemukan!                                    |")
                print("| [1] Update Status                                          |")
                print("| [2] Hapus Data                                             |")
                print("| [3] Kembali                                                |")
                print("==============================================================")
                pilih = str(input("Pilih Pilihan> "))
                if(pilih == "1"):
                    if(riwayats[indeks]['STATUS'] == "Sudah diperiksa"):
                        print("==============================================================")
                        print("| Error: Orang tersebut sudah diperiksa!                     |")
                        print("==============================================================")
                        break
                    else:
                        print("==============================================================")
                        print("| Keterangan:                                                |")
                        print("| [1] Terkonfirmasi                                          |")
                        print("| [2] Suspek                                                 |")
                        print("| [3] Discarded                                              |")
                        print("| [4] Probable                                               |")
                        print("| [5] Kontak Erat                                            |")
                        print("| [6] Pelaku Perjalanan                                      |")
                        print("| [7] Kembali                                                |")
                        print("==============================================================")
                        keterangan = str(input("Pilih Pilihan> "))
                        if(keterangan == "1"):
                            riwayats[indeks]['KETERANGAN'] = "Terkonfirmasi"
                        elif(keterangan == "2"):
                            riwayats[indeks]['KETERANGAN'] = "Suspek"
                        elif(keterangan == "3"):
                            riwayats[indeks]['KETERANGAN'] = "Discarded"
                        elif(keterangan == "4"):
                            riwayats[indeks]['KETERANGAN'] = "Probable"
                        elif(keterangan == "5"):
                            riwayats[indeks]['KETERANGAN'] = "Kontak Erat"
                        elif(keterangan == "6"):
                            riwayats[indeks]['KETERANGAN'] = "Pelaku Perjalanan"
                        elif(keterangan == "7"):
                            deteksi_data()
                        else:
                            print("==============================================================")
                            print("| Error: Anda memilih pilihan yang salah!                    |")
                            print("==============================================================")
                            back_to_menu()
                        riwayats[indeks]['STATUS'] = "Sudah diperiksa"
                        print("==============================================================")
                        print("| Sukses: Data berhasil di update!                           |")
                        print("==============================================================")
                elif(pilih == "2"):
                    riwayats.remove(riwayats[indeks])
                    print("==============================================================")
                    print("| Sukses: Data berhasil di hapus!                            |")
                    print("==============================================================")
                elif(pilih == "3"):
                    show_menu()
                else:
                    print("==============================================================")
                    print("| Error: Anda memilih pilihan yang salah!                    |")
                    print("==============================================================")
                    back_to_menu()
            indeks = indeks + 1
        with open(csv_filename_deteksi, mode="w") as csv_file:
            fieldnames = ['NO', 'TIMESTAMP', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2', 'STATUS', 'KETERANGAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in riwayats:
                writer.writerow({'NO': new_data['NO'], 'TIMESTAMP': new_data['TIMESTAMP'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2'], 'STATUS': new_data['STATUS'], 'KETERANGAN': new_data['KETERANGAN']})
    back_to_menu()

def pencegahan_covid():
    clear_screen()
    print("==================================================================")
    print("|                    CARA PENCEGAHAN COVID-19                    |")
    print("==================================================================")
    print("| 1. Sering cuci tangan dengan sabun atau hand-sanitizer.        |")
    print("| 2. Hindari menyentuh wajah, terutama hidung, mulut, dan mata   |")
    print("| 3. Bersihkan permukaan benda yang disentuh banyak orang        |")
    print("| 4. Physical Distancing! Minimalisir kontak fisik dengan sesama |")
    print("| 5. Jaga jarak 1-3 meter dengan orang yang sakit                |")
    print("==================================================================")
    back_to_menu()

def call_center():
    clear_screen()
    print("==================================================================")
    print("|   CALL CENTER COVID-19 10 KAB/KOTA PROVINSI KALIMANTAN TIMUR   |")
    print("==================================================================")
    print("| Samarinda            : 112                                     |")
    print("| Balikpapan           : 119/08115231919119                      |")
    print("| Bontang              : 08125368104                             |")
    print("| Berau                : 082149492491                            |")
    print("| Paser                : 08125877983                             |")
    print("| Penajam Paser Utama  : 082151610373/081354818119               |")
    print("| Kutai Timur          : 082195724043/081347391313               |")
    print("| Kutai Barat          : 081249999749/082251085231               |")
    print("| Kutai Kartanegara    : 082251171009                            |")
    print("| Mahakam Ulu          : 085246768633/082148745314/085259592255  |")
    print("==================================================================")
    back_to_menu()

def rs_covid():
    clear_screen()
    print("==================================================================================")
    print("|             RUMAH SAKIT RUJUKAN COVID-19 PROVINSI KALIMANTAN TIMUR             |")
    print("==================================================================================")
    print("| RSUD A.W. Syahranie Samarinda              RSUD Panglima Sebaya Paser          |")
    print("| RSUD I.A. Moeis Samarinda                  RSUD Taman Husada Bontang           |")
    print("| RSUD Beriman Balikpapan                    RSUD Abdul Rivai Berau              |")
    print("| RSUD DR Kanujoso Djatiwibowo Bpn           RSUD Kudungga Sangatta              |")
    print("| RS Tk II Dr. R. Hardjanto Balikpapan       RSUD Ratu Aji Putri Botung PPU      |")
    print("| RSUD A.M Parikesit Tenggarong              RSUD Harapan Insan Sendawar Kubar   |")
    print("| RSJD Atma Husada Mahakam                   RSUD ABADI Samboja                  |")
    print("| RS Pupuk Kaltim Bontang                    RS Pertamina Balikpapan             |")
    print("==================================================================================")
    back_to_menu()

def faq_covid():
    clear_screen()
    print("===========================================================================================================================")
    print("|                                                           FAQ                                                           |")
    print("===========================================================================================================================")
    print("| Info: Pertanyaan yang sering ditanyakan mengenai COVID-19.                                                              |")
    print("| [1] Informasi Dasar COVID-19                                                                                            |")
    print("| [2] Penularan COVID-19                                                                                                  |")
    print("| [3] Mencegah Penularan COVID-19                                                                                         |")
    print("| [4] Kasus COVID-19                                                                                                      |")
    print("| [5] Kembali                                                                                                             |")
    print("===========================================================================================================================")
    faq = str(input("Masukkan Pilihan> "))
    if(faq == "1"):
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Informasi Dasar COVID-19                                                                                                |")
        print("===========================================================================================================================")
        print("| [1] Apakah Coronanvirus dan COVID-19?                                                                                   |")
        print("| [2] Apakah gejala COVID-19?                                                                                             |")
        print("| [3] Apa itu Kasus Suspek, Probable, dan Konfirmasi?                                                                     |")
        print("| [4] Apa yang dimaksud dengan Kontak Erat?                                                                               |")
        print("| [5] Apa itu Pelaku Perjalanan, Discarded, Selesai Isolasi, dan Kasus Kematian?                                          |")
        print("| [6] Seberapa bahaya COVID-19 ini?                                                                                       |")
        print("| [7] Berapa lama virus ini bertahan di permukaan benda?                                                                  |")
        print("| [8] Apakah COVID-19 seperti SARS?                                                                                       |")
        print("| [9] Kembali                                                                                                             |")
        print("===========================================================================================================================")
        faq_id = str(input("Masukkan Pilihan> "))
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Informasi Dasar COVID-19                                                                                                |")
        print("===========================================================================================================================")
        if(faq_id == "1"):
            print("| [Apakah Coronanvirus dan COVID-19?]                                                                                     |")
            print("| Coronavirus Disease 2019 atau COVID-19 adalah penyakit baru yang dapat menyebabkan gangguan pernapasan dan radang paru. |")
            print("| Penyakit ini disebabkan oleh infeksi Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2). Gejala klinis yang   |")
            print("| muncul beragam, mulai dari seperti gejala flu biasa (batuk, pilek, nyeri tenggorok, nyeri otot, nyeri kepala) sampai    |")
            print("| yang berkomplikasi berat (pneumonia atau sepsis) atau bahkan tidak bergejala sama sekali.                               |")
        elif(faq_id == "2"):
            print("| [Apakah gejala COVID-19?]                                                                                               |")
            print("| Orang dengan COVID-19 memiliki berbagai gejala yang dilaporkan - mulai dari gejala ringan hingga penyakit parah. Gejala |")
            print("| dapat muncul 2-14 hari setelah terpapar virus. Orang dengan gejala di bawah ini mungkin memiliki COVID-19:              |")
            print("| - Demam atau kedinginan                                                                                                 |")
            print("| - Batuk                                                                                                                 |")
            print("| - Napas pendek atau sulit bernapas                                                                                      |")
            print("| - Kelelahan                                                                                                             |")
            print("| - Otot atau sakit tubuh                                                                                                 |")
            print("| - Sakit kepala                                                                                                          |")
            print("| - Kehilangan rasa atau bau baru                                                                                         |")
            print("| - Sakit tenggorokan                                                                                                     |")
            print("| - Hidung tersumbat atau berair                                                                                          |")
            print("| - Mual atau muntah                                                                                                      |")
            print("| - Diare                                                                                                                 |")
            print("| Jika ada orang yang dalam 14 hari sebelum muncul gejala tersebut pernah melakukan perjalanan ke wilayah terjangkit atau |")
            print("| pernah merawat/kontak erat dengan penderita COVID-19, maka orang tersebut akan diperiksa melalui pemeriksaan            |")
            print("| laboratorium lebih lanjut untuk memastikan diagnosisnya.                                                                |")
        elif(faq_id == "3"):
            print("| [Apa itu Kasus Suspek, Probable, dan Konfirmasi?]                                                                       |")
            print("| Menurut KMK No. HK.01.07-MENKES-413-2020 ttg Pedoman Pencegahan dan Pengendalian COVID-19, yang dimaksud dengan Kasus   |")
            print("| Suspek, Probable, dan Konfirmasi adalah sebagai berikut:                                                                |")
            print("|                                                                                                                         |")
            print("| Kasus Suspek                                                                                                            |")
            print("|                                                                                                                         |")
            print("| Seseorang yang memiliki salah satu dari kriteria berikut:                                                               |")
            print("| a. Orang dengan Infeksi Saluran Pernapasan Akut (ISPA)* DAN pada 14 hari terakhir sebelum timbul gejala memiliki riwayat|")
            print("| perjalanan atau tinggal di negara/wilayah Indonesia yang melaporkan transmisi lokal**.                                  |")
            print("| b. Orang dengan salah satu gejala/tanda ISPA* DAN pada 14 hari terakhir sebelum timbul gejala memiliki riwayat kontak   |")
            print("| dengan kasus konfirmasi/probable COVID-19. Orang dengan ISPA berat/pneumonia berat yang membutuhkan perawatan di rumah  |")
            print("| sakit dan tidak ada penyebab lain berdasarkan gambaran klinis yang meyakinkan.                                          |")
            print("|                                                                                                                         |")
            print("| Istilah Pasien Dalam Pengawasan (PDP) saat ini dikenal kembali dengan istilah kasus suspek.                             |")
            print("|                                                                                                                         |")
            print("| Kasus Probable                                                                                                          |")
            print("|                                                                                                                         |")
            print("| Kasus suspek dengan ISPA Berat/ARDS/meninggal dengan gambaran klinis yang meyakinkan COVID-19 DAN belum ada hasil       |")
            print("| pemeriksaan laboratorium RT-PCR.                                                                                        |")
            print("|                                                                                                                         |")
            print("| Kasus Konfirmasi                                                                                                        |")
            print("|                                                                                                                         |")
            print("| Seseorang yang dinyatakan positif terinfeksi virus COVID-19 yang dibuktikan dengan pemeriksaan laboratorium RT-PCR.     |")
            print("| Kasus konfirmasi dibagi menjadi 2:                                                                                      |")
            print("| a. Kasus konfirmasi dengan gejala (simptomatik)                                                                         |")
            print("| b. Kasus konfirmasi tanpa gejala (asimptomatik)                                                                         |")
            print("|                                                                                                                         |")
            print("| Keterangan:                                                                                                             |")
            print("|                                                                                                                         |")
            print("| *ISPA yaitu demam (≥38oC) atau riwayat demam; dan disertai salah satu gejala/tanda penyakit pernapasan seperti:         |")
            print("| batuk/sesak nafas/sakit tenggorokan/pilek/pneumonia ringan hingga berat.                                                |")
        elif(faq_id == "4"):
            print("| [Apa yang dimaksud dengan Kontak Erat?]                                                                                 |")
            print("| Menurut KMK No. HK.01.07-MENKES-413-2020 ttg Pedoman Pencegahan dan Pengendalian COVID-19, yang dimaksud dengan Kontak  |")
            print("| Erat adalah sebagai berikut:                                                                                            |")
            print("|                                                                                                                         |")
            print("| Orang yang memiliki riwayat kontak dengan kasus probable atau konfirmasi COVID-19. Riwayat kontak yang dimaksud antara  |")
            print("| lain:                                                                                                                   |")
            print("|                                                                                                                         |")
            print("| a. Kontak tatap muka/berdekatan dengan kasus probable atau kasus konfirmasi dalam radius 1 meter dan dalam jangka waktu |")
            print("| 15 menit atau lebih.                                                                                                    |")
            print("| b. Sentuhan fisik langsung dengan kasus probable atau konfirmasi (seperti bersalaman, berpegangan tangan, dan lain      |")
            print("| -lain).                                                                                                                 |")
            print("| c. Orang yang memberikan perawatan langsung terhadap kasus probable atau konfirmasi tanpa menggunakan APD yang sesuai   |")
            print("| standar.                                                                                                                |")
            print("| d. Situasi lainnya yang mengindikasikan adanya kontak berdasarkan penilaian risiko lokal yang ditetapkan oleh tim       |")
            print("| penyelidikan epidemiologi setempat.                                                                                     |")
            print("|                                                                                                                         |")
            print("| Pada kasus probable atau konfirmasi yang bergejala (simptomatik), untuk menemukan kontak erat periode kontak dihitung   |")
            print("| dari 2 hari sebelum timbul gejala dan hingga 14 hari setelah timbul gejala.                                             |")
            print("|                                                                                                                         |")
            print("| Pada kasus konfirmasi yang tidak bergejala (asimptomatik), untuk menemukan kontak erat periode kontak dihitung dari 2   |")
            print("| hari sebelum dan 14 hari setelah tanggal pengambilan spesimen kasus konfirmasi.                                         |")
        elif(faq_id == "5"):
            print("| [Apa itu Pelaku Perjalanan, Discarded, Selesai Isolasi, dan Kasus Kematian?]                                            |")
            print("| Menurut KMK No. HK.01.07-MENKES-413-2020 ttg Pedoman Pencegahan dan Pengendalian COVID-19, yang dimaksud dengan Pelaku  |")
            print("| Perjalanan, Discarded, Selesai Isolasi, dan Kasus Kematian adalah sebagai berikut:                                      |")
            print("|                                                                                                                         |")
            print("| Pelaku Perjalanan                                                                                                       |")
            print("|                                                                                                                         |")
            print("| Seseorang yang melakukan perjalanan dari dalam negeri (domestik) maupun luar negeri pada 14 hari terakhir.              |")
            print("|                                                                                                                         |")
            print("| Discarded                                                                                                               |")
            print("|                                                                                                                         |")
            print("| Seseorang dikategorikan discarded apabila memenuhi salah satu kriteria berikut:                                         |")
            print("|                                                                                                                         |")
            print("| a. Seseorang dengan status kasus suspek dengan hasil pemeriksaan RT-PCR 2 kali negatif selama 2 hari berturut-turut     |")
            print("| dengan selang waktu >24 jam.                                                                                            |")
            print("| b. Seseorang dengan status kontak erat yang telah menyelesaikan masa karantina selama 14 hari.                          |")
            print("|                                                                                                                         |")
            print("| Selesai Isolasi                                                                                                         |")
            print("|                                                                                                                         |")
            print("| Selesai isolasi apabila memenuhi salah satu kriteria berikut:                                                           |")
            print("|                                                                                                                         |")
            print("| a. Kasus konfirmasi tanpa gejala (asimtomatik) yang tidak dilakukan pemeriksaan follow up RT-PCR dengan ditambah 10     |")
            print("| hari isolasi mandiri sejak pengambilan spesimen diagnosis konfirmasi.                                                   |")
            print("| b. Kasus probable/kasus konfirmasi dengan gejala (simptomatik) yang tidak dilakukan pemeriksaan follow up RT-PCR        |")
            print("| dihitung 10 hari sejak tanggal onset dengan ditambah minimal 3 hari setelah tidak lagi menunjukkan gejala demam dan     |")
            print("| gangguan pernapasan.                                                                                                    |")
            print("|                                                                                                                         |")
            print("| c. Kasus probable/kasus konfirmasi dengan gejala (simptomatik) yang mendapatkan hasil pemeriksaan follow up RT-PCR 1    |")
            print("| kali negatif, dengan ditambah minimal 3 hari setelah tidak lagi menunjukkan gejala demam dan gangguan pernapasan.       |")
            print("|                                                                                                                         |")
            print("| Kematian                                                                                                                |")
            print("|                                                                                                                         |")
            print("| Kematian COVID-19 untuk kepentingan surveilans adalah kasus konfirmasi/probable COVID-19 yang meninggal.                |")
        elif(faq_id == "6"):
            print("| [Seberapa bahaya COVID-19 ini?]                                                                                         |")
            print("| Seperti penyakit pernapasan lainnya, COVID-19 dapat menyebabkan gejala ringan termasuk pilek sakit tenggorokan, batuk,  |")
            print("| dan demam. Sekitar 80% kasus dapat pulih tanpa perlu perawatan khusus. Sekitar 1 dari setiap 6 orang mungkin akan       |")
            print("| menderita sakit yang parah, seperti disertai pneumonia atau kesulitan bernafas, yang biasanya muncul secara bertahap.   |")
            print("| Walaupun angka kematian penyakit ini masih jarang, namun bagi orang yang berusia lanjut, dan orang-orang dengan kondisi |")
            print("| medis yang sudah ada sebelumnya (seperti diabetes, tekanan darah tinggi dan penyakit jantung), mereka biasanya lebih    |")
            print("| rentan untuk gejala yang lebih parah. Orang yang mengalami demam, batuk, dan sulit bernapas harus segera mendapatkan    |")
            print("| pertolongan medis.                                                                                                      |")
        elif(faq_id == "7"):
            print("| [Berapa lama virus ini bertahan di permukaan benda?]                                                                    |")
            print("| Sampai saat ini belum diketahui dengan pasti berapa lama COVID-19 mampu bertahan di permukaan suatu benda, meskipun     |")
            print("| studi awal menunjukkan bahwa COVID-19 dapat bertahan hingga beberapa jam, tergantung jenis permukaan, suhu, atau        |")
            print("| kelembaban lingkungan.                                                                                                  |")
            print("|                                                                                                                         |")
            print("| Namun desinfektan sederhana dapat membunuh virus tersebut sehingga tidak mungkin menginfeksi orang lagi. Dan            |")
            print("| membiasakan cuci tangan dengan air dan sabun, atau handrub berbasis alkohol, serta hindari menyentuh mata, mulut atau   |")
            print("| hidung (segitiga wajah) lebih efektif melindungi diri Anda.                                                             |")
        elif(faq_id == "8"):
            print("| [Apakah COVID-19 seperti SARS?]                                                                                         |")
            print("| SARS adalah coronavirus yang diidentifikasi pada tahun 2003 dan termasuk dalam keluarga besar virus yang sama dengan    |")
            print("| COVID-19, namun berbeda jenis virusnya. Gejalanya mirip dengan COVID-19, namun SARS lebih berat. SARS lebih mematikan   |")
            print("| tetapi tidak lebih infeksius (menular) dibanding COVID-19.                                                              |")
        elif(faq_id == "9"):
            faq_covid()
        else:            
            print("| Error: Pilihan tersebut tidak tersedia!                                                                                 |")
        print("===========================================================================================================================")
        back_to_faq()
    elif(faq == "2"):
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Penularan COVID-19                                                                                                      |")
        print("===========================================================================================================================")
        print("| [1]  Bagaimana manusia bisa terinfeksi COVID-19?                                                                        |")
        print("| [2]  Siapa saja yang berisiko terinfeksi COVID-19?                                                                      |")
        print("| [3]  Manakah yang lebih rentan terinfeksi coronavirus: orang yang lebih tua atau orang yang lebih muda?                 |")
        print("| [4]  Apakah COVID-19 dapat ditularkan dari orang yang tidak bergejala sakit?                                            |")
        print("| [5]  Apa COVID-19 dapat menular melalui udara?                                                                          |")
        print("| [6]  Bisakah manusia terinfeksi COVID-19 dari hewan?                                                                    |")
        print("| [7]  Apakah sudah ada vaksin atau obat untuk COVID-19?                                                                  |")
        print("| [8]  Sepertinya saya berinteraksi dengan orang terjangkit COVID-19, apa yang harus saya lakukan?                        |")
        print("| [9]  Teman kantor/sekolah/kuliah atau tetangga saya baru pulang dari wilayah atau negara yang terinfeksi COVID-19, apa  |")
        print("|      yang harus saya lakukan?                                                                                           |")
        print("| [10] Bisakah saya terjangkit COVID-19 dari surat atau paket kiriman dari luar negeri?                                   |")
        print("| [11] Bisakah saya terjangkit COVID-19 dari makanan atau makanan yang dikirim?                                           |")
        print("| [12] Berapa lama waktu yang diperlukan sejak tertular/terinfeksi hingga muncul gejala penyakit infeksi COVID-19?        |")
        print("| [13] Bisa saya di tes jika saya merasa saya terjangkit COVID-19?                                                        |")
        print("| [14] Apa yang harus saya lakukan ketika saya mengalami gejala COVID-19 saat sedang di luar rumah?                       |")
        print("| [15] Apa yang akan terjadi jika tenaga medis profesional menyatakan saya mungkin terjangkit COVID-19?                   |")
        print("| [16] Kembali                                                                                                            |")
        print("===========================================================================================================================")
        faq_id = str(input("Masukkan Pilihan> "))
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Penularan COVID-19                                                                                                      |")
        print("===========================================================================================================================")
        if(faq_id == "1"):
            print("| [Bagaimana manusia bisa terinfeksi COVID-19?]                                                                           |")
            print("| Seseorang dapat terinfeksi dari penderita COVID-19. Penyakit ini dapat menyebar melalui tetesan kecil (droplet) dari    |")
            print("| hidung atau mulut pada saat batuk atau bersin. Droplet tersebut kemudian jatuh pada benda di sekitarnya. Kemudian jika  |")
            print("| ada orang lain menyentuh benda yang sudah terkontaminasi dengan droplet tersebut, lalu orang itu menyentuh mata, hidung |")
            print("| atau mulut (segitiga wajah), maka orang itu dapat terinfeksi COVID-19. Atau bisa juga seseorang terinfeksi COVID-19     |")
            print("| ketika tanpa sengaja menghirup droplet dari penderita. Inilah sebabnya penting untuk memakai masker dan menjaga jarak   |")
            print("| dengan orang lain.                                                                                                      |")
            print("|                                                                                                                         |")
            print("| Sampai saat ini, para ahli masih terus melakukan penyelidikan untuk menentukan sumber virus, jenis paparan, dan cara    |")
            print("| penularannya. Tetap pantau sumber informasi yang akurat dan resmi mengenai perkembangan penyakit ini.                   |")
        elif(faq_id == "2"):
            print("| [Siapa saja yang berisiko terinfeksi COVID-19?]                                                                         |")
            print("| Orang yang tinggal atau bepergian di daerah di mana virus COVID-19 bersirkulasi sangat mungkin berisiko terinfeksi.     |")
            print("| Mereka yang terinfeksi adalah orang-orang yang dalam 14 hari sebelum muncul gejala melakukan perjalanan dari negara     |")
            print("| terjangkit, atau yang kontak erat, seperti anggota keluarga, rekan kerja atau tenaga medis yang merawat pasien sebelum  |")
            print("| mereka tahu pasien tersebut terinfeksi COVID-19.                                                                        |")
            print("|                                                                                                                         |")
            print("| Petugas kesehatan yang merawat pasien yang terinfeksi COVID-19 berisiko lebih tinggi dan harus konsisten melindungi     |")
            print("| diri mereka sendiri dengan prosedur pencegahan dan pengendalian infeksi yang tepat.                                     |")
        elif(faq_id == "3"):
            print("| [Manakah yang lebih rentan terinfeksi coronavirus: orang yang lebih tua atau orang yang lebih muda?]                    |")
            print("| Tidak ada batasan usia orang-orang dapat terinfeksi oleh coronavirus ini (COVID-19). Namun orang yang lebih tua dan     |")
            print("| orang-orang dengan kondisi medis yang sudah ada sebelumnya (seperti asma, diabetes, penyakit jantung, atau tekanan      |")
            print("| darah tinggi) tampaknya lebih rentan mengalami gejala yang lebih parah.                                                 |")
        elif(faq_id == "4"):
            print("| [Apakah COVID-19 dapat ditularkan dari orang yang tidak bergejala sakit?]                                               |")
            print("| Cara penularan utama penyakit ini adalah melalui tetesan kecil (droplet) yang dikeluarkan pada saat seseorang batuk     |")
            print("| atau bersin.                                                                                                            |")
            print("|                                                                                                                         |")
            print("| Banyak orang yang teridentifikasi COVID-19 hanya mengalami gejala ringan seperti batuk ringan, atau tidak mengeluh      |")
            print("| sakit, yang mungkin terjadi pada tahap awal penyakit. Sampai saat ini, para ahli masih terus melakukan penyelidikan     |")
            print("| untuk menentukan periode penularan atau masa inkubasi COVID-19. Tetap pantau sumber informasi yang akurat dan resmi     |")
            print("| mengenai perkembangan penyakit ini.                                                                                     |")
        elif(faq_id == "5"):
            print("| [Apa COVID-19 dapat menular melalui udara?]                                                                             |")
            print("| Menurut WHO, droplet, yang umumnya dianggap partikel dengan diameter <5μm, dapat tetap berada di udara untuk jangka     |")
            print("| waktu yang lama dan ditransmisikan ke orang lain pada jarak lebih dari 1 m. Dalam konteks COVID-19, transmisi melalui   |")
            print("| udara dapat terjadi dalam keadaan dan pengaturan khusus di mana prosedur atau perawatan pendukung yang menghasilkan     |")
            print("| aerosol dilakukan, misalnya, bronkoskopi, mengubah pasien ke posisi tengkurap, memutus hubungan pasien dari ventilator, |")
            print("| atau lainnya.                                                                                                           |")
        elif(faq_id == "6"):
            print("| [Bisakah manusia terinfeksi COVID-19 dari hewan?]                                                                       |")
            print("| Saat ini, belum ditemukan bukti bahwa hewan peliharaan seperti anjing atau kucing dapat terinfeksi virus COVID-19.      |")
            print("| Namun, akan jauh lebih baik untuk selalu mencuci tangan dengan sabun dan air setelah kontak dengan hewan peliharaan.    |")
            print("| Kebiasaan ini dapat melindungi Anda terhadap berbagai bakteri umum seperti E.coli dan Salmonella yang dapat berpindah   |")
            print("| antara hewan peliharaan dan manusia.                                                                                    |")
        elif(faq_id == "7"):
            print("| [Apakah sudah ada vaksin atau obat untuk COVID-19?]                                                                     |")
            print("| Vaksin untuk mencegah infeksi COVID-19 sedang dalam tahap pengembangan/uji coba.                                        |")
        elif(faq_id == "8"):
            print("| [Sepertinya saya berinteraksi dengan orang terjangkit COVID-19, apa yang harus saya lakukan?]                           |")
            print("| Silakan melakukan uji risiko mandiri gejala COVID-19 di Aplikasi Deteksi Dini Mandiri COVID-19. Jika timbul gejala      |")
            print("| mirip COVID-19, segera hubungi Call Center Posko Tanggap COVID-19 di nomor 112 (Samarinda) untuk mendapat arahan lebih  |")
            print("| lanjut.                                                                                                                 |")
        elif(faq_id == "9"):
            print("| [Teman kantor/sekolah/kuliah atau tetangga saya baru pulang dari wilayah atau negara yang terinfeksi COVID-19, apa yang |")
            print("| harus saya lakukan?]                                                                                                    |")
            print("| Pastikan teman atau tetangga Anda melakukan isolasi mandiri atau menghubungi Call Center Posko Tanggap COVID-19 di      |")
            print("| nomor 112 (Samarinda) untuk mendapat arahan lebih lanjut.                                                               |")
        elif(faq_id == "10"):
            print("| [Bisakah saya terjangkit COVID-19 dari surat atau paket kiriman dari luar negeri?]                                      |")
            print("| Orang yang menerima paket tidak berisiko tertular virus COVID-19. Dari data virus korona sebelumnya, kita tahu bahwa    |")
            print("| jenis virus ini tidak bertahan lama pada benda mati, seperti surat atau paket.                                          |")
        elif(faq_id == "11"):
            print("| [Bisakah saya terjangkit COVID-19 dari makanan atau makanan yang dikirim?]                                              |")
            print("| Saat ini tidak ada bukti bahwa penularan coronavirus penyebab COVID-19 dari makanan. Virus seperti coronavirus tidak    |")
            print("| bisa hidup lama di luar tubuh.                                                                                          |")
        elif(faq_id == "12"):
            print("| [Berapa lama waktu yang diperlukan sejak tertular/terinfeksi hingga muncul gejala penyakit infeksi COVID-19?]           |")
            print("| Waktu yang diperlukan sejak tertular/terinfeksi hingga muncul gejala disebut masa inkubasi. Saat ini masa inkubasi      |")
            print("| COVID-19 diperkirakan antara 1-14 hari, dan perkiraan ini dapat berubah sewaktu-waktu sesuai perkembangan kasus.        |")
        elif(faq_id == "13"):
            print("| [Bisa saya di tes jika saya merasa saya terjangkit COVID-19?]                                                           |")
            print("| Tes untuk COVID-19 di fasilitas kesehatan milik Pemprov Kalimatan Timur hanya dilakukan jika ada kemungkinan besar Anda |")
            print("| memiliki penyakit tersebut                                                                                              |")
            print("|                                                                                                                         |")
            print("| Misalnya jika:                                                                                                          |")
            print("|                                                                                                                         |")
            print("| -Anda melakukan kontak dekat dengan seseorang dengan orang yang positif COVID-19                                        |")
            print("| -Anda bepergian ke negara atau daerah dengan risiko COVID-19 tinggi dalam 14 hari terakhir                              |")
            print("|                                                                                                                         |")
            print("| Dalam kasus ini, Anda dapat hubungi Call Center Posko Tanggap COVID-19 di nomor 112 (Samarinda) untuk mendapat arahan   |")
            print("| lebih lanjut.                                                                                                           |")
        elif(faq_id == "14"):
            print("| [Apa yang harus saya lakukan ketika saya mengalami gejala COVID-19 saat sedang di luar rumah?]                          |")
            print("| Anda tidak disarankan untuk melakukan kegiatan di luar rumah kecuali untuk kegiatan yang penting atau mendesak. Jika    |")
            print("| Anda mengalami gejala demam/batuk/pilek/nyeri tenggorok atau sesak napas, segera kembali ke rumah, lakukan isolasi diri |")
            print("| dan Segera hubungi Call Center Posko Tanggap COVID-19 di nomor 112 (Samarinda) untuk mendapat arahan lebih lanjut.      |")
        elif(faq_id == "15"):
            print("| [Apa yang akan terjadi jika tenaga medis profesional menyatakan saya mungkin terjangkit COVID-19?]                      |")
            print("| Jika Anda diduga terjangkit COVID-19, Tim Tanggap COVID-19 akan mengambil beberapa sampel untuk diuji, misalnya:        |")
            print("|                                                                                                                         |")
            print("| *Lendir dari hidung, tenggorokan, atau paru-paru, dan/atau                                                              |")
            print("| *darah                                                                                                                  |")
            print("|                                                                                                                         |")
            print("| Dan, anda akan diisolasi dari orang lain sampai dikonfirmasi apakah Anda negatif terinfeksi coronavirus.                |")
        elif(faq_id == "16"):
            faq_covid()
        else:            
            print("| Error: Pilihan tersebut tidak tersedia!                                                                                 |")
        print("===========================================================================================================================")
        back_to_faq()
    elif(faq == "3"):
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Mencegah Penularan COVID-19                                                                                             |")
        print("===========================================================================================================================")
        print("| [1] Bagaimana mengantisipasi penularan COVID-19?                                                                        |")
        print("| [2] Apakah masker kesehatan dapat mencegah COVID-19?                                                                    |")
        print("| [3] Apakah saya harus selalu menggunakan masker?                                                                        |")
        print("| [4] Haruskan saya khawatir terhadap penyakit COVID-19 ini?                                                              |")
        print("| [5] Apakah antibiotik efektif dalam mencegah atau mengobati COVID-19?                                                   |")
        print("| [6] Seberapa efektif pemindai suhu badan dalam mendeteksi orang yang terjangkit COVID-19?                               |")
        print("| [7] Bagaimana membedakan antara sakit akibat infeksi COVID-19, dengan influenza biasa?                                  |")
        print("| [8] Kembali                                                                                                             |")
        print("===========================================================================================================================")
        faq_id = str(input("Masukkan Pilihan> "))
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Mencegah Penularan COVID-19                                                                                             |")
        print("===========================================================================================================================")
        if(faq_id == "1"):
            print("| [Bagaimana mengantisipasi penularan COVID-19?]                                                                          |")
            print("| Hingga saat ini, belum ada vaksin untuk mencegah penularan COVID-19 tetapi Anda dapat melakukan tindakan pencegahan     |")
            print("| agar tidak tertular. Di antaranya dengan:                                                                               |")
            print("|                                                                                                                         |")
            print("| A. Menjaga kesehatan dan kebugaran agar sistem imunitas/kekebalan tubuh meningkat.                                      |")
            print("| B. Gunakan masker penutup mulut dan hidung ketika Anda berada di luar rumah.                                            |")
            print("| C. Jaga jara aman dengan orang lain minimal 1,5 meter.                                                                  |")
            print("| D. Mencuci tangan menggunakan sabun dan air mengalir atau menggunakan alkohol 70-80% handrub sesuai langkah-langkah     |")
            print("| mencuci tangan yang benar. Mencuci tangan sampai bersih merupakan salah satu tindakan yang mudah dan murah. Dan,        |")
            print("| sebagian besar penyebaran penyakit akibat virus dan bakteri bersumber dari tangan. Karena itu, menjaga kebersihan       |")
            print("| tangan adalah hal yang sangat penting.                                                                                  |")
            print("| E. Ketika batuk dan bersin, upayakan menjaga agar lingkungan Anda tidak tertular. Tutup hidung dan mulut Anda dengan    |")
            print("| tisu atau dengan lipatan siku tangan bagian dalam (bukan dengan telapak tangan) dan gunakan masker.                     |")
            print("| F.  Hindari kontak dengan orang lain atau bepergian ke tempat umum.                                                     |")
            print("| G. Hindari menyentuh mata, hidung dan mulut (segitiga wajah). Tangan menyentuh banyak hal yang dapat terkontaminasi     |")
            print("| virus. Jika kita menyentuh mata, hidung dan mulut dengan tangan yang terkontaminasi, maka virus dapat dengan mudah      |")
            print("| masuk ke tubuh kita.                                                                                                    |")
            print("| H. Buang tisu dan masker yang sudah digunakan ke tempat sampah dengan benar, lalu cucilah tangan Anda.                  |")
            print("| I.  Menunda perjalanan ke daerah/negara di mana virus ini ditemukan.                                                    |")
            print("| J. Hindari bepergian ke luar rumah kecuali untuk kegiatan mendesak.                                                     |")
            print("| K. Selalu pantau perkembangan penyakit COVID-19 dari sumber resmi dan akurat. Ikuti arahan dan informasi dari petugas   |")
            print("| kesehatan dan Dinas Kesehatan setempat. Informasi dari sumber yang tepat dapat membantu Anda melindungi dari Anda dari  |")
            print("| penularan dan penyebaran penyakit ini.                                                                                  |")
        elif(faq_id == "2"):
            print("| [Apakah masker kesehatan dapat mencegah COVID-19?]                                                                      |")
            print("| Iya. Namun, Anda dapat menggunakan masker kain (berlapis 3) karena masker kesehatan dibutuhkan oleh petugas medis.      |")
        elif(faq_id == "3"):
            print("| [Apakah saya harus selalu menggunakan masker?]                                                                          |")
            print("| Iya. Anda wajib untuk selalu menggunakan masker saat berkegiatan di luar rumah. Masker yang digunakan dapat berupa      |")
            print("| masker kain (berlapis 3).                                                                                               |")
        elif(faq_id == "4"):
            print("| [Haruskan saya khawatir terhadap penyakit COVID-19 ini?]                                                                |")
            print("| Anda diminta untuk selalu waspada dan mengikuti imbauan pemerintah. Tetap berada di rumah dan berkegiatan dari rumah    |")
            print("| dan tetap tenang. Carilah informasi yang benar dan akurat tentang perkembangan COVID-19 agar Anda mengetahui situasi    |")
            print("| wilayah Anda dan Anda dapat mengambil tindakan pencegahan yang tepat.                                                   |")
        elif(faq_id == "5"):
            print("| [Apakah antibiotik efektif dalam mencegah atau mengobati COVID-19?]                                                     |")
            print("| Tidak. Antibiotik hanya bekerja untuk melawan bakteri, bukan virus. Karena COVID-19 disebabkan oleh virus, maka         |")
            print("| antibiotik tidak bisa digunakan sebagai sarana pencegahan atau pengobatan. Namun, jika Anda dirawat di rumah sakit dan  |")
            print("| didiagnosis COVID-19, Anda mungkin akan diberikan antibiotik, karena seringkali terjadi infeksi sekunder yang           |")
            print("| disebabkan bakteri.                                                                                                     |")
        elif(faq_id == "6"):
            print("| [Seberapa efektif pemindai suhu badan dalam mendeteksi orang yang terjangkit COVID-19?]                                 |")
            print("| Pemindai suhu tubuh dinilai efektif dalam mendeteksi orang dengan suhu tinggi yang dapat disebabkan oleh coronavirus.   |")
            print("| Tetapi, alat ini tidak dapat mendeteksi orang yang terjangkit COVID-19 dengan gejala suhu tinggi yang tidak ditemukan.  |")
        elif(faq_id == "7"):
            print("| [Bagaimana membedakan antara sakit akibat infeksi COVID-19, dengan influenza biasa?]                                    |")
            print("| Orang yang terinfeksi COVID-19 dan influenza akan mengalami gejala infeksi saluran pernafasan yang sama, seperti demam, |")
            print("| batuk dan pilek. Walaupun gejalanya sama, tapi penyebab virusnya berbeda-beda, sehingga kita sulit mengidentifikasi     |")
            print("| masing-masing penyakit tersebut.                                                                                        |")
            print("|                                                                                                                         |")
            print("| Pemeriksaan medis yang akurat disertai rujukan pemeriksaan laboratorium sangat diperlukan untuk mengonfirmasi apakah    |")
            print("| seseorang terinfeksi COVID-19. Bagi setiap orang yang menderita demam, batuk, dan sulit bernapas sangat                 |")
            print("| direkomendasikan untuk segera mencari pengobatan, dan memberitahukan petugas kesehatan jika mereka telah melakukan      |")
            print("| perjalanan dari wilayah terjangkit dalam 14 hari sebelum muncul gejala, atau jika mereka telah melakukan kontak erat    |")
            print("| dengan seseorang yang sedang menderita gejala infeksi saluran pernafasan.                                               |")
        elif(faq_id == "8"):
            faq_covid()
        else:            
            print("| Error: Pilihan tersebut tidak tersedia!                                                                                 |")
        print("===========================================================================================================================")
        back_to_faq()
    elif(faq == "4"):
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Kasus COVID-19                                                                                                          |")
        print("===========================================================================================================================")
        print("| [1] Berapa banyak orang yang telah terinfeksi oleh COVID-19 dan negara mana saja yang sudah ada kasusnya?               |")
        print("| [2] Apakah di Indonesia sudah ditemukan kasus terinfeksi?                                                               |")
        print("| [3] Bagaimana situasi terkini di Indonesia? Apakah sudah ada kasus konfirmasi COVID-19?                                 |")
        print("| [4] Saya akan bepergian ke luar negeri untuk sesuatu yang mendesak, apakah saya dapat memperoleh Surat Keterangan Bebas |")
        print("|     COVID-19? Di mana?                                                                                                  |")
        print("| [5] Apakah sudah ada pembatasan untuk bepergian ke Tiongkok dan negara terjangkit lainnya?                              |")
        print("| [6] Di manakah saya bisa mendapatkan media edukasi dan informasi serta situasi perkembangan COVID-19?                   |")
        print("| [7] Kembali                                                                                                             |")
        print("===========================================================================================================================")
        faq_id = str(input("Masukkan Pilihan> "))
        clear_screen()
        print("===========================================================================================================================")
        print("|                                                           FAQ                                                           |")
        print("===========================================================================================================================")
        print("| Kasus COVID-19                                                                                                          |")
        print("===========================================================================================================================")
        if(faq_id == "1"):
            print("| [Berapa banyak orang yang telah terinfeksi oleh COVID-19 dan negara mana saja yang sudah ada kasusnya?]                 |")
            print("| WHO secara ketat memantau situasi terkini dan secara teratur menerbitkan informasi tentang penyakit ini. Informasi      |")
            print("| lebih lanjut mengenai penyakit ini dapat dilihat melalui:                                                               |")
            print("| https://www.who.int/emergencies/diseases/novel-coronavirus-2019 atau                                                    |")
            print("| https://infeksiemerging.kemkes.go.id/category/situasi-infeksi-emerging/info-corona-virus                                |")
        elif(faq_id == "2"):
            print("| [Apakah di Indonesia sudah ditemukan kasus terinfeksi?]                                                                 |")
            print("| Anda dapat melihat data terbaru terkait kasus COVID-19 di Indonesia pada portal Kementerian Kesehatan Republik          |")
            print("| Indonesia di https://infeksiemerging.kemkes.go.id/ atau pada menu Data di https://covid19.kaltimprov.go.id/ untuk data  |")
            print("| kasus di Provinsi Kalimantan Timur.                                                                                     |")
        elif(faq_id == "3"):
            print("| [Bagaimana situasi terkini di Indonesia? Apakah sudah ada kasus konfirmasi COVID-19?]                                   |")
            print("| Situasi perkembangan penyakit COVID-19 di Indonesia dapat dipantau melalui laman website                                |")
            print("| https://infeksiemerging.kemkes.go.id atau melalui https://covid19.kaltimprov.go.id/ untuk memantau perkembangan kasus   |")
            print("| di Provinsi Kalimatan Timur.                                                                                            |")
        elif(faq_id == "4"):
            print("| [Saya akan bepergian ke luar negeri untuk sesuatu yang mendesak, apakah saya dapat memperoleh Surat Keterangan Bebas    |")
            print("| COVID-19? Di mana?]                                                                                                     |")
            print("| Untuk kondisi saat ini, seseorang belum bisa diberikan surat keterangan bebas COVID-19, karena kita tidak pernah tahu   |")
            print("| apakah dia pernah kontak dengan orang yang sakit COVID-19.                                                              |")
        elif(faq_id == "5"):
            print("| [Apakah sudah ada pembatasan untuk bepergian ke Tiongkok dan negara terjangkit lainnya?]                                |")
            print("| Sejak 5 Februari 2020, Indonesia telah memberlakukan pembatasan perjalanan ke Tiongkok berupa penghentian sementara     |")
            print("| penerbangan dari dan ke Tiongkok. Pada tanggal 5 Maret 2020, Indonesia juga memberlakukan pelarangan transit atau masuk |")
            print("| ke Indonesia bagi pelaku perjalanan yang dalam 14 hari sebelumnya datang dari wilayah berikut:                          |")
            print("|                                                                                                                         |")
            print("| *Iran: Tehran, Qom, Gilan                                                                                               |")
            print("| *Italia: Wilayah Lombardi, Veneto, Emilia Romagna, Marche dan Piedmont                                                  |")
            print("| *Korea Selatan: Kota Daegu dan Provinsi Gyeongsangbuk-do.                                                               |")
        elif(faq_id == "6"):
            print("| [Di manakah saya bisa mendapatkan media edukasi dan informasi serta situasi perkembangan COVID-19?]                     |")
            print("| Informasi tentang media KIE atau situasi perkembangan COVID-19, dapat diakses melalui:                                  |")
            print("|                                                                                                                         |")
            print("| Halo Kemenkes: 1500567                                                                                                  |")
            print("| Hotline Emergency Operation Center (EOC): 119 atau (021) 521 0411 atau 0812 1212 3119                                   |")
            print("|                                                                                                                         |")
            print("| Twitter: @KemenkesRI                                                                                                    |")
            print("| Facebook: @KementerianKesehatanRI                                                                                       |")
            print("| Instagram: @kemenkes_ri                                                                                                 |")
            print("| Website: www.who.int, www.infeksiemerging.kemkes.go.id, www.sehatnegeriku.kemkes.go.id                                  |")
        elif(faq_id == "7"):
            faq_covid()
        else:            
            print("| Error: Pilihan tersebut tidak tersedia!                                                                                 |")
        print("===========================================================================================================================")
        back_to_faq()
    elif(faq == "5"):
        show_menu()
    else:
        print("===========================================================================================================================")
        print("| Error: Pilihan tersebut tidak tersedia!                                                                                 |")
        print("===========================================================================================================================")
        back_to_faq()

def back_to_faq():
    input("\nTekan Enter untuk kembali...")
    faq_covid()

def tentang_aplikasi():
    clear_screen()
    print("=================================================================")
    print("|                     TENTANG APLIKASI                          |")
    print("=================================================================")
    print("| Nama Aplikasi        : Deteksi Dini Mandiri COVID-19          |")
    print("| Versi                : 1.0                                    |")
    print("| Pengembang           : Andi Alfian Bahtiar  (2009106002)      |")
    print("|                      : Muhammad Gusti Keyandi E. (2009106006) |")
    print("|                      : Ihsan Magribi (2009106107)             |")
    print("|                      : Rena Indah Choirunnisa (2009106126)    |")
    print("| Donasi Pengembangan  : 056301058860507 (BRI)                  |")
    print("|                      : 7995048523 (BCA)                       |")
    print("|                      : 4132282159 (Permata)                   |")
    print("|                      : 1480016496716 (Mandiri)                |")
    print("|                      : 90020219079 (Jenius)                   |")
    print("|                      : 085346816962 (Dana/OVO/Gopay)          |")
    print("|                                                               |")
    print("|      Hak Cipta © 2020 Deteksi Dini Mandiri COVID-19           |")
    print("=================================================================")
    back_to_menu()

def pengaturan_akun():
    clear_screen()
    print("======================================================================")
    print("|                           PENGATURAN AKUN                          |")
    print("======================================================================")
    if(data_akun[0] == "user"):
        print("| [1] Ganti Password                                                 |")
        print("| [2] Ganti Umur                                                     |")
        print("| [3] Ganti No HP                                                    |")
        print("| [4] Ganti Alamat                                                   |")
        print("| [5] Ganti Kelurahan / Desa                                         |")
        print("| [6] Kembali                                                        |")
    elif(data_akun[0] == "dinkes"):
        print("| [1] Ganti Password                                                 |")
        print("| [2] Kembali                                                        |")
    elif(data_akun[0] == "admin"):
        print("| [1] Ganti Password                                                 |")
        print("| [2] Kembali                                                        |")
    print("======================================================================")
    selected_menu = str(input("Pilih menu> "))
    if(data_akun[0] == "user"):
        if(selected_menu == "1"):
            clear_screen()
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan Password lama dan ganti dengan password baru        |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['NAMA'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                passlama = str(input("Password Lama              : "))
                if(data_found['PASSWORD'] == passlama):
                    passbaru = str(input("Password Baru              : "))
                    if(len(passbaru) < 8):
                        print("======================================================================")
                        print("| Error: Password baru minimal 8 huruf!                              |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    konfirpassbaru = str(input("Konfirmasi Password Baru   : "))
                    if(len(konfirpassbaru) < 8):
                        print("======================================================================")
                        print("| Error: Password baru minimal 8 huruf!                              |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    if(passbaru == passlama or konfirpassbaru == passlama):
                        print("======================================================================")
                        print("| Error: Password baru tidak boleh sama dengan password lama         |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    elif(passbaru == konfirpassbaru):
                        indeks = 0
                        for data in akuns:
                            if (data['NAMA'] == data_akun[1]):
                                akuns[indeks]['PASSWORD'] = passbaru
                            indeks = indeks + 1
                        print("======================================================================")
                        print("| Sukses: Password berhasil di update!                               |")
                        print("======================================================================")
                    else:
                        print("======================================================================")
                        print("| Error: Password dan Konfirmasi Password berbeda!                   |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    with open(csv_filename_account, mode="w") as csv_file:
                        fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        for new_data in akuns:
                            writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
                    back_to_menu()
                else:
                    print("======================================================================")
                    print("| Error: Password lama anda salah!                                   |")
                    print("======================================================================")
                    back_to_pengaturan_akun()
        elif(selected_menu == "2"):
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan Umur baru                                           |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['NAMA'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                try:
                    umurbaru = int(input("Umur baru (contoh 18) : "))
                except ValueError:
                    print("======================================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...               |")
                    print("======================================================================")
                    back_to_pengaturan_akun()
                indeks = 0
                for data in akuns:
                    if (data['NAMA'] == data_akun[1]):
                        akuns[indeks]['UMUR'] = umurbaru
                    indeks = indeks + 1
                print("======================================================================")
                print("| Sukses: Umur berhasil di update!                                   |")
                print("======================================================================")
            with open(csv_filename_account, mode="w") as csv_file:
                fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in akuns:
                    writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
            back_to_menu()
        elif(selected_menu == "3"):
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan No HP baru                                          |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['NAMA'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                try:
                    nohpbaru = int(input("No HP baru    : "))
                except ValueError:
                    print("======================================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...               |")
                    print("======================================================================")
                    back_to_pengaturan_akun()
                indeks = 0
                for data in akuns:
                    if (data['NAMA'] == data_akun[1]):
                        akuns[indeks]['NOHP'] = nohpbaru
                    indeks = indeks + 1
                print("======================================================================")
                print("| Sukses: No HP berhasil di update!                                  |")
                print("======================================================================")
            with open(csv_filename_account, mode="w") as csv_file:
                fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in akuns:
                    writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
            back_to_menu()
        elif(selected_menu == "4"):
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan Alamat baru                                         |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['NAMA'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                alamatbaru = str(input("Alamat baru    : "))
                if(len(alamatbaru) < 1):
                    print("========================================================================")
                    print("| Error: Anda tidak dapat mengkosongkan alamat                         |")
                    print("========================================================================")
                    back_to_pengaturan_akun()
                indeks = 0
                for data in akuns:
                    if (data['NAMA'] == data_akun[1]):
                        akuns[indeks]['ALAMAT'] = alamatbaru
                    indeks = indeks + 1
                print("======================================================================")
                print("| Sukses: Alamat berhasil di update!                                 |")
                print("======================================================================")
            with open(csv_filename_account, mode="w") as csv_file:
                fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in akuns:
                    writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
            back_to_menu()
        elif(selected_menu == "5"):
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan Kelurahan / Desa baru                               |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['NAMA'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                alamat2baru = str(input("Kelurahan / Desa baru    : "))
                if(len(alamat2baru) < 1):
                    print("========================================================================")
                    print("| Error: Anda tidak dapat mengkosongkan Kelurahan / Desa               |")
                    print("========================================================================")
                    back_to_pengaturan_akun()
                indeks = 0
                for data in akuns:
                    if (data['NAMA'] == data_akun[1]):
                        akuns[indeks]['ALAMAT2'] = alamat2baru
                    indeks = indeks + 1
                print("======================================================================")
                print("| Sukses: Kelurahan / Desa berhasil di update!                       |")
                print("======================================================================")
            with open(csv_filename_account, mode="w") as csv_file:
                fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for new_data in akuns:
                    writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
            back_to_menu()
        elif(selected_menu == "6"):
            show_menu()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_pengaturan_akun()
    elif(data_akun[0] == "dinkes"):
        if(selected_menu == "1"):
            clear_screen()
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan Password lama dan ganti dengan password baru        |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['NAMA'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                passlama = str(input("Password Lama              : "))
                if(data_found['PASSWORD'] == passlama):
                    passbaru = str(input("Password Baru              : "))
                    if(len(passbaru) < 8):
                        print("======================================================================")
                        print("| Error: Password baru minimal 8 huruf!                              |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    konfirpassbaru = str(input("Konfirmasi Password Baru   : "))
                    if(len(konfirpassbaru) < 8):
                        print("======================================================================")
                        print("| Error: Password baru minimal 8 huruf!                              |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    if(passbaru == passlama or konfirpassbaru == passlama):
                        print("======================================================================")
                        print("| Error: Password baru tidak boleh sama dengan password lama         |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    elif(passbaru == konfirpassbaru):
                        indeks = 0
                        for data in akuns:
                            if (data['NAMA'] == data_akun[1]):
                                akuns[indeks]['PASSWORD'] = passbaru
                            indeks = indeks + 1
                        print("======================================================================")
                        print("| Sukses: Password berhasil di update!                               |")
                        print("======================================================================")
                    else:
                        print("======================================================================")
                        print("| Error: Password dan Konfirmasi Password berbeda!                   |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    with open(csv_filename_account, mode="w") as csv_file:
                        fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        for new_data in akuns:
                            writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
                    back_to_menu()
                else:
                    print("======================================================================")
                    print("| Error: Password lama anda salah!                                   |")
                    print("======================================================================")
                    back_to_pengaturan_akun()
        elif(selected_menu == "2"):
            show_menu()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_pengaturan_akun()
    elif(data_akun[0] == "admin"):
        if(selected_menu == "1"):
            clear_screen()
            print("======================================================================")
            print("|                           PENGATURAN AKUN                          |")
            print("======================================================================")
            print("| Info: Masukkan Password lama dan ganti dengan password baru        |")
            print("======================================================================")
            akuns = []
            with open(csv_filename_account, mode="r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    akuns.append(row)
            data_found = []
            indeks = 0
            for data in akuns:
                if (data['USERNAME'] == data_akun[1]):
                    data_found = akuns[indeks]
                indeks = indeks + 1
            if len(data_found) > 0:
                passlama = str(input("Password Lama              : "))
                if(data_found['PASSWORD'] == passlama):
                    passbaru = str(input("Password Baru              : "))
                    if(len(passbaru) < 8):
                        print("======================================================================")
                        print("| Error: Password baru minimal 8 huruf!                              |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    konfirpassbaru = str(input("Konfirmasi Password Baru   : "))
                    if(len(konfirpassbaru) < 8):
                        print("======================================================================")
                        print("| Error: Password baru minimal 8 huruf!                              |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    if(passbaru == passlama or konfirpassbaru == passlama):
                        print("======================================================================")
                        print("| Error: Password baru tidak boleh sama dengan password lama         |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    elif(passbaru == konfirpassbaru):
                        indeks = 0
                        for data in akuns:
                            if (data['USERNAME'] == data_akun[1]):
                                akuns[indeks]['PASSWORD'] = passbaru
                            indeks = indeks + 1
                        print("======================================================================")
                        print("| Sukses: Password berhasil di update!                               |")
                        print("======================================================================")
                    else:
                        print("======================================================================")
                        print("| Error: Password dan Konfirmasi Password berbeda!                   |")
                        print("======================================================================")
                        back_to_pengaturan_akun()
                    with open(csv_filename_account, mode="w") as csv_file:
                        fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
                        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                        writer.writeheader()
                        for new_data in akuns:
                            writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
                    back_to_menu()
                else:
                    print("======================================================================")
                    print("| Error: Password lama anda salah!                                   |")
                    print("======================================================================")
                    back_to_pengaturan_akun()
        elif(selected_menu == "2"):
            show_menu()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_pengaturan_akun()

def back_to_pengaturan_akun():
    input("\nTekan Enter untuk kembali...")
    pengaturan_akun()

def kritikdansaran():
    clear_screen()
    print("======================================================================")
    print("|                          KRITIK DAN SARAN                          |")
    print("======================================================================")
    if(data_akun[0] == "guest" or data_akun[0] == "user"):
        print("| [1] Developer                                                      |")
        print("| [2] Dinkes                                                         |")
        print("| [3] Kembali                                                        |")
    elif(data_akun[0] == "dinkes"):
        print("| [1] Developer                                                      |")
        print("| [2] Kembali                                                        |")
    print("======================================================================")
    selected_ks = str(input("Pilih Tujuan> "))
    if(data_akun[0] == "guest"):
        if(selected_ks == "1"):
            kritikdansaran_developer()
        elif(selected_ks == "2"):
            kritikdansaran_dinkes()
        elif(selected_ks == "3"):
            show_menu()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_kritikdansaran()
    elif(data_akun[0] == "user"):
        if(selected_ks == "1"):
            kritikdansaran_developer()
        elif(selected_ks == "2"):
            kritikdansaran_dinkes()
        elif(selected_ks == "3"):
            show_menu()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_kritikdansaran()
    elif(data_akun[0] == "dinkes"):
        if(selected_ks == "1"):
            kritikdansaran_developer()
        elif(selected_ks == "2"):
            show_menu()
        else:
            print("======================================================================")
            print("| Error: Anda memilih menu yang salah!                               |")
            print("======================================================================")
            back_to_kritikdansaran()

def back_to_kritikdansaran():
    input("\nTekan Enter untuk kembali...")
    kritikdansaran()

def kritikdansaran_developer():
    clear_screen()
    print("======================================================================")
    print("|                          KRITIK DAN SARAN                          |")
    print("======================================================================")
    print("| Info: Silakan masukan kritik dan saran untuk Developer             |")
    print("======================================================================")
    kritik = str(input("Kritik> "))
    saran = str(input("Saran> "))
    if(data_akun[0] == "guest"):
        with open(csv_filename_kritiksaran, mode='a') as csv_file:
            fieldnames = ['JENIS', 'NAMA', 'KRITIK', 'SARAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'JENIS': "Developer", 'NAMA': "Guest", 'KRITIK': kritik, 'SARAN': saran})
        print("======================================================================")
        print("| Sukses: Kritik dan saran berhasil disimpan!                        |")
        print("======================================================================")
    elif(data_akun[0] == "user"):
        with open(csv_filename_kritiksaran, mode='a') as csv_file:
            fieldnames = ['JENIS', 'NAMA', 'KRITIK', 'SARAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'JENIS': "Developer", 'NAMA': data_akun[1], 'KRITIK': kritik, 'SARAN': saran})
    elif(data_akun[0] == "dinkes"):
        with open(csv_filename_kritiksaran, mode='a') as csv_file:
            fieldnames = ['JENIS', 'NAMA', 'KRITIK', 'SARAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'JENIS': "Developer", 'NAMA': data_akun[1], 'KRITIK': kritik, 'SARAN': saran})
    back_to_menu()

def kritikdansaran_dinkes():
    clear_screen()
    print("======================================================================")
    print("|                          KRITIK DAN SARAN                          |")
    print("======================================================================")
    print("| Info: Silakan masukan kritik dan saran untuk Dinkes                |")
    print("======================================================================")
    kritik = str(input("Kritik> "))
    saran = str(input("Saran> "))
    if(data_akun[0] == "guest"):
        with open(csv_filename_kritiksaran, mode='a') as csv_file:
            fieldnames = ['JENIS', 'NAMA', 'KRITIK', 'SARAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'JENIS': "Dinkes", 'NAMA': "Guest", 'KRITIK': kritik, 'SARAN': saran})
        print("======================================================================")
        print("| Sukses: Kritik dan saran berhasil disimpan!                        |")
        print("======================================================================")
    elif(data_akun[0] == "user"):
        with open(csv_filename_kritiksaran, mode='a') as csv_file:
            fieldnames = ['JENIS', 'NAMA', 'KRITIK', 'SARAN']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'JENIS': "Dinkes", 'NAMA': data_akun[1], 'KRITIK': kritik, 'SARAN': saran})
        print("======================================================================")
        print("| Sukses: Kritik dan saran berhasil disimpan!                        |")
        print("======================================================================")
    back_to_menu()

def show_kritiksaran():
    clear_screen()
    print("==============================================================")
    if(data_akun[0] == "dinkes"):
        print("|                   KRITIK DAN SARAN DINKES                  |")
    elif(data_akun[0] == "admin"):
        print("|                 KRITIK DAN SARAN DEVELOPER                 |")
    print("==============================================================")
    krisan = []
    with open(csv_filename_kritiksaran, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            krisan.append(row)
    for data in krisan:
        if(data_akun[0] == "dinkes"):
            if (data['JENIS'] == "Dinkes"):
                print("| Nama: %s" % data['NAMA'])
                print("| Kritik: %s" % data['KRITIK'])
                print("| Saran: %s" % data['SARAN'])
            else:
                print("==============================================================")
                print("| Error: Tidak ada data ditemukan!                           |")
                print("==============================================================")
        elif(data_akun[0] == "admin"):
            if (data['JENIS'] == "Developer"):
                print("| Nama: %s" % data['NAMA'])
                print("| Kritik: %s" % data['KRITIK'])
                print("| Saran: %s" % data['SARAN'])
            else:
                print("==============================================================")
                print("| Error: Tidak ada data ditemukan!                           |")
                print("==============================================================")
    back_to_menu()

def show_account():
    clear_screen()
    print("==============================================================")
    print("|                    DAFTAR AKUN PENGGUNA                    |")
    print("==============================================================")
    akuns = []
    with open(csv_filename_account, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)
    if (len(akuns) > 0):
        i = 1
        for data in akuns:
            print("| Akun ke-%d" % (i))
            print("| Username           : %s " % (data['USERNAME']))
            print("| Password           : %s " % (data['PASSWORD']))
            print("| Level              : %s " % (data['LEVEL']))
            print("| Nama               : %s " % (data['NAMA']))
            print("| Umur               : %s " % (data['UMUR']))
            print("| No HP              : %s " % (data['NOHP']))
            print("| Alamat             : %s " % (data['ALAMAT']))
            print("| Kelurahan / Desa   : %s " % (data['ALAMAT2']))
            print("==============================================================")
            i += 1
    else:
        print("==============================================================")
        print("| Error: Tidak ada data!                                     |")
        print("==============================================================")
    back_to_menu()

def create_account():
    clear_screen()
    print("========================================================================")
    print("|                          BUAT AKUN PENGGUNA                          |")
    print("========================================================================")
    print("| Info: Silakan isi Nama, Username, Password, dan Kode Unik akun       |")
    print("========================================================================")
    nama = str(input("Nama                : "))
    if(len(nama) < 1):
        print("========================================================================")
        print("| Error: Anda tidak dapat mengkosongkan Nama                           |")
        print("========================================================================")
        back_to_menu()
    try:
        umur = int(input("Umur (Contoh: 18)   : "))
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        back_to_menu()
    try:
        nohp = int(input("No. HP/WA           : "))
    except ValueError:
        print("========================================================================")
        print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...                 |")
        print("========================================================================")
        back_to_menu()
    alamat = str(input("Alamat              : "))
    if(len(alamat) < 1):
        print("========================================================================")
        print("| Error: Anda tidak dapat mengkosongkan Alamat                         |")
        print("========================================================================")
        back_to_menu()
    alamat2 = str(input("Kelurahan / Desa    : "))
    if(len(alamat2) < 1):
        print("========================================================================")
        print("| Error: Anda tidak dapat mengkosongkan Kelurahan / Desa               |")
        print("========================================================================")
        back_to_menu()
    username = str(input("Username            : "))
    if not(len(username) > 3):
        print("========================================================================")
        print("| Error: Username minimal 4 huruf/angka!                               |")
        print("========================================================================")
        show_menu()
    password = str(input("Password            : "))
    if not(len(password) > 7):
        print("========================================================================")
        print("| Error: Password minimal 8 huruf/angka!                               |")
        print("========================================================================")
        show_menu()
    kodeunik = str(input("Kode Unik (jika ada) : "))
    akun = []
    with open(csv_filename_account, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akun.append(row)
    data_found = []
    indeks = 0
    for data in akun:
        if (data['USERNAME'] == username):
            data_found = akun[indeks]
        indeks = indeks + 1
        if(len(data_found) > 0):
            print("========================================================================")
            print("| Error: Akun tersebut telah didaftarkan!                              |")
            print("========================================================================")
            back_to_menu()
    with open(csv_filename_account, mode='a') as csv_file:
        fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if(kodeunik == "admin"):
            writer.writerow({'USERNAME': username, 'PASSWORD': password, 'LEVEL': 'admin', 'NAMA': nama, 'UMUR': umur, 'NOHP': nohp, 'ALAMAT': alamat, 'ALAMAT2': alamat2})
        elif(kodeunik == "dinkes"):
            writer.writerow({'USERNAME': username, 'PASSWORD': password, 'LEVEL': 'dinkes', 'NAMA': nama, 'UMUR': umur, 'NOHP': nohp, 'ALAMAT': alamat, 'ALAMAT2': alamat2})
        else:
            writer.writerow({'USERNAME': username, 'PASSWORD': password, 'LEVEL': 'user', 'NAMA': nama, 'UMUR': umur, 'NOHP': nohp, 'ALAMAT': alamat, 'ALAMAT2': alamat2})
        print("========================================================================")
        print("| Sukses: Akun Baru berhasil dibuat dan disimpan!                      |")
        print("========================================================================")
    back_to_menu()

def edit_account():
    clear_screen()
    print("==============================================================")
    print("|                     EDIT AKUN PENGGUNA                     |")
    print("==============================================================")
    akuns = []
    with open(csv_filename_account, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)
    i = 1
    for data in akuns:
        print("| Akun ke-%d" % (i))
        print("| Username           : %s " % (data['USERNAME']))
        print("| Password           : %s " % (data['PASSWORD']))
        print("| Level              : %s " % (data['LEVEL']))
        print("| Nama               : %s " % (data['NAMA']))
        print("| Umur               : %s " % (data['UMUR']))
        print("| No HP              : %s " % (data['NOHP']))
        print("| Alamat             : %s " % (data['ALAMAT']))
        print("| Kelurahan / Desa   : %s " % (data['ALAMAT2']))
        print("==============================================================")
        i += 1
    username = str(input("\nMasukkan Username> "))
    if not(data['USERNAME'] == username):
        print("==============================================================")
        print("| Error: Username tidak ditemukan!                           |")
        print("==============================================================")
    indeks = 0
    for data in akuns:
        if (data['USERNAME'] == username):
            print("==============================================================")
            print("| Sukses: Data Akun ditemukan!                               |")
            print("==============================================================")
            password = str(input("\nPassword baru                  : "))
            if(len(password) < 8):
                print("==============================================================")
                print("| Error: Password minimal 8 huruf/angka!                     |")
                print("==============================================================")
                back_to_menu()
            level = str(input("Level baru (admin/dinkes/user) : "))
            if not(level == "admin" or level == "dinkes" or level == "user"):
                print("==============================================================")
                print("| Error: Level tidak tersedia!                               |")
                print("==============================================================")
                back_to_menu()
            nama = str(input("Nama baru                      : "))
            if(len(nama) < 1):
                print("==============================================================")
                print("| Error: Anda tidak dapat mengkosongkan Nama                 |")
                print("==============================================================")
                back_to_menu()
            try:
                umur = int(input("Umur baru                      : "))
            except ValueError:
                print("==============================================================")
                print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                print("==============================================================")
                back_to_menu()
            try:
                nohp = int(input("No HP baru                     : "))
            except ValueError:
                print("==============================================================")
                print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                print("==============================================================")
                back_to_menu()
            alamat = str(input("Alamat baru                    : "))
            if(len(alamat) < 1):
                print("==============================================================")
                print("| Error: Anda tidak dapat mengkosongkan Alamat               |")
                print("==============================================================")
                back_to_menu()
            alamat2 = str(input("Kelurahan / Desa baru          : "))
            if(len(alamat2) < 1):
                print("==============================================================")
                print("| Error: Anda tidak dapat mengkosongkan Kelurahan / Desa     |")
                print("==============================================================")
                back_to_menu()
            akuns[indeks]['PASSWORD'] = password
            akuns[indeks]['LEVEL'] = level
            akuns[indeks]['NAMA'] = nama
            akuns[indeks]['UMUR'] = umur
            akuns[indeks]['NOHP'] = nohp
            akuns[indeks]['ALAMAT'] = alamat
            akuns[indeks]['ALAMAT2'] = alamat2
            print("==============================================================")
            print("| Sukses: Akun berhasil di update!                           |")
            print("==============================================================")
        indeks = indeks + 1
    with open(csv_filename_account, mode="w") as csv_file:
        fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in akuns:
            writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
    back_to_menu()

def delete_account():
    clear_screen()
    print("==============================================================")
    print("|                     HAPUS AKUN PENGGUNA                    |")
    print("==============================================================")
    akuns = []
    with open(csv_filename_account, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)
    i = 1
    for data in akuns:
        print("| Akun ke-%d" % (i))
        print("| Username           : %s " % (data['USERNAME']))
        print("| Password           : %s " % (data['PASSWORD']))
        print("| Level              : %s " % (data['LEVEL']))
        print("| Nama               : %s " % (data['NAMA']))
        print("| Umur               : %s " % (data['UMUR']))
        print("| No HP              : %s " % (data['NOHP']))
        print("| Alamat             : %s " % (data['ALAMAT']))
        print("| Kelurahan / Desa   : %s " % (data['ALAMAT2']))
        print("==============================================================")
        i += 1
    username = str(input("\nMasukkan Username> "))
    if not(data['USERNAME'] == username):
        print("==============================================================")
        print("| Error: Username tidak ditemukan!                           |")
        print("==============================================================")
    indeks = 0
    for data in akuns:
        if (username == data_akun[1]):
            print("==============================================================")
            print("| Error: Anda tidak dapat menghapus diri anda sendiri!       |")
            print("==============================================================")
            break
        else:
            if (data['USERNAME'] == username):
                print("==============================================================")
                print("| Sukses: Data Akun ditemukan!                               |")
                print("==============================================================")
                akuns.remove(akuns[indeks])
                print("==============================================================")
                print("| Sukses: Akun berhasil di hapus!                            |")
                print("==============================================================")
            indeks = indeks + 1
    with open(csv_filename_account, mode="w") as csv_file:
        fieldnames = ['USERNAME', 'PASSWORD', 'LEVEL', 'NAMA', 'UMUR', 'NOHP', 'ALAMAT', 'ALAMAT2']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in akuns:
            writer.writerow({'USERNAME': new_data['USERNAME'], 'PASSWORD': new_data['PASSWORD'], 'LEVEL': new_data['LEVEL'], 'NAMA': new_data['NAMA'], 'UMUR': new_data['UMUR'], 'NOHP': new_data['NOHP'], 'ALAMAT': new_data['ALAMAT'], 'ALAMAT2': new_data['ALAMAT2']})
    back_to_menu()

def search_account():
    clear_screen()
    print("==============================================================")
    print("|                      CARI AKUN PENGGUNA                    |")
    print("==============================================================")
    akuns = []
    with open(csv_filename_account, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            akuns.append(row)
    username = input("\nCari berdasarkan username> ")
    data_found = []
    indeks = 0
    for data in akuns:
        if (data['USERNAME'] == username):
            data_found = akuns[indeks]
        indeks = indeks + 1
    if len(data_found) > 0:
        print("==============================================================")
        print("| Sukses: Data Akun ditemukan!                               |")
        print("==============================================================")
        print("| Username           : %s " % (data_found['USERNAME']))
        print("| Password           : %s " % (data_found['PASSWORD']))
        print("| Level              : %s " % (data_found['LEVEL']))
        print("| Nama               : %s " % (data_found['NAMA']))
        print("| Umur               : %s " % (data_found['UMUR']))
        print("| No HP              : %s " % (data_found['NOHP']))
        print("| Alamat             : %s " % (data_found['ALAMAT']))
        print("| Kelurahan / Desa   : %s " % (data_found['ALAMAT2']))
        print("==============================================================")
    else:
        print("==============================================================")
        print("| Error: Username tidak ditemukan!                           |")
        print("==============================================================")
    back_to_menu()

def update_data_covid(tingkat):
    clear_screen()
    print("==============================================================")
    if(tingkat == "Dunia"):
        print("|                   UPDATE DATA COVID DUNIA                  |")
    if(tingkat == "Indonesia"):
        print("|                 UPDATE DATA COVID INDONESIA                |")
    if(tingkat == "Kaltim"):
        print("|                  UPDATE DATA COVID KALTIM                  |")
    if(tingkat == "Samarinda"):
        print("|                 UPDATE DATA COVID SAMARINDA                |")
    print("==============================================================")
    print("| Info : Isi 'q' untuk membatalkan dan kembali ke menu       |")
    print("==============================================================")
    covids = []
    with open(csv_filename_covid, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            covids.append(row)
    for data in covids:
        if(data['JENIS'] == "Dunia" and tingkat == "Dunia"):
            print("| Data Covid %s" % (data['JENIS']))
            print("| Update Terakhir      : %s" % data["TANGGAL"])
            print("| Terkonfirmasi        : %d" % int(data["TERKONFIRMASI"]))
            print("| Meninggal            : %d" % int(data["MENINGGAL"]))
            print("==============================================================")
        elif(data['JENIS'] == "Indonesia" and tingkat == "Indonesia"):
            print("| Data Covid %s" % (data['JENIS']))
            print("| Update Terakhir      : %s" % data["TANGGAL"])
            print("| Terkonfirmasi        : %d" % int(data["TERKONFIRMASI"]))
            print("| Kasus Aktif          : %d" % int(data["KASUS_AKTIF"]))
            print("| Sembuh               : %d" % int(data["SEMBUH"]))
            print("| Meninggal            : %d" % int(data["MENINGGAL"]))
            print("| Suspek               : %d" % int(data["SUSPEK"]))
            print("| Probable             : %d" % int(data["PROBABLE"]))
            print("==============================================================")
        elif(data['JENIS'] == "Kaltim" and tingkat == "Kaltim"):
            print("| Data Covid %s" % (data['JENIS']))
            print("| Update Terakhir      : %s" % data["TANGGAL"])
            print("| Terkonfirmasi        : %d" % int(data["TERKONFIRMASI"]))
            print("| Dirawat              : %d" % int(data["KASUS_AKTIF"]))
            print("| Sembuh               : %d" % int(data["SEMBUH"]))
            print("| Meninggal            : %d" % int(data["MENINGGAL"]))
            print("| Suspek               : %d" % int(data["SUSPEK"]))
            print("| Discarded            : %d" % int(data["DISCARDED"]))
            print("| Probable             : %d" % int(data["PROBABLE"]))
            print("| Menunggu Hasil Lab   : %d" % int(data["MENUNGGU_HASIL_LAB"]))
            print("==============================================================")
        elif(data['JENIS'] == "Samarinda" and tingkat == "Samarinda"):
            print("| Data Covid %s" % (data['JENIS']))
            print("| Update Terakhir      : %s" % data["TANGGAL"])
            print("| Terkonfirmasi        : %d" % int(data["TERKONFIRMASI"]))
            print("| Dirawat              : %d" % int(data["KASUS_AKTIF"]))
            print("| Sembuh               : %d" % int(data["SEMBUH"]))
            print("| Meninggal            : %d" % int(data["MENINGGAL"]))
            print("| Suspek               : %d" % int(data["SUSPEK"]))
            print("| Discarded            : %d" % int(data["DISCARDED"]))
            print("| Probable             : %d" % int(data["PROBABLE"]))
            print("| Menunggu Hasil Lab   : %d" % int(data["MENUNGGU_HASIL_LAB"]))
            print("==============================================================")
    indeks = 0
    for data in covids:
        if (data['JENIS'] == tingkat):
            if(data['JENIS'] == "Dunia"):
                update_terakhir = str(input("Update Terakhir baru   : "))
                try:
                    terkonfirmasi = int(input("Terkonfirmasi baru     : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    meninggal = int(input("Meninggal baru         : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                covids[indeks]['TANGGAL'] = update_terakhir
                covids[indeks]['TERKONFIRMASI'] = terkonfirmasi
                covids[indeks]['MENINGGAL'] = meninggal
                print("==============================================================")
                print("| Sukses: Data Covid berhasil di update!                     |")
                print("==============================================================")
            elif(data['JENIS'] == "Indonesia"):
                update_terakhir = str(input("\nUpdate Terakhir baru   : "))
                try:
                    terkonfirmasi = int(input("Terkonfirmasi baru     : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    kasus_aktif = int(input("Kasus Aktif baru       : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    sembuh = int(input("Sembuh baru            : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    meninggal = int(input("Meninggal baru         : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    suspek = int(input("Suspek baru            : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    probable = int(input("Probable baru          : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                covids[indeks]['TANGGAL'] = update_terakhir
                covids[indeks]['TERKONFIRMASI'] = terkonfirmasi
                covids[indeks]['KASUS_AKTIF'] = kasus_aktif
                covids[indeks]['SEMBUH'] = sembuh
                covids[indeks]['MENINGGAL'] = meninggal
                covids[indeks]['SUSPEK'] = suspek
                covids[indeks]['PROBABLE'] = probable
                print("==============================================================")
                print("| Sukses: Data Covid berhasil di update!                     |")
                print("==============================================================")
            elif(data['JENIS'] == "Kaltim" or data['JENIS'] == "Samarinda"):
                update_terakhir = str(input("\nUpdate Terakhir baru       : "))
                try:
                    terkonfirmasi = int(input("Terkonfirmasi baru         : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    kasus_aktif = int(input("Dirawat baru               : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    sembuh = int(input("Sembuh baru                : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    meninggal = int(input("Meninggal baru             : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    suspek = int(input("Suspek baru                : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    discarded = int(input("Discarded baru             : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    probable = int(input("Probable baru              : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                try:
                    menunggu_hasil_lab = int(input("Menunggu Hasil Lab baru    : "))
                except ValueError:
                    print("==============================================================")
                    print("| Error: Ups! Itu bukan nomor yang valid. Coba lagi...       |")
                    print("==============================================================")
                    back_to_menu()
                covids[indeks]['TANGGAL'] = update_terakhir
                covids[indeks]['TERKONFIRMASI'] = terkonfirmasi
                covids[indeks]['KASUS_AKTIF'] = kasus_aktif
                covids[indeks]['SEMBUH'] = sembuh
                covids[indeks]['MENINGGAL'] = meninggal
                covids[indeks]['SUSPEK'] = suspek
                covids[indeks]['DISCARDED'] = discarded
                covids[indeks]['PROBABLE'] = probable
                covids[indeks]['MENUNGGU_HASIL_LAB'] = menunggu_hasil_lab
                print("==============================================================")
                print("| Sukses: Data Covid berhasil di update!                     |")
                print("==============================================================")
        indeks = indeks + 1
    with open(csv_filename_covid, mode="w") as csv_file:
        fieldnames = ['JENIS','TANGGAL','TERKONFIRMASI','KASUS_AKTIF','SEMBUH','MENINGGAL','SUSPEK','DISCARDED','PROBABLE','MENUNGGU_HASIL_LAB']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in covids:
            writer.writerow({'JENIS': new_data['JENIS'], 'TANGGAL': new_data['TANGGAL'], 'TERKONFIRMASI': new_data['TERKONFIRMASI'], 'KASUS_AKTIF': new_data['KASUS_AKTIF'], 'SEMBUH': new_data['SEMBUH'], 'MENINGGAL': new_data['MENINGGAL'], 'SUSPEK': new_data['SUSPEK'], 'DISCARDED': new_data['DISCARDED'], 'PROBABLE': new_data['PROBABLE'], 'MENUNGGU_HASIL_LAB': new_data['MENUNGGU_HASIL_LAB']})
    back_to_menu()

def cekpilihan(jenis):
    if(jenis == "DEMAM"):
        if not(data_deteksi[0] == "1" or data_deteksi[0] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            DEMAM = str(input("Pilihan anda: "))
            data_deteksi.pop(0)
            data_deteksi.insert(0,DEMAM)
            cekpilihan("DEMAM")
    elif(jenis == "BATUK"):
        if not(data_deteksi[1] == "1" or data_deteksi[1] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            BATUK = str(input("Pilihan anda: "))
            data_deteksi.pop(1)
            data_deteksi.insert(1,BATUK)
            cekpilihan("BATUk")
    elif(jenis == "NAFAS"):
        if not(data_deteksi[2] == "1" or data_deteksi[2] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            NAFAS = str(input("Pilihan anda: "))
            data_deteksi.pop(2)
            data_deteksi.insert(2,NAFAS)
            cekpilihan("NAFAS")
    elif(jenis == "NYERI"):
        if not(data_deteksi[3] == "1" or data_deteksi[3] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            NYERI = str(input("Pilihan anda: "))
            data_deteksi.pop(3)
            data_deteksi.insert(3,NYERI)
            cekpilihan("NYERI")
    elif(jenis == "LAMA"):
        if not(data_deteksi[4] == "1" or data_deteksi[4] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            LAMA = str(input("Pilihan anda: "))
            data_deteksi.pop(4)
            data_deteksi.insert(4,LAMA)
            cekpilihan("LAMA")
    elif(jenis == "KONTAK"):
        if not(data_deteksi[5] == "1" or data_deteksi[5] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            KONTAK = str(input("Pilihan anda: "))
            data_deteksi.pop(5)
            data_deteksi.insert(5,KONTAK)
            cekpilihan("KONTAK")
    elif(jenis == "JALAN"):
        if not(data_deteksi[6] == "1" or data_deteksi[6] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            JALAN = str(input("Pilihan anda: "))
            data_deteksi.pop(6)
            data_deteksi.insert(6,JALAN)
            cekpilihan("JALAN")
    elif(jenis == "AREA"):
        if not(data_deteksi[7] == "1" or data_deteksi[7] == "2"):
            print("==================================================================================")
            print("| Error: Pilihan anda salah!                                                     |")
            print("| [1] Ya                                                                         |")
            print("| [2] Tidak                                                                      |")
            print("==================================================================================")
            AREA = str(input("Pilihan anda: "))
            data_deteksi.pop(7)
            data_deteksi.insert(7,AREA)
            cekpilihan("AREA")

if __name__ == "__main__":
    check_file()
    while True:
        show_auth()
