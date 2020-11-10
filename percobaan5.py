idr = int(input("Masukan Jumlah Rupiah: "))
#Update: 8 Nov 03.47
kurs_usd_to_idr = 14215 

konversi = idr / kurs_usd_to_idr
print("\nJumlah Rupiah: %s" % (idr))
print("Kurs Rupiah ke Dollar: %d" % (kurs_usd_to_idr))
print("Konversi tersebut adalah: %d x %d = %f" % (idr,kurs_usd_to_idr,konversi))