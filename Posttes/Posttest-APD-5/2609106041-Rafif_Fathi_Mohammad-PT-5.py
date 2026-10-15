import os
import time

# ===================== DATA =====================

user_data = [
    ["admin", "admin1", "admin"],
    ["pengguna", "pengguna1", "pengguna"]
]

layanan_data = ["Reguler", "Express", "Same Day"]
kurir_data = ["Budi", "Sinta", "Andi"]
lokasi_data = ["Balikpapan", "Samarinda", "Bontang", "Tenggarong", "Penajam"]
status_data = ["Diproses", "Dikirim", "Sampai", "Dibatalkan"]


jarak_data = [
    ["Balikpapan", "Samarinda", 115],
    ["Balikpapan", "Bontang", 235],
    ["Balikpapan", "Tenggarong", 130],
    ["Balikpapan", "Penajam", 40],
    ["Samarinda", "Bontang", 120],
    ["Samarinda", "Tenggarong", 35],
    ["Samarinda", "Penajam", 150],
    ["Bontang", "Tenggarong", 155],
    ["Bontang", "Penajam", 275],
    ["Tenggarong", "Penajam", 165]
]


paket_data = [
    ["1", "pengguna", "Laptop", "Express", "Budi", "Balikpapan", "Samarinda", 0, "Dikirim"]
]


permintaan_data = []


edit_fields = [
    ["Nama paket", 2, None],
    ["Jenis layanan", 3, layanan_data],
    ["Kurir", 4, kurir_data],
    ["Lokasi asal", 5, lokasi_data],
    ["Lokasi tujuan", 6, lokasi_data],
    ["Status", 8, status_data]
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

        akun = None
        for i in user_data:
            if i[0] == username:
                akun = i
                break

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong.")
            time.sleep(1)
            os.system(clear)

            pilihan = input("Tidak punya akun, apakah ingin membuat akun? (Y/N): ")
            if pilihan.upper() == "Y":
                login = False
                register = True
            os.system(clear)
        
        elif akun is None:
            print("Username salah.")
            time.sleep(1)
            os.system(clear)

            pilihan = input("Tidak punya akun, apakah ingin membuat akun? (Y/N): ")
            if pilihan.upper() == "Y":
                login = False
                register = True
            os.system(clear)

        elif akun[1] != password:
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

            role = akun[2]
            login = False
            table = True

    while register == True: #Register
        print("Register")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        ada = False
        for i in user_data:
            if i[0] == username:
                ada = True
                break

        if username == "" or password == "":
            print("Username dan password tidak boleh kosong.")
        elif ada:
            print("Username sudah dipakai.")
        else:
            user_data.append([username, password, "pengguna"])
            print("Registrasi berhasil!")
            register = False
            menu = True

        time.sleep(1)
        os.system(clear)

    while table == True: #Table
        os.system(clear)

        for paket in paket_data:
            paket[7] = 0
            for jarak in jarak_data:
                if (jarak[0] == paket[5] and jarak[1] == paket[6]) or (jarak[0] == paket[6] and jarak[1] == paket[5]):
                    paket[7] = jarak[2]

        # READ
        print(f"Login sebagai: {username} ({role})")
        print()
        if role == "admin":
            print("DAFTAR SEMUA PAKET")
        else:
            print("PAKET SAYA")

        header = ["ID", "Pemilik", "Paket", "Layanan", "Kurir", "Asal", "Tujuan", "Jarak", "Status"]
        widths = [8, 10, 16, 10, 8, 12, 12, 9, 11]

        line = ""
        for i in range(len(header)):
            line += header[i].ljust(widths[i])
        print(line)
        print("-" * sum(widths))

        tampil = []
        for paket in paket_data:
            if role == "admin" or paket[1] == username:
                tampil.append(paket)

        if len(tampil) == 0:
            print("(belum ada paket)")

        for paket in tampil:
            line = ""
            for i in range(len(paket)):
                if i == 7:
                    nilai = str(paket[i]) + " km"
                else:
                    nilai = str(paket[i])
                line += nilai.ljust(widths[i])
            print(line)

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
            ada = False
            for user in user_data:
                if user[0] == pemilik and user[2] == "pengguna":
                    ada = True
            nama = input("Nama paket (maks 15 karakter): ")

            if not ada:
                print("Pelanggan tidak ditemukan.")
            elif nama == "":
                print("Nama paket tidak boleh kosong.")
            elif len(nama) > 15:
                print("Nama paket tidak lebih dari 15")
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

                id_baru = f"{next_paket_id:1d}"
                paket_data.append([id_baru, pemilik, nama, values[0], values[1], values[2], values[3], 0, values[4]])
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
            for paket in paket_data:
                if paket[0] == id_paket and (role == "admin" or paket[1] == username):
                    target = paket

            if target is None:
                print("Paket tidak ditemukan.")
            elif target[8] == "Sampai":
                print("Paket sudah Sampai, tidak bisa diubah.")
            elif target[8] == "Dibatalkan":
                print("Paket sudah Dibatalkan, tidak bisa diubah")
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
                        asal_baru = target[5]
                        tujuan_baru = target[6]
                        if editf[1] == 5:
                            asal_baru = baru
                        if editf[1] == 6:
                            tujuan_baru = baru

                        if asal_baru == tujuan_baru:
                            print("Lokasi asal dan tujuan tidak boleh sama.")
                        elif baru == target[editf[1]]:
                            print("Nilai baru sama dengan nilai sekarang.")
                        elif role == "admin":
                            target[editf[1]] = baru
                            print("Paket berhasil diubah! Jarak diperbarui otomatis.")
                        else:
                            permintaan_data.append([f"REQ{next_req_id:03d}", username, target[0], editf[0], baru, "Menunggu"])
                            next_req_id += 1
                            print("Permintaan perubahan dikirim ke admin.")
            time.sleep(1.5)

        # Delete
        elif role == "admin" and aksi == "3":
            print("HAPUS PAKET")
            id_paket = input("Masukkan ID paket: ").upper()
            target = None
            for paket in paket_data:
                if paket[0] == id_paket:
                    target = paket

            if target is None:
                print("Paket tidak ditemukan.")
            elif target[8] != "Sampai" and target[8] != "Dibatalkan":
                print("Paket hanya bisa dihapus jika statusnya Sampai atau Dibatalkan.")
            else:
                yakin = input("Yakin ingin menghapus? (Y/N): ")
                if yakin.upper() == "Y":
                    paket_data.remove(target)

                    i = 0
                    while i < len(permintaan_data):
                        if permintaan_data[i][2] == id_paket:
                            permintaan_data.pop(i)
                        else:
                            i += 1

                    print("Paket berhasil dihapus!")
                else:
                    print("Dibatalkan.")
            time.sleep(1.5)

        # PERMINTAAN PERUBAHAN 
        elif (role == "admin" and aksi == "4") or (role == "pengguna" and aksi == "2"):
            print("PERMINTAAN PERUBAHAN")
            req_header = ["ID", "Pelanggan", "Paket", "Perubahan", "Nilai baru", "Status"]
            req_widths = [8, 12, 9, 16, 14, 10]

            line = ""
            for i in range(len(req_header)):
                line += req_header[i].ljust(req_widths[i])
            print(line)
            print("-" * sum(req_widths))

            daftar = []
            for r in permintaan_data:
                if role == "admin" or r[1] == username:
                    daftar.append(r)

            if len(daftar) == 0:
                print("(belum ada permintaan)")

            for r in daftar:
                line = ""
                for i in range(len(r)):
                    line += r[i].ljust(req_widths[i])
                print(line)
            print()

            if role == "admin" and len(daftar) > 0:
                id_req = input("ID permintaan yang diproses (kosongkan untuk kembali): ").upper()

                if id_req != "":
                    req = None
                    for r in permintaan_data:
                        if r[0] == id_req:
                            req = r

                    if req is None:
                        print("Permintaan tidak ditemukan.")
                    elif req[5] != "Menunggu":
                        print("Permintaan ini sudah diproses.")
                    else:
                        proses = input("1. Setujui  2. Tolak : ")

                        if proses == "1":
                            target = None
                            for paket in paket_data:
                                if paket[0] == req[2]:
                                    target = paket

                            idx = 0
                            for editf in edit_fields:
                                if editf[0] == req[3]:
                                    idx = editf[1]

                            if target is None or target[8] == "Sampai" or target[8] == "Dibatalkan":
                                req[5] = "Ditolak"
                                print("Paket sudah tidak bisa diubah. Permintaan ditolak.")
                            else:
                                asal_baru = target[5]
                                tujuan_baru = target[6]
                                if idx == 5:
                                    asal_baru = req[4]
                                if idx == 6:
                                    tujuan_baru = req[4]

                                if asal_baru == tujuan_baru:
                                    req[5] = "Ditolak"
                                    print("Lokasi asal dan tujuan sama. Permintaan ditolak.")
                                else:
                                    target[idx] = req[4]
                                    req[5] = "Disetujui"
                                    print("Permintaan disetujui! Jarak diperbarui otomatis.")
                        elif proses == "2":
                            req[5] = "Ditolak"
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

