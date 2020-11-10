m = int(input("Masukan Massa Benda (kg): "))
g = int(input("Masukan Percepatan Gravitasi Bumi (9.8 atau 10): "))
h = int(input("Masukan Tinggi Benda (m): "))

print("\nRumus Energi Potensial: m x g x h\n")
ep = m * g * h
print("M: %d" % (m))
print("G: %d" % (g))
print("H: %d" % (h))
print("Energi Potensial tersebut adalah: %d" % (ep))