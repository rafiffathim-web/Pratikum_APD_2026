# def luas_persegi_panjang():
#     luas = 3 * 5
#     return luas
#     #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang())
#     #Output
#     #Luas persegi panjang: 15

# print("-"*100)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
#     #Kita panggil fungsinya lalu argumen kita adalah angka 7
# print("Luas persegi:", luas_persegi(7))

# print("-"*100)

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     return luas

# def total_harga_tanah(panjang, lebar, harga = 100000):
#     total = luas_persegi_panjang(panjang, lebar) * harga
#     return total
# #Kita panggil fungsinya
# print("Luas persegi panjang:", luas_persegi_panjang(7, 4))
# print("Total harga tanah:", total_harga_tanah(7, 4))

# print("-"*100)

# def sapa_pengguna(nama_pengguna):
#     print(f"Halo, selamat datang {nama_pengguna}")
#     #Pemanggilan Prosedur
# sapa_pengguna("Citra")

# print("-"*100)

# #Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"
# #Membuat variabel lokal
# def data():
#     nama = "Teknik Kedokteran"
#     prodi = "Kedokteran Lanjut"
#     print("Nama:", nama)
#     print("Prodi:", prodi)
#     #Mengakses variabel lokal
#     data()
#     #Mengakses variabel global
# print("Nama:", nama)
# print("Prodi:", prodi)

# print("-"*100)

# def faktorial(n):
# #Base Case: Kondisi fungsi berhenti
#     if n == 0 or n == 1:
#         return 1
#     #Rekursive Case: Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")

# print("-"*100)

# #Variabel global untuk menyimpan data buku
# buku = []
# #Fungsi untuk menampilkan data buku
# def lihat_buku():
#     if len(buku) >= 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#     for indeks in range(len(buku)):
#         print(indeks, "|", buku[indeks])

# print("-"*100)

# #Fungsi untuk menambah data
# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")

# print("-"*100)

# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks >= len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#     buku[indeks] = buku_baru
#     print("Buku berhasil diupdate!")

# print("-"*100)

# def hapus_buku():
#     lihat_buku()
# indeks = int(input("Masukkan ID Film: "))
# if indeks >= len(buku) or indeks < 0:
#     print("ID tidak valid")
# else:
#     buku.remove(buku[indeks])
# print("Buku berhasil dihapus!")



# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
#     menu = input("PILIH MENU > ")
#     print("\n")
#     if menu == "1":
#         lihat_buku()
#     elif menu == "2":
#         tambah_buku()
#     elif menu == "3":
#         edit_buku()
#     elif menu == "4":
#         hapus_buku()
#     elif menu == "5":
#         exit()
#     else:
#         print("Pilihan tidak valid!")

# print("-"*100)

# #Variabel global untuk menyimpan data buku
# buku = []
# #Fungsi untuk menampilkan data buku
# def lihat_buku():
#     if len(buku) >= 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#     for indeks in range(len(buku)):
#         print(indeks, "|", buku[indeks])

# #Fungsi untuk menambah data
# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")
# #Fungsi untuk mengedit data
# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks >= len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks]=buku_baru
#         print("Buku berhasil diupdate!")

# def hapus_buku():
#     lihat_buku()
#     indeks=int(input("Masukkan ID Film:"))
#     if indeks>=len(buku) or indeks<0:
#         print("ID tidak valid")
#     else:buku.remove(buku[indeks])
#     print("Buku berhasil dihapus!")

# def tampilkan_menu():
#     print("\n")
#     print("=========MENU=========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")
#     menu=input("PILIH MENU>")
#     print("\n")
#     if menu=="1":
#         lihat_buku()
#     elif menu=="2":
#         tambah_buku()
#     elif menu=="3":
#         edit_buku()
#     elif menu=="4":
#         hapus_buku()
#     elif menu=="5":
#         exit()
#     else:print("Pilihan tidak valid!")

#     while(True):
#         tampilkan_menu()


print("="*100)