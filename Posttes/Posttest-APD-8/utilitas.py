import data
from errors import NamaPaketError


def ambil_jarak(asal, tujuan):
    return data.jarak_data[asal][tujuan]


def validasi_nama(nama):
    if nama == "":
        raise NamaPaketError("Nama paket tidak boleh kosong.")
    if len(nama) > 15:
        raise NamaPaketError("Nama paket tidak lebih dari 15 karakter.")
    return nama


def cari_paket_milik(id_paket):
    paket = data.paket_data[id_paket]
    if data.role_aktif != "admin" and paket["pemilik"] != data.username_aktif:
        raise KeyError(id_paket)
    return paket


def ambil_id_terlihat():
    hasil = []
    for id_p in data.paket_data:
        if data.role_aktif == "admin" or data.paket_data[id_p]["pemilik"] == data.username_aktif:
            hasil.append(id_p)
    return hasil


def hitung_total_jarak(daftar_id, index):
    if index >= len(daftar_id):
        return 0
    jarak_ini = data.paket_data[daftar_id[index]]["jarak"]
    return jarak_ini + hitung_total_jarak(daftar_id, index + 1)


def perbarui_jarak_semua():
    for id_p in data.paket_data:
        try:
            data.paket_data[id_p]["jarak"] = ambil_jarak(data.paket_data[id_p]["asal"],
                                                         data.paket_data[id_p]["tujuan"])
        except KeyError:
            data.paket_data[id_p]["jarak"] = 0
            print(f"Peringatan: data jarak paket {id_p} tidak ditemukan.")