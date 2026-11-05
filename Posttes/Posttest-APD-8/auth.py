import time
import data
import tampilan
from errors import AkunError


def proses_register():
    print("Register")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    try:
        if username == "" or password == "":
            raise AkunError("Username dan password tidak boleh kosong.")
        if username in data.user_data:
            raise AkunError("Username sudah dipakai.")
        data.user_data[username] = {"password": password, "role": "pengguna"}
        tampilan.sukses("Registrasi berhasil!")
    except AkunError as e:
        tampilan.gagal(e)
    finally:
        time.sleep(1)
        tampilan.bersihkan_layar()


def proses_login():
    print("Login")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    try:
        if username == "" or password == "":
            raise AkunError("Username dan password tidak boleh kosong.")
        if username not in data.user_data:
            raise AkunError("Username salah.")
        if data.user_data[username]["password"] != password:
            raise AkunError("Password salah.")
        data.username_aktif = username
        data.role_aktif = data.user_data[username]["role"]
        tampilan.sukses("Login berhasil!")
        time.sleep(1)
        return True
    except AkunError as e:
        tampilan.gagal(e)
        time.sleep(1)
        tampilan.bersihkan_layar()
        if input("Tidak punya akun, apakah ingin membuat akun? (Y/N): ").upper() == "Y":
            tampilan.bersihkan_layar()
            proses_register()
        return False