import os
import time

#Biodata
biodata = ['Undefined', 'Undefined', '0', '0.0', 'Undefined']

#SmartHome
smarthome = ['0','0','0','0','0']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("-----------------------------------------------")
    print("\t\tAplikasi Bebas")
    print("\tDibuat oleh Andi Alfian Bahtiar")
    print("-----------------------------------------------")
    print("[1] Biodata")
    print("[2] SmartHome")
    print("[3] Operasi Aritmatika")
    print("[4] Operasi Perbandingan")
    print("[5] Operasi Penugasan")
    print("[6] Tentang Aplikasi")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        show_menu_biodata()
    elif(selected_menu == "2"):
        show_menu_smarthome()
    elif(selected_menu == "3"):
        show_menu_aritmatika()
    elif(selected_menu == "4"):
        show_menu_perbandingan()
    elif(selected_menu == "5"):
        show_menu_penugasan()
    elif (selected_menu == "6"):
        tentang_aplikasi()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def show_menu_biodata():
    clear_screen()
    print("----------------------------")
    print("\tMENU BIODATA")
    print("----------------------------")
    print("[1] Nama Lengkap")
    print("[2] Alamat")
    print("[3] Umur")
    print("[4] Tinggi")
    print("[5] Menikah")
    print("[6] Mencetak")
    print("[7] Kembali")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        biodata_nama()
    elif(selected_menu == "2"):
        biodata_alamat()
    elif(selected_menu == "3"):
        biodata_umur()
    elif (selected_menu == "4"):
        biodata_tinggi()
    elif (selected_menu == "5"):
        biodata_menikah()
    elif (selected_menu == "6"):
        biodata_mencetak()
    elif (selected_menu == "7"):
        show_menu()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def show_menu_smarthome():
    clear_screen()
    print("------------------------------")
    print("\tMENU SMARTHOME")
    print("------------------------------")
    print("[1] Lampu")
    print("[2] Listrik")
    print("[3] Jendela")
    print("[4] Pintu")
    print("[5] Stop Kontak")
    print("[6] Status")
    print("[7] Kembali")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        smarthome_lampu()
    elif(selected_menu == "2"):
        smarthome_listrik()
    elif(selected_menu == "3"):
        smarthome_jendela()
    elif (selected_menu == "4"):
        smarthome_pintu()
    elif (selected_menu == "5"):
        smarthome_stopkontak()
    elif (selected_menu == "6"):
        smarthome_status()
    elif (selected_menu == "7"):
        show_menu()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def show_menu_aritmatika():
    clear_screen()
    print("---------------------------------------")
    print("\tMENU OPERASI ARITMATIKA")
    print("---------------------------------------")
    print("[1] Operator Penjumlahan")
    print("[2] Operator Pengurangan")
    print("[3] Operator Perkalian")
    print("[4] Operator Pembagian")
    print("[5] Operator Sisa Bagi")
    print("[6] Operator Pangkat")
    print("[7] Kembali")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        operator_penjumlahan()
    elif(selected_menu == "2"):
        operator_pengurangan()
    elif(selected_menu == "3"):
        operator_perkalian()
    elif (selected_menu == "4"):
        operator_pembagian()
    elif (selected_menu == "5"):
        operator_sisabagi()
    elif (selected_menu == "6"):
        operator_pangkat()
    elif (selected_menu == "7"):
        show_menu()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def show_menu_perbandingan():
    clear_screen()
    print("-----------------------------------------------")
    print("\t   MENU OPERASI PERBANDINGAN")
    print("-----------------------------------------------")
    print("[1] Operator Lebih besar atu sama dengan (>=)")
    print("[2] Operator Lebih kecil atau sama dengan (<=)")
    print("[3] Operator Tidak sama dengan (!=)")
    print("[4] Operator Lebih kecil (<)")
    print("[5] Operator Lebih besar (>)")
    print("[6] Operator Sama dengan (==)")
    print("[7] Kembali")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        operator_lebihbesarsama()
    elif(selected_menu == "2"):
        operator_lebihkecilsama()
    elif(selected_menu == "3"):
        operator_tidaksama()
    elif (selected_menu == "4"):
        operator_lebihkecil()
    elif (selected_menu == "5"):
        operator_lebihbesar()
    elif (selected_menu == "6"):
        operator_samadengan()
    elif (selected_menu == "7"):
        show_menu()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()

def show_menu_penugasan():
    clear_screen()
    print("--------------------------------------")
    print("\tMENU OPERASI PENUGASAN")
    print("--------------------------------------")
    print("[1] Operator *=")
    print("[2] Operator /=")
    print("[3] Operator %=")
    print("[4] Operator +=")
    print("[5] Operator -=")
    print("[6] Kembali")
    print("[0] Keluar")
    selected_menu = str(input("Pilih menu> "))

    if(selected_menu == "1"):
        operator_kalisama()
    elif(selected_menu == "2"):
        operator_bagisama()
    elif(selected_menu == "3"):
        operator_modulussama()
    elif (selected_menu == "4"):
        operator_tambahsama()
    elif (selected_menu == "5"):
        operator_kurangsama()
    elif (selected_menu == "6"):
        show_menu()
    elif (selected_menu == "0"):
        close_app()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
        
def close_app():
    clear_screen()
    print("-------------------------------------------------------------")
    print("\tTerima kasih telah menggunakan Aplikasi Bebas")
    print("-------------------------------------------------------------")
    time.sleep(3)
    exit()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()
    
def back_to_biodata():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_biodata()

def back_to_smarthome():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_smarthome()

def back_to_menu_aritmatika():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_aritmatika()

def back_to_menu_perbandingan():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_perbandingan()

def back_to_menu_penugasan():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu_penugasan()

def biodata_nama():
    clear_screen()
    print("-"*55)
    print("\t\t\tBIODATA")
    print("-"*55)
    insert_nama = str(input("Masukkan Nama Lengkap Anda: "))
    print("Nama Lengkap: %s" % (insert_nama))
    biodata.pop(0)
    biodata.insert(0,insert_nama)
    cek = str(input("Apakah Nama Lengkap sudah benar? ('Y' untuk menyimpan): "))
    if(cek == "Y"):
        back_to_biodata()
    else:
        biodata_nama()

def biodata_alamat():
    clear_screen()
    print("-"*55)
    print("\t\t\tBIODATA")
    print("-"*55)
    insert_alamat = str(input("Masukkan Alamat Anda: "))
    print("Alamat: %s" % (insert_alamat))
    biodata.pop(1)
    biodata.insert(1,insert_alamat)
    cek = str(input("Apakah Alamat sudah benar? ('Y' untuk menyimpan): "))
    if(cek == "Y"):
        back_to_biodata()
    else:
        biodata_alamat()

def biodata_umur():
    clear_screen()
    print("-"*55)
    print("\t\t\tBIODATA")
    print("-"*55)
    insert_umur = int(input("Masukkan Umur Anda (Contoh: 18): "))
    print("Umur: %d" % (insert_umur))
    biodata.pop(2)
    biodata.insert(2,insert_umur)
    cek = str(input("Apakah Umur sudah benar? ('Y' untuk menyimpan): "))
    if(cek == "Y"):
        back_to_biodata()
    else:
        biodata_umur()

def biodata_tinggi():
    clear_screen()
    print("-"*55)
    print("\t\t\tBIODATA")
    print("-"*55)
    insert_tinggi = float(input("Masukkan Tinggi Anda (170.5) Anda: "))
    print("Tinggi: %0.1f" % (insert_tinggi))
    biodata.pop(3)
    biodata.insert(3,insert_tinggi)
    cek = str(input("\nApakah Tinggi sudah benar? ('Y' untuk menyimpan): "))
    if(cek == "Y"):
        back_to_biodata()
    else:
        biodata_tinggi()

def biodata_menikah():
    clear_screen()
    print("-"*55)
    print("\t\t\tBIODATA")
    print("-"*55)
    print("Apakah Anda Menikah?")
    print("1. Ya")
    print("2. Tidak")
    insert_menikah = str(input("Pilih Pilihan> "))
    if(insert_menikah == "1" or insert_menikah == "2"):
        if(insert_menikah == "1"):
            print("Status: Menikah")
            biodata.pop(4)
            biodata.insert(4,"Menikah")
        elif(insert_menikah == "2"):
            print("Status: Belum Menikah")
            biodata.pop(4)
            biodata.insert(4,"Belum Menikah")
        cek = str(input("Apakah Status sudah benar? ('Y' untuk menyimpan): "))
        if(cek == "Y"):
            back_to_biodata()
        else:
            biodata_menikah()
    else:
        print("Kamu memilih pilihan yang salah!")
        biodata_menikah()

def biodata_mencetak():
    clear_screen()
    print("-"*55)
    print("\t\t\tBIODATA")
    print("-"*55)
    print("Nama Lengkap: %s" % (biodata[0]))
    print("Alamat: %s" % (biodata[1]))
    print("Umur: %s" % (biodata[2]))
    print("Tinggi: %s" % (biodata[3]))
    print("Status: %s" % (biodata[4]))
    back_to_biodata()

def smarthome_lampu():
    clear_screen()
    print("-"*73)
    print("\t\t\t\tSMARTHOME")
    print("-"*73)
    if(smarthome[0] == "1"):
        lampu_str = "Menyala (True)"
    else:
        lampu_str = "Mati (False)"
    print("Lampu: %s" % (lampu_str))
    if(smarthome[0] == "1"):
        insert_lampu = str(input("Apakah Anda ingin mematikan Lampu? ('Y' untuk menyimpan): "))     
        if(insert_lampu == "Y"):
            smarthome.pop(0)
            smarthome.insert(0,"0")
            back_to_smarthome()
        else:
            smarthome_lampu()
    else:
        insert_lampu = str(input("Apakah Anda ingin menyalakan Lampu? ('Y' untuk menyimpan): "))
        if(insert_lampu == "Y"):
            smarthome.pop(0)
            smarthome.insert(0,"1")
            back_to_smarthome()
        else:
            smarthome_lampu()

def smarthome_listrik():
    clear_screen()
    print("-"*73)
    print("\t\t\t\tSMARTHOME")
    print("-"*73)
    if(smarthome[1] == "1"):
        listrik_str = "Menyala (True)"
    else:
        listrik_str = "Mati (False)"
    print("Listrik: %s" % (listrik_str))
    if(smarthome[1] == "1"):
        insert_listrik = str(input("Apakah Anda ingin mematikan Listrik? ('Y' untuk menyimpan): "))     
        if(insert_listrik == "Y"):
            smarthome.pop(1)
            smarthome.insert(1,"0")
            back_to_smarthome()
        else:
            smarthome_listrik()
    else:
        insert_listrik = str(input("Apakah Anda ingin menyalakan Listrik? ('Y' untuk menyimpan): "))     
        if(insert_listrik == "Y"):
            smarthome.pop(1)
            smarthome.insert(1,"1")
            back_to_smarthome()
        else:
            smarthome_listrik()

def smarthome_jendela():
    clear_screen()
    print("-"*73)
    print("\t\t\t\tSMARTHOME")
    print("-"*73)
    if(smarthome[2] == "1"):
        jendela_str = "Terbuka (True)"
    else:
        jendela_str = "Tertutup (False)"
    print("Jendela: %s" % (jendela_str))
    if(smarthome[2] == "1"):
        insert_jendela = str(input("Apakah Anda ingin menutup Jendela? ('Y' untuk menyimpan): "))     
        if(insert_jendela == "Y"):
            smarthome.pop(2)
            smarthome.insert(2,"0")
            back_to_smarthome()
        else:
            smarthome_jendela()
    else:
        insert_jendela = str(input("Apakah Anda ingin membuka Jendela? ('Y' untuk menyimpan): "))     
        if(insert_jendela == "Y"):
            smarthome.pop(2)
            smarthome.insert(2,"1")
            back_to_smarthome()
        else:
            smarthome_jendela()

def smarthome_pintu():
    clear_screen()
    print("-"*73)
    print("\t\t\t\tSMARTHOME")
    print("-"*73)
    if(smarthome[3] == "1"):
        pintu_str = "Terbuka (True)"
    else:
        pintu_str = "Tertutup (False)"
    print("Pintu: %s" % (pintu_str))
    if(smarthome[3] == "1"):
        insert_pintu = str(input("Apakah Anda ingin menutup Pintu? ('Y' untuk menyimpan): "))     
        if(insert_pintu == "Y"):
            smarthome.pop(3)
            smarthome.insert(3,"0")
            back_to_smarthome()
        else:
            smarthome_pintu()
    else:
        insert_pintu = str(input("Apakah Anda ingin membuka Pintu? ('Y' untuk menyimpan): "))     
        if(insert_pintu == "Y"):
            smarthome.pop(3)
            smarthome.insert(0,"1")
            back_to_smarthome()
        else:
            smarthome_pintu()

def smarthome_stopkontak():
    clear_screen()
    print("-"*73)
    print("\t\t\t\tSMARTHOME")
    print("-"*73)
    if(smarthome[4] == "1"):
        stopkontak_str = "Menyala (True)"
    else:
        stopkontak_str = "Mati (False)"
    print("Stop Kontak: %s" % (stopkontak_str))
    if(smarthome[4] == "1"):
        insert_stopkontak = str(input("Apakah Anda ingin mematikan Stop Kontak? ('Y' untuk menyimpan): "))     
        if(insert_stopkontak == "Y"):
            smarthome.pop(4)
            smarthome.insert(4,"0")
            back_to_smarthome()
        else:
            smarthome_stopkontak()
    else:
        insert_stopkontak = str(input("Apakah Anda ingin menyalakan Stop Kontak? ('Y' untuk menyimpan): "))     
        if(insert_stopkontak == "Y"):
            smarthome.pop(4)
            smarthome.insert(4,"1")
            back_to_smarthome()
        else:
            smarthome_stopkontak()

def smarthome_status():
    clear_screen()
    print("-"*73)
    print("\t\t\t\tSMARTHOME")
    print("-"*73)
    if(smarthome[0] == "1"):
        lampu_str = "Menyala (True)"
    else:
        lampu_str = "Mati (False)"

    if(smarthome[1] == "1"):
        listrik_str = "Menyala (True)"
    else:
        listrik_str = "Mati (False)"

    if(smarthome[2] == "1"):
        jendela_str = "Terbuka (True)"
    else:
        jendela_str = "Tertutup (False)"

    if(smarthome[3] == "1"):
        pintu_str = "Terbuka (True)"
    else:
        pintu_str = "Tertutup (False)"

    if(smarthome[4] == "1"):
        stopkontak_str = "Menyala (True)"
    else:
        stopkontak_str = "Mati (False)"

    print("Lampu: %s" % (lampu_str))
    print("Listik: %s" % (listrik_str))
    print("Jendela: %s" % (jendela_str))
    print("Pintu: %s" % (pintu_str))
    print("Stop Kontak: %s" % (stopkontak_str))
    back_to_smarthome()

def operator_penjumlahan():
    clear_screen()
    print("-"*35)
    print("\tOPERATOR ARITMATIKA")
    print("-"*35)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a + b
    print("Hasil %d + %d = %d" % (a,b,c))
    back_to_menu_aritmatika()

def operator_pengurangan():
    clear_screen()
    print("-"*35)
    print("\tOPERATOR ARITMATIKA")
    print("-"*35)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a - b
    print("Hasil %d - %d = %d" % (a,b,c))
    back_to_menu_aritmatika()

def operator_perkalian():
    clear_screen()
    print("-"*35)
    print("\tOPERATOR ARITMATIKA")
    print("-"*35)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a * b
    print("Hasil %d * %d = %d" % (a,b,c))
    back_to_menu_aritmatika()

def operator_pembagian():
    clear_screen()
    print("-"*35)
    print("\tOPERATOR ARITMATIKA")
    print("-"*35)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a / b
    print("Hasil %d / %d = %d" % (a,b,c))
    back_to_menu_aritmatika()

def operator_sisabagi():
    clear_screen()
    print("-"*35)
    print("\tOPERATOR ARITMATIKA")
    print("-"*35)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a % b
    print("Hasil %d %% %d = %d" % (a,b,c))
    back_to_menu_aritmatika()

def operator_pangkat():
    clear_screen()
    print("-"*35)
    print("\tOPERATOR ARITMATIKA")
    print("-"*35)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a ** b
    print("Hasil %d ** %d = %d" % (a,b,c))
    back_to_menu_aritmatika()

def operator_lebihbesarsama():
    clear_screen()
    print("-"*37)
    print("\tOPERATOR PERBANDINGAN")
    print("-"*37)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a >= b
    print("Hasil %d >= %d = %s" % (a,b,c))
    back_to_menu_perbandingan()

def operator_lebihkecilsama():
    clear_screen()
    print("-"*37)
    print("\tOPERATOR PERBANDINGAN")
    print("-"*37)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a <= b
    print("Hasil %d <= %d = %s" % (a,b,c))
    back_to_menu_perbandingan()

def operator_tidaksama():
    clear_screen()
    print("-"*37)
    print("\tOPERATOR PERBANDINGAN")
    print("-"*37)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a != b
    print("Hasil %d != %d = %s" % (a,b,c))
    back_to_menu_perbandingan()

def operator_lebihkecil():
    clear_screen()
    print("-"*37)
    print("\tOPERATOR PERBANDINGAN")
    print("-"*37)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a < b
    print("Hasil %d < %d = %s" % (a,b,c))
    back_to_menu_perbandingan()

def operator_lebihbesar():
    clear_screen()
    print("-"*37)
    print("\tOPERATOR PERBANDINGAN")
    print("-"*37)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a > b
    print("Hasil %d > %d = %s" % (a,b,c))
    back_to_menu_perbandingan()

def operator_samadengan():
    clear_screen()
    print("-"*37)
    print("\tOPERATOR PERBANDINGAN")
    print("-"*37)
    a = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c = a == b
    print("Hasil %d == %d = %s" % (a,b,c))
    back_to_menu_perbandingan()

def operator_kalisama():
    clear_screen()
    print("-"*34)
    print("\tOPERATOR PENUGASAN")
    print("-"*34)
    a = c = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c *= b
    print("Nilai %d *= %d = %d" % (a,b,c))
    back_to_menu_penugasan()

def operator_bagisama():
    clear_screen()
    print("-"*34)
    print("\tOPERATOR PENUGASAN")
    print("-"*34)
    a = c = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c /= b
    print("Nilai %d /= %d = %d" % (a,b,c))
    back_to_menu_penugasan()

def operator_modulussama():
    clear_screen()
    print("-"*34)
    print("\tOPERATOR PENUGASAN")
    print("-"*34)
    a = c = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c %= b
    print("Nilai %d %%= %d = %d" % (a,b,c))
    back_to_menu_penugasan()

def operator_tambahsama():
    clear_screen()
    print("-"*34)
    print("\tOPERATOR PENUGASAN")
    print("-"*34)
    a = c = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c += b
    print("Nilai %d += %d = %d" % (a,b,c))
    back_to_menu_penugasan()

def operator_kurangsama():
    clear_screen()
    print("-"*34)
    print("\tOPERATOR PENUGASAN")
    print("-"*34)
    a = c = int(input("Input Nilai Pertama: "))
    b = int(input("Input Nilai Kedua: "))
    c -= b
    print("Nilai %d -= %d = %d" % (a,b,c))
    back_to_menu_penugasan()
    
def tentang_aplikasi():
    clear_screen()
    print("---------------------------------------------------")
    print("\t\tTENTANG APLIKASI")
    print("---------------------------------------------------")
    print("Nama Aplikasi    : Bebas")
    print("Versi            : 1.0")
    print("Pengembang       : Andi Alfian Bahtiar (2009106002)")
    print("\nHak Cipta © 2020 Bebas")
    print("---------------------------------------------------")
    back_to_menu()

if __name__ == "__main__":
    while True:
        show_menu()
