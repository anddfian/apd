usd = int(input("Masukan Jumlah Dollar: "))
#Update: 8 Nov 03.47
kurs_usd_to_idr = 14215 

konversi = usd * kurs_usd_to_idr
print("\nJumlah Dollar: %s" % (usd))
print("Kurs Dollar ke Rupiah: %d" % (kurs_usd_to_idr))
print("Konversi tersebut adalah: %d x %d = %d" % (usd,kurs_usd_to_idr,konversi))