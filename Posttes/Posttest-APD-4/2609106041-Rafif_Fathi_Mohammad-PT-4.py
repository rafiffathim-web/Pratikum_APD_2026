username = "RAFIF"
password = "041"

lanjut = "Y"

while True:
    input_username = input("Enter username: ").strip().upper()
    input_password = input("Enter password: ").strip().upper()

    if input_username == username:
        if input_password == password:
            print("Login berhasil!")
            break
        elif input_password == "":
            print("Password tidak boleh kosong!")
        elif input_password != password:
            print("Password salah!")
    elif input_username == "":
        if input_password == "":
            print("Username dan password tidak boleh kosong!")
        elif input_password != password:
            print("Username tidak boleh kosong! Password salah!")
        else:
            print("Username tidak boleh kosong!")
    elif input_username != username:
        if input_password == "":
            print("Username salah! Password tidak boleh kosong!")
        elif input_password != password:
            print("Username dan password salah!")
        else:
            print("Username salah!")
    else:
        print("Username salah!")

total_kal_gambut = 0
total_kal_mineral = 0
total_sum_gambut = 0
total_sum_mineral = 0

while lanjut == "Y":



    while True:
        pulau = input("Pulau (KALIMANTAN, SUMATERA): ").strip().upper()
        if pulau == "":
            print("Pulau tidak boleh kosong!")
        elif pulau == "KALIMANTAN" or pulau == "SUMATERA":
            break
        else:
            print("Pulau tidak valid!")

    if pulau == "KALIMANTAN":
        while True:
            tipe = input("Tipe (Lahan): ").strip().upper()
            if tipe == "GAMBUT":
                kategori = "KALIMANTAN-Gambut"
                break
            elif tipe == "MINERAL":
                kategori = "KALIMANTAN-Mineral"
                break
            elif tipe == "":
                print("Tipe lahan tidak boleh kosong!")
            else:
                print("Tipe lahan tidak valid!")
    elif pulau == "SUMATERA":
        while True:
            tipe = input("Tipe (Lahan): ").strip().upper()
            if tipe == "GAMBUT":
                kategori = "SUMATERA-Gambut"
                break
            elif tipe == "MINERAL":
                kategori = "SUMATERA-Mineral"
                break
            elif tipe == "":
                print("Tipe lahan tidak boleh kosong!")
            else:
                print("Tipe lahan tidak valid!")
    else:
        print("pulau tidak valid!")



    hektare = 5

    while True:
        teks = input("Berapa titik api: ").strip()
        if teks == "":
            print("Input tidak boleh kosong!")
            continue
        if not teks.isdigit():
            print("Masukkan angka bulat positif!")
            continue
        titik_api = int(teks)
        break

    nilai = titik_api * hektare 
    
    if kategori == "KALIMANTAN-Gambut":
        total_kal_gambut += nilai
    elif kategori == "KALIMANTAN-Mineral":
        total_kal_mineral += nilai
    elif kategori == "SUMATERA-Gambut":
        total_sum_gambut += nilai
    elif kategori == "SUMATERA-Mineral":
        total_sum_mineral += nilai

    while True:
        lanjut = input("Input lagi? (Y/T): ").strip().upper()
        if lanjut == "":
            print("Tidak boleh kosong!")
        elif lanjut == "Y" or lanjut == "T":
            break
        else:
            print("Ketik Y atau T saja!")

print("=" * 100)
print("REKAPITULASI TITIK API KARHUTLA")
print("=" * 100)
print(f"Luas lahan terbakar di KALIMANTAN-Gambut: {total_kal_gambut} Ha")
print(f"Luas lahan terbakar di KALIMANTAN-Mineral: {total_kal_mineral} Ha")
print(f"Luas lahan terbakar di SUMATERA-Gambut: {total_sum_gambut} Ha")
print(f"Luas lahan terbakar di SUMATERA-Mineral: {total_sum_mineral} Ha")
print("=" * 100)
print(f"Total luas lahan terbakar di KALIMANTAN: {total_kal_gambut + total_kal_mineral} Ha")
print(f"Total luas lahan terbakar di SUMATERA: {total_sum_gambut + total_sum_mineral} Ha")
print("=" * 100)
print(f"Total luas lahan terbakar di seluruh Indonesia: {total_kal_gambut + total_kal_mineral + total_sum_gambut + total_sum_mineral} Ha")