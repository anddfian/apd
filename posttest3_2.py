import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        #NIM: 2009106002 + 10 = 12
        angka = int(input("Masukkan angka: "))
        z = 1
        a = 1
        while z < angka:
            print (a)
            a += 1
            if a == 10:
                a -= 9
                z -= 1
            z += 1
        break
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        time.sleep(1.5)
