# kartu = {"merah", "merah", "biru", "hijau"}
# print(kartu)

# # set menggunakan list
# matkul = ["apd", "orsikom", "apd", "kalkulus"]
# sks = set(matkul)
# print(sks)

# #set menggunakan tuple
# buah = set(("apel", "jeruk", "mangga", "apel"))
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# print("==="*20)

# kelas = {"a", "b", "c"}
# kelas.add("d")
# print(kelas)

# print("==="*20)

# buah = {"apel", "mangga", "jeruk"}
# buah.remove("mangga")
# print(buah)

# print("==="*20)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal", "shasha"}
# # gabung = aslab1.union(aslab2)
# # A1 = gabung
# # update = aslab1.update(aslab2)
# # A1=aslab1
# # intersect = aslab1.intersection(aslab2)
# # A1 = intersect
# differ = aslab1.difference(aslab2)
# A1 = differ
# print(A1)

# print("==="*20)
# print("dictionary")
# print("==="*20)
# Matkul = {
# "Matkul_ganjil" : "kalkulus",
# "Matkul_genap" : "statistik"
# }

# print(Matkul["Matkul_ganjil"])
# print(Matkul)

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }
# print(f"Nama saya adalah {Biodata['Nama']}")
# print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")

# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }
# print(f"Nama saya adalah {Biodata.get('Nama')}")
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Key untuk alamat tidak ada"))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i in game.values():
#     print(i)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# for i, j in game.items():
#     print(f"{i} adalah jenis game {j}")

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# game["resident evil"] = "horror"
# print(game)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# game.update({"resident evil" : "horror"})
# print(game)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# tambah = game.setdefault("resident evil", "horror")
# print(game)
# print("Tipe game", game.setdefault("grow a garden", "gardening"))

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# print(game)
# game["genshin impact"] = "adventure"
# print(game)

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }

# print(game)
# game.update({"genshin impact" : "adventure"})
# print(game)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print(aset)
# aset.clear()
# print(aset)

# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }
# print("Panjang dictionary :", len(aset))
# print(len(aset))

# menu = {
# "ayam geprek" : 15000,
# "ayam goreng" : 13000,
# "ayam bakar" : 17000,
# "nasi goreng" : 12000,
# "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# menu_baru["nasi goreng"] = 15000
# print(menu)
# print(menu_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)
# print(menu)

# menu = {
# "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
# "nasi" : ["nasi goreng", "nasi uduk"],
# "mie" : ["mie goreng rendang", "mie goreng aceh"],
# "kuah" : ["soto", "rawon", "sop iga"]
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
# for kategori in j:
#     print(kategori)
# print("")
