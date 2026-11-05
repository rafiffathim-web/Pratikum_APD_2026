import time
import data
import tampilan
import utilitas
from errors import LokasiSamaError


def kelola_permintaan():
    print("PERMINTAAN PERUBAHAN")
    tampilan.tampilkan_tabel_permintaan()

    if data.role_aktif != "admin":
        input("Tekan Enter untuk kembali...")
        return
    if len(data.permintaan_data) == 0:
        time.sleep(1.5)
        return

    id_req = input("ID permintaan yang diproses (kosongkan untuk kembali): ").strip().upper()
    if id_req == "":
        return

    try:
        req = data.permintaan_data[id_req]
        if req["status"] != "Menunggu":
            raise ValueError("Permintaan ini sudah diproses.")

        proses = input("1. Setujui  2. Tolak : ")
        if proses == "2":
            req["status"] = "Ditolak"
            tampilan.peringatan("Permintaan ditolak.")
        elif proses == "1":
            terapkan_permintaan(req)
        else:
            tampilan.gagal("Pilihan tidak valid.")
    except KeyError:
        tampilan.gagal("Permintaan tidak ditemukan.")
    except ValueError as e:
        tampilan.gagal(e)
    finally:
        time.sleep(1.5)


def terapkan_permintaan(req):
    kunci = ""
    for editf in data.edit_fields:
        if editf[0] == req["perubahan"]:
            kunci = editf[1]

    try:
        target = data.paket_data[req["paket"]]
        if target["status"] in ("Sampai", "Dibatalkan"):
            raise ValueError("Paket sudah tidak bisa diubah. Permintaan ditolak.")

        asal_baru = req["nilai_baru"] if kunci == "asal" else target["asal"]
        tujuan_baru = req["nilai_baru"] if kunci == "tujuan" else target["tujuan"]
        if asal_baru == tujuan_baru:
            raise LokasiSamaError("Lokasi asal dan tujuan sama. Permintaan ditolak.")

        target[kunci] = req["nilai_baru"]
        req["status"] = "Disetujui"
        utilitas.perbarui_jarak_semua()
        tampilan.sukses("Permintaan disetujui! Jarak diperbarui otomatis.")
    except KeyError:
        req["status"] = "Ditolak"
        tampilan.gagal("Paket sudah tidak ada. Permintaan ditolak.")
    except (ValueError, LokasiSamaError) as e:
        req["status"] = "Ditolak"
        tampilan.gagal(e)