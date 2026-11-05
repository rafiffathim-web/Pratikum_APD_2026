import data
import tampilan
import utilitas
import auth
import paket
import permintaan


def menu_utama():
    tampilan.tampilkan_menu("MENU UTAMA", [(1, "Login"), (2, "Register"), (3, "Keluar")])
    try:
        return int(input("Pilih menu: "))
    except ValueError:
        return None


def dashboard():
    aktif = True
    while aktif:
        tampilan.bersihkan_layar()
        utilitas.perbarui_jarak_semua()
        tampilan.tampilkan_tabel_paket()

        print()
        if data.role_aktif == "admin":
            tampilan.tampilkan_menu("MENU ADMIN", [
                (1, "Tambah paket"), (2, "Ubah paket"), (3, "Hapus paket"),
                (4, "Permintaan perubahan dari pelanggan"), (0, "Logout")])
        else:
            tampilan.tampilkan_menu("MENU PENGGUNA", [
                (1, "Ajukan perubahan paket"), (2, "Riwayat permintaan saya"),
                (0, "Logout")])

        aksi = input("Pilih: ").strip()
        print()

        if data.role_aktif == "admin" and aksi == "1":
            paket.tambah_paket()
        elif (data.role_aktif == "admin" and aksi == "2") or (data.role_aktif == "pengguna" and aksi == "1"):
            paket.ubah_paket()
        elif data.role_aktif == "admin" and aksi == "3":
            paket.hapus_paket()
        elif (data.role_aktif == "admin" and aksi == "4") or (data.role_aktif == "pengguna" and aksi == "2"):
            permintaan.kelola_permintaan()
        elif aksi == "0":
            aktif = False
            data.username_aktif = ""
            data.role_aktif = ""
        else:
            tampilan.tampilkan_pesan("Pilihan tidak ada.", 1)


def main():
    program = True
    tampilan.bersihkan_layar()
    while program:
        pilih = menu_utama()
        if pilih is None:
            tampilan.tampilkan_pesan("Invalid, masukkan angka", 1)
        elif pilih == 1:
            tampilan.bersihkan_layar()
            if auth.proses_login():
                dashboard()
        elif pilih == 2:
            tampilan.bersihkan_layar()
            auth.proses_register()
        elif pilih == 3:
            program = False
            print("Terima kasih!")
        else:
            tampilan.tampilkan_pesan("Invalid, menu tidak ada", 1)
        if program:
            tampilan.bersihkan_layar()


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan oleh pengguna.")
finally:
    print("Sesi program selesai.")