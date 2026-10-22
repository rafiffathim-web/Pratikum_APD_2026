import os
import time

# ===================== DATA =====================

user_data = {
    "admin":        {"password": "admin1", "role": "admin"},
    "pengguna":     {"password": "pengguna1", "role": "pengguna"}
}

layanan_data = ["Reguler", "Express", "Same Day"]
kurir_data = ["Budi", "Sinta", "Andi"]
lokasi_data = ["Balikpapan", "Samarinda", "Bontang", "Tenggarong", "Penajam"]
status_data = ["Diproses", "Dikirim", "Sampai", "Dibatalkan"]


jarak_data = {
    "Balikpapan": {"Samarinda": 115, "Bontang": 235, "Tenggarong": 130, "Penajam": 40},
    "Samarinda": {"Balikpapan": 115, "Bontang": 120, "Tenggarong": 35, "Penajam": 150},
    "Bontang": {"Balikpapan": 235, "Samarinda": 120, "Tenggarong": 155, "Penajam": 275},
    "Tenggarong": {"Balikpapan": 130, "Samarinda": 35, "Bontang": 155, "Penajam": 165},
    "Penajam": {"Balikpapan": 40, "Samarinda": 150, "Bontang": 275, "Tenggarong": 165}
}


paket_data = {
    "1": {"pemilik": "pengguna", "nama": "Laptop", "layanan": "Express",
          "kurir": "Budi", "asal": "Balikpapan", "tujuan": "Samarinda",
          "jarak": 0, "status": "Dikirim"}
}

permintaan_data = {}


edit_fields = [
    ["Nama paket", "nama", None],
    ["Jenis layanan", "layanan", layanan_data],
    ["Kurir", "kurir", kurir_data],
    ["Lokasi asal", "asal", lokasi_data],
    ["Lokasi tujuan", "tujuan", lokasi_data],
    ["Status", "status", status_data]
]

choice_fields = [
    ["Jenis layanan", layanan_data],
    ["Kurir", kurir_data],
    ["Lokasi asal", lokasi_data],
    ["Lokasi tujuan", lokasi_data],
    ["Status", status_data]
]

next_paket_id = 2
next_req_id = 1

login = False
register = False
table = False
menu = True
program = True
role = ""
username = ""
clear = "cls" if os.name == "nt" else "clear"

os.system(clear)

# ===================== Program =====================
while program == True:

    while menu == True: #Login
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilih_menu = input("Pilih menu: ")

        if pilih_menu == "1":
            login = True
            menu = False
        elif pilih_menu == "2":
            register = True
            menu = False
        elif pilih_menu == "3":
            program = False
            menu = False
            print("Terima kasih!")
        elif pilih_menu.isdigit():
            print("Invalid, menu tidak ada")
        else:
            print("Invalid, masukkan angka")

        time.sleep(1)
        os.system(clear)

    while login == True:
        print("Login")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong.")
            time.sleep(1)
            os.system(clear)

            pilihan = input("Tidak punya akun, apakah ingin membuat akun? (Y/N): ")
            if pilihan.upper() == "Y":
                login = False
                register = True
            os.system(clear)
        
        elif username not in user_data:
            print("Username salah.")
            time.sleep(1)
            os.system(clear)

            pilihan = input("Tidak punya akun, apakah ingin membuat akun? (Y/N): ")
            if pilihan.upper() == "Y":
                login = False
                register = True
            os.system(clear)

        elif user_data[username]["password"] != password:
            print("Password salah.")
            time.sleep(1)
            os.system(clear)

            pilihan = input("Tidak punya akun, apakah ingin membuat akun? (Y/N): ")
            if pilihan.upper() == "Y":
                login = False
                register = True
            os.system(clear)

        else:
            print("Login berhasil!")
            time.sleep(1)
            os.system(clear)

            print("Selamat datang di sistem kami!")
            print(username)
            time.sleep(1)
            os.system(clear)

            role = user_data[username]["role"]
            login = False
            table = True

    while register == True: #Register
        print("Register")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong.")
        elif username in user_data:
            print("Username sudah dipakai.")
        else:
            user_data[username] = {"password": password, "role": "pengguna"}
            print("Registrasi berhasil!")
            register = False
            menu = True

        time.sleep(1)
        os.system(clear)

    while table == True: #Table
        os.system(clear)

        for id_p in paket_data:
            asal = paket_data[id_p]["asal"]
            tujuan = paket_data[id_p]["tujuan"]
            paket_data[id_p]["jarak"] = jarak_data[asal][tujuan]

        # READ
        print(f"Login sebagai: {username} ({role})")
        print()
        if role == "admin":
            print("DAFTAR SEMUA PAKET")
        else:
            print("PAKET SAYA")

        header = ["ID", "Pemilik", "Paket", "Layanan", "Kurir", "Asal", "Tujuan", "Jarak", "Status"]
        kolom = ["pemilik", "nama", "layanan", "kurir", "asal", "tujuan", "jarak", "status"]
        widths = [8, 10, 16, 10, 8, 12, 12, 9, 11]

        line = ""
        for i in range(len(header)):
            line += header[i].ljust(widths[i])
        print(line)
        print("-" * sum(widths))

        jumlah = 0

        for id_p in paket_data:
            paket = paket_data[id_p]
            if role == "admin" or paket["pemilik"] == username:
                line = id_p.ljust(widths[0])
                for i in range(len(kolom)):
                    if kolom[i] == "jarak":
                        nilai = str(paket["jarak"]) + " km"
                    else:
                        nilai = str(paket[kolom[i]])
                    line += nilai.ljust(widths[i + 1])
                print(line)
                jumlah += 1

        if jumlah == 0:
            print("(belum ada paket)")

        print()
        if role == "admin":
            print("1. Tambah paket")
            print("2. Ubah paket")
            print("3. Hapus paket")
            print("4. Permintaan perubahan dari pelanggan")
        else:
            print("1. Ajukan perubahan paket")
            print("2. Riwayat permintaan saya")
        print("0. Logout")

        aksi = input("Pilih: ")
        print()

        # Create
        if role == "admin" and aksi == "1":
            print("TAMBAH PAKET")
            pemilik = input("Username pelanggan: ")
            nama = input("Nama paket (maks 15 karakter): ")

            if pemilik not in user_data or user_data[pemilik]["role"] != "pengguna":
                print("Pelanggan tidak ditemukan.")
            elif nama == "":
                print("Nama paket tidak boleh kosong.")
            elif len(nama) > 15:
                print("Nama paket tidak lebih dari 15 karakter.")
            else:
                values = []
                for choicef in choice_fields:
                    while True:
                        print(choicef[0] + ":")
                        n = 1
                        for opt in choicef[1]:
                            print(f"  {n}. {opt}")
                            n += 1
                        pilihn = input("Pilih nomor: ")

                        if not pilihn.isdigit() or int(pilihn) < 1 or int(pilihn) > len(choicef[1]):
                            print("Pilihan tidak valid.")
                        elif choicef[0] == "Lokasi tujuan" and choicef[1][int(pilihn) - 1] == values[2]:
                            print("Lokasi tujuan tidak boleh sama dengan lokasi asal.")
                        else:
                            values.append(choicef[1][int(pilihn) - 1])
                            break

                id_baru = str(next_paket_id)
                paket_data[id_baru] = {
                    "pemilik": pemilik,
                    "nama": nama,
                    "layanan": values[0],
                    "kurir": values[1],
                    "asal": values[2],
                    "tujuan": values[3],
                    "jarak": 0,
                    "status": values[4]
                }
                next_paket_id += 1
                print(f"Paket {id_baru} berhasil ditambahkan!")
            time.sleep(1.5)

        # UPDATE
        elif (role == "admin" and aksi == "2") or (role == "pengguna" and aksi == "1"):
            if role == "admin":
                print("UBAH PAKET")
            else:
                print("AJUKAN PERUBAHAN PAKET")

            id_paket = input("Masukkan ID paket: ").upper()
            target = None
            if id_paket in paket_data:
                if role == "admin" or paket_data[id_paket]["pemilik"] == username:
                    target = paket_data[id_paket]

            if target is None:
                print("Paket tidak ditemukan.")
            elif target["status"] == "Sampai":
                print("Paket sudah Sampai, tidak bisa diubah.")
            elif target["status"] == "Dibatalkan":
                print("Paket sudah Dibatalkan, tidak bisa diubah.")
            else:
                print("Data yang ingin diubah:")
                n = 1
                for editf in edit_fields:
                    print(f"  {n}. {editf[0]}")
                    n += 1
                pilihn = input("Pilih nomor: ")

                if not pilihn.isdigit() or int(pilihn) < 1 or int(pilihn) > len(edit_fields):
                    print("Pilihan tidak valid.")
                else:
                    editf = edit_fields[int(pilihn) - 1]
                    baru = ""

                    if editf[2] is None:
                        baru = input("Nama paket baru (maks 15 karakter): ")

                        if baru == "":
                            print("Nama paket tidak boleh kosong.")
                            baru = ""
                        elif len(baru) > 15:
                            print("maksimal 15 karakter")
                            baru = ""

                    else:
                        n = 1
                        for opt in editf[2]:
                            print(f"  {n}. {opt}")
                            n += 1
                        no = input(f"{editf[0]} baru, pilih nomor: ")
                        
                        if no.isdigit() and 1 <= int(no) <= len(editf[2]):
                            baru = editf[2][int(no) - 1]
                        else:
                            print("Pilihan tidak valid.")

                    if baru != "":
                        asal_baru = target["asal"]
                        tujuan_baru = target["tujuan"]
                        if editf[1] == "asal":
                            asal_baru = baru
                        if editf[1] == "tujuan":
                            tujuan_baru = baru

                        if asal_baru == tujuan_baru:
                            print("Lokasi asal dan tujuan tidak boleh sama.")
                        elif baru == target[editf[1]]:
                            print("Nilai baru sama dengan nilai sekarang.")
                        elif role == "admin":
                            target[editf[1]] = baru
                            print("Paket berhasil diubah! Jarak diperbarui otomatis.")
                        else:
                            id_req = f"REQ{next_req_id:03d}"
                            permintaan_data[id_req] = {
                                "pelanggan": username,
                                "paket": id_paket,
                                "perubahan": editf[0],
                                "nilai_baru": baru,
                                "status": "Menunggu"
                            }
                            next_req_id += 1
                            print("Permintaan perubahan dikirim ke admin.")
            time.sleep(1.5)

        # Delete
        elif role == "admin" and aksi == "3":
            print("HAPUS PAKET")
            id_paket = input("Masukkan ID paket: ").upper()

            if id_paket not in paket_data:
                print("Paket tidak ditemukan.")
            elif paket_data[id_paket]["status"] != "Sampai" and paket_data[id_paket]["status"] != "Dibatalkan":
                print("Paket hanya bisa dihapus jika statusnya Sampai atau Dibatalkan.")
            else:
                yakin = input("Yakin ingin menghapus? (Y/N): ")
                if yakin.upper() == "Y":
                    del paket_data[id_paket]

                    hapus = []
                    for id_r in permintaan_data:
                        if permintaan_data[id_r]["paket"] == id_paket:
                            hapus.append(id_r)
                    for id_r in hapus:
                        del permintaan_data[id_r]

                    print("Paket berhasil dihapus!")
                else:
                    print("Dibatalkan.")
            time.sleep(1.5)

        # PERMINTAAN PERUBAHAN 
        elif (role == "admin" and aksi == "4") or (role == "pengguna" and aksi == "2"):
            print("PERMINTAAN PERUBAHAN")
            req_header = ["ID", "Pelanggan", "Paket", "Perubahan", "Nilai baru", "Status"]
            req_kolom = ["pelanggan", "paket", "perubahan", "nilai_baru", "status"]
            req_widths = [8, 12, 9, 16, 14, 10]

            line = ""
            for i in range(len(req_header)):
                line += req_header[i].ljust(req_widths[i])
            print(line)
            print("-" * sum(req_widths))

            jumlah_req = 0
            for id_r in permintaan_data:
                r = permintaan_data[id_r]
                if role == "admin" or r["pelanggan"] == username:
                    line = id_r.ljust(req_widths[0])
                    for i in range(len(req_kolom)):
                        line += str(r[req_kolom[i]]).ljust(req_widths[i + 1])
                    print(line)
                    jumlah_req += 1

            if jumlah_req == 0:
                print("(belum ada permintaan)")
            print()

            if role == "admin" and jumlah_req > 0:
                id_req = input("ID permintaan yang diproses (kosongkan untuk kembali): ").upper()

                if id_req != "":
                    if id_req not in permintaan_data:
                        print("Permintaan tidak ditemukan.")
                    elif permintaan_data[id_req]["status"] != "Menunggu":
                        print("Permintaan ini sudah diproses.")
                    else:
                        req = permintaan_data[id_req]
                        proses = input("1. Setujui  2. Tolak : ")

                        if proses == "1":
                            target = None
                            if req["paket"] in paket_data:
                                target = paket_data[req["paket"]]

                            kunci = ""
                            for editf in edit_fields:
                                if editf[0] == req["perubahan"]:
                                    kunci = editf[1]

                            if target is None or target["status"] == "Sampai" or target["status"] == "Dibatalkan":
                                req["status"] = "Ditolak"
                                print("Paket sudah tidak bisa diubah. Permintaan ditolak.")
                            else:
                                asal_baru = target["asal"]
                                tujuan_baru = target["tujuan"]
                                if kunci == "asal":
                                    asal_baru = req["nilai_baru"]
                                if kunci == "tujuan":
                                    tujuan_baru = req["nilai_baru"]

                                if asal_baru == tujuan_baru:
                                    req["status"] = "Ditolak"
                                    print("Lokasi asal dan tujuan sama. Permintaan ditolak.")
                                else:
                                    target[kunci] = req["nilai_baru"]
                                    req["status"] = "Disetujui"
                                    print("Permintaan disetujui! Jarak diperbarui otomatis.")
                        elif proses == "2":
                            req["status"] = "Ditolak"
                            print("Permintaan ditolak.")
                        else:
                            print("Pilihan tidak valid.")
                    time.sleep(1.5)
            else:
                input("Tekan Enter untuk kembali...")

        # LOGOUT
        elif aksi == "0":
            table = False
            menu = True
            role = ""
            os.system(clear)

        else:
            print("Pilihan tidak ada.")
            time.sleep(1)    

