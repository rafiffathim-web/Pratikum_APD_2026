# batas = 5
# for i in range(batas):
#     print("Perulangan ke-", i)

# print("="*100)

# game = ["Genshin", 7.0, True]
# for i in game:
#     print(i)

# print("="*100)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
# print('') #biar ada jarak tiap iterasi

# print("="*100)

# jawab = "ya"
# hitung = 0
# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# print("="*100)

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# print("="*100)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# print("="*100)

# angka_benar = 7

# while True:
#     print("=======Game Tebak Angka=======")

#     angka_input = int(input("masukan angka (1 - 10): "))

#     if not angka_input.isdigit(): # "abc12"
#         continue

#     angka_input = int(angka_input) #tujuh

#     if angka_benar == angka_input:
#         print("Angka yang kamu masukan benar")
#         break
#     else:
#         print("Angka salah")
#         break

#print("="*100)

Uang_Awal = int(input("masukan saldo awal:"))



while Uang_Awal > 0:
    pengluaran = int(input("Masukan Pengeluaran anda: "))
    if pengluaran < 1000:
        pengluaran = pengluaran * 1000
    Uang_Awal -= pengluaran
    print(f"Saldo Anda: {Uang_Awal}")