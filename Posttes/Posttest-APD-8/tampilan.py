import os
import time
from colorama import Fore, init
from prettytable import PrettyTable
import data
import utilitas
from errors import LokasiSamaError

init(autoreset=True)


def bersihkan_layar():
    os.system(data.clear)


def tampilkan_pesan(pesan, detik):
    print(pesan)
    time.sleep(detik)


def sukses(pesan):
    print(Fore.GREEN + str(pesan))


def gagal(pesan):
    print(Fore.RED + str(pesan))


def peringatan(pesan):
    print(Fore.YELLOW + str(pesan))


def tampilkan_menu(judul, daftar):
    tabel = PrettyTable()
    tabel.field_names = ["No", judul]
    tabel.align = "l"
    for nomor, isi in daftar:
        tabel.add_row([nomor, isi])
    print(tabel)


def tampilkan_tabel_paket():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Pemilik", "Paket", "Layanan", "Kurir",
                         "Asal", "Tujuan", "Jarak", "Status"]
    tabel.align = "l"

    print(f"Login sebagai: {data.username_aktif} ({data.role_aktif})")
    print()
    print("DAFTAR SEMUA PAKET" if data.role_aktif == "admin" else "PAKET SAYA")

    daftar_id = utilitas.ambil_id_terlihat()
    for id_p in daftar_id:
        p = data.paket_data[id_p]
        tabel.add_row([id_p, p["pemilik"], p["nama"], p["layanan"], p["kurir"],
                       p["asal"], p["tujuan"], str(p["jarak"]) + " km", p["status"]])

    if len(daftar_id) == 0:
        peringatan("(belum ada paket)")
    else:
        print(tabel)
        print(f"Total jarak seluruh paket: {utilitas.hitung_total_jarak(daftar_id, 0)} km")


def tampilkan_tabel_permintaan():
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Pelanggan", "Paket", "Perubahan", "Nilai baru", "Status"]
    tabel.align = "l"

    jumlah = 0
    for id_r in data.permintaan_data:
        r = data.permintaan_data[id_r]
        if data.role_aktif == "admin" or r["pelanggan"] == data.username_aktif:
            tabel.add_row([id_r, r["pelanggan"], r["paket"], r["perubahan"],
                           r["nilai_baru"], r["status"]])
            jumlah += 1

    if jumlah == 0:
        peringatan("(belum ada permintaan)")
    else:
        print(tabel)
    print()


def ambil_pilihan(judul, opsi, dilarang=None):
    while True:
        tabel = PrettyTable()
        tabel.field_names = ["No", judul]
        tabel.align = "l"
        for n, opt in enumerate(opsi, 1):
            tabel.add_row([n, opt])
        print(tabel)
        try:
            nomor = int(input("Pilih nomor: "))
            if nomor < 1 or nomor > len(opsi):
                raise IndexError
            pilihan = opsi[nomor - 1]
            if dilarang is not None and pilihan == dilarang:
                raise LokasiSamaError("Lokasi tujuan tidak boleh sama dengan lokasi asal.")
            return pilihan
        except ValueError:
            gagal("Input harus berupa angka.")
        except IndexError:
            gagal("Pilihan tidak valid.")
        except LokasiSamaError as e:
            gagal(e)