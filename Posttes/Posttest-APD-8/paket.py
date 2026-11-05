import time
import data
import tampilan
import utilitas
from errors import NamaPaketError, LokasiSamaError


def tambah_paket():
    print("TAMBAH PAKET")
    pemilik = input("Username pelanggan: ").strip()
    try:
        if pemilik not in data.user_data or data.user_data[pemilik]["role"] != "pengguna":
            raise KeyError(pemilik)
        nama = utilitas.validasi_nama(input("Nama paket (maks 15 karakter): ").strip())
        layanan = tampilan.ambil_pilihan("Jenis layanan", data.layanan_data)
        kurir = tampilan.ambil_pilihan("Kurir", data.kurir_data)
        asal = tampilan.ambil_pilihan("Lokasi asal", data.lokasi_data)
        tujuan = tampilan.ambil_pilihan("Lokasi tujuan", data.lokasi_data, asal)
        status = tampilan.ambil_pilihan("Status", data.status_data)
    except KeyError:
        tampilan.gagal("Pelanggan tidak ditemukan.")
    except NamaPaketError as e:
        tampilan.gagal(e)
    else:
        id_baru = str(data.next_paket_id)
        data.paket_data[id_baru] = {"pemilik": pemilik, "nama": nama, "layanan": layanan,
                                    "kurir": kurir, "asal": asal, "tujuan": tujuan,
                                    "jarak": utilitas.ambil_jarak(asal, tujuan),
                                    "status": status}
        data.next_paket_id += 1
        tampilan.sukses(f"Paket {id_baru} berhasil ditambahkan!")
    finally:
        time.sleep(1.5)


def ubah_paket():
    print("UBAH PAKET" if data.role_aktif == "admin" else "AJUKAN PERUBAHAN PAKET")
    id_paket = input("Masukkan ID paket: ").strip().upper()

    try:
        target = utilitas.cari_paket_milik(id_paket)
        if target["status"] in ("Sampai", "Dibatalkan"):
            raise ValueError(f"Paket sudah {target['status']}, tidak bisa diubah.")

        tampilan.tampilkan_menu("Data yang ingin diubah",
                                [(n, f[0]) for n, f in enumerate(data.edit_fields, 1)])
        try:
            nomor = int(input("Pilih nomor: "))
        except ValueError:
            tampilan.gagal("Input harus berupa angka.")
            return
        if nomor < 1:
            raise IndexError
        editf = data.edit_fields[nomor - 1]
        if editf[2] is None:
            baru = utilitas.validasi_nama(input("Nama paket baru (maks 15 karakter): ").strip())
        else:
            baru = tampilan.ambil_pilihan(editf[0] + " baru", editf[2])

        asal_baru = baru if editf[1] == "asal" else target["asal"]
        tujuan_baru = baru if editf[1] == "tujuan" else target["tujuan"]
        if asal_baru == tujuan_baru:
            raise LokasiSamaError("Lokasi asal dan tujuan tidak boleh sama.")
        if baru == target[editf[1]]:
            raise ValueError("Nilai baru sama dengan nilai sekarang.")

        if data.role_aktif == "admin":
            target[editf[1]] = baru
            utilitas.perbarui_jarak_semua()
            tampilan.sukses("Paket berhasil diubah! Jarak diperbarui otomatis.")
        else:
            id_req = f"REQ{data.next_req_id:03d}"
            data.permintaan_data[id_req] = {"pelanggan": data.username_aktif, "paket": id_paket,
                                            "perubahan": editf[0], "nilai_baru": baru,
                                            "status": "Menunggu"}
            data.next_req_id += 1
            tampilan.sukses("Permintaan perubahan dikirim ke admin.")
    except KeyError:
        tampilan.gagal("Paket tidak ditemukan.")
    except (NamaPaketError, LokasiSamaError) as e:
        tampilan.gagal(e)
    except IndexError:
        tampilan.gagal("Pilihan tidak valid.")
    except ValueError as e:
        tampilan.gagal(e)
    finally:
        time.sleep(1.5)


def hapus_paket():
    print("HAPUS PAKET")
    id_paket = input("Masukkan ID paket: ").strip().upper()
    try:
        if id_paket not in data.paket_data:
            raise KeyError(id_paket)
        if data.paket_data[id_paket]["status"] not in ("Sampai", "Dibatalkan"):
            raise ValueError("Paket hanya bisa dihapus jika statusnya Sampai atau Dibatalkan.")

        yakin = input("Yakin ingin menghapus? (Y/N): ")
        if yakin.upper() == "Y":
            del data.paket_data[id_paket]
            id_hapus = [i for i in data.permintaan_data
                        if data.permintaan_data[i]["paket"] == id_paket]
            for id_r in id_hapus:
                del data.permintaan_data[id_r]
            tampilan.sukses("Paket berhasil dihapus!")
        else:
            tampilan.peringatan("Dibatalkan.")
    except KeyError:
        tampilan.gagal("Paket tidak ditemukan.")
    except ValueError as e:
        tampilan.gagal(e)
    finally:
        time.sleep(1.5)