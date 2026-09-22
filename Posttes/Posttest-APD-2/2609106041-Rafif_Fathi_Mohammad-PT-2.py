# Daftar harga makanan

makanan_1 = 15000
makanan_2 = 16000
makanan_3 = 19000
makanan_4 = 20000
makanan_5 = 21000
makanan_6 = 22000
biaya_aplikasi = 5000

harga_makanan = [makanan_1, makanan_2, makanan_3, makanan_4, makanan_5, makanan_6]

total_bayar = makanan_1 + makanan_2 + makanan_3 + makanan_4 + makanan_5 + makanan_6 + biaya_aplikasi

rata_rata = total_bayar / len(harga_makanan)
rata_rata = round(rata_rata, 2)

nim = 41

bolean = nim != rata_rata

kurs_eur = 20000
total_euro = total_bayar / kurs_eur
total_euro = round(total_euro, 2)

# Print semua variabel
print("Total bayar :", total_bayar)
print("Rata-rata   :", rata_rata)
print("NIM         :", nim)
print("Boolean     :", bolean)
print("Total Euro  :", total_euro)
print("List harga  :", harga_makanan)

print("Makanan 1-6 :", harga_makanan[-6:])