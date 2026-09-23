angka = 6
if angka < 10: # Kondisi percabangan IF
    print("Angka kurang dari 10")

print("////////////////////////////////////")

umur = int(input("Masukkan umur: ")) # Input umur
# Misalkan, umur = 17
if umur >= 17:
    print("Kamu sudah bisa membuat KTP") # Blok if dijalankan karena
    # kondisi True
else:
    print("Kamu belum bisa membuat KTP") # Blok else tidak dijalankan

print("////////////////////////////////////")

# Input jenis kendaraan dari user
kendaraan = input("Masukkan jenis kendaraan anda: ")
# Misalnya, kendaraan = "mobil"
# Percabangan

if kendaraan == "mobil":
    tarif_parkir = 10000
elif kendaraan == "motor":
    tarif_parkir = 5000
else:
    tarif_parkir = 15000
# Menampilkan tarif parkir yang harus dibayar
print("Tarif parkir yang harus dibayar:", tarif_parkir)

print("////////////////////////////////////")

# Bentuk Awal Percabangan IF/ELSE
umur = 20
if umur >= 18:
    status = "Dewasa"
else:
    status = "Belum Dewasa"

# Bentuk singkat percabangan IF/ELSE

# Bentuk Ternary Operator
umur = 20
status = "Dewasa" if umur >= 18 else "Belum Dewasa"

print("Status:", status)

print("////////////////////////////////////")

