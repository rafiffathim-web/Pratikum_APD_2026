print("🌌 Selamat datang di ANGKASA 🌌")
print("="*100)
print("aplikasi streaming musik 🎧")
print("="*100)

# Validasi Login

biaya_langganan = 1500000

langganan = {
    1: {"nama": "Paket Orbit", "biaya_administrasi": 0.01, "akses": "Akses dasar ke lagu-lagu populer"},
    2: {"nama": "Paket Nebula", "biaya_administrasi": 0.03, "akses": "Akses lagu premium dan playlist kustom"},
    3: {"nama": "Paket Galaxy", "biaya_administrasi": 0.05, "akses": "Akses lagu premium, playlist kustom, dan mode offline"},
    4: {"nama": "Paket Supernova", "biaya_administrasi": 0.07, "akses": "Akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"}
}

print("login untuk melanjutkan ke pembayaran biaya langganan aplikasi streaming musik")
NAMA = input("Masukkan Username: ")
NIM = input("Masukkan Password: ")

if NAMA == "Rafif Fathi Mohammad" and NIM == "41":
    print("Login berhasil! Selamat datang, ", NAMA, "!")

    # Opsi Pembayaran Biaya Langganan
    print("Pilih paket langganan:")
    print(f"1. {langganan[1]['nama']} - Biaya Administrasi: {round(langganan[1]['biaya_administrasi']*100)}% - {langganan[1]['akses']}")
    print(f"2. {langganan[2]['nama']} - Biaya Administrasi: {round(langganan[2]['biaya_administrasi']*100)}% - {langganan[2]['akses']}")
    print(f"3. {langganan[3]['nama']} - Biaya Administrasi: {round(langganan[3]['biaya_administrasi']*100)}% - {langganan[3]['akses']}")
    print(f"4. {langganan[4]['nama']} - Biaya Administrasi: {round(langganan[4]['biaya_administrasi']*100)}% - {langganan[4]['akses']}")

    # Tampilan Hasil
    paket_id = int(input("Masukkan nomor paket langganan yang ingin Anda pilih (1-4): "))
    if paket_id in langganan:
        paket_terpilih = langganan[paket_id]
        # rumus untuk menghitung total biaya langganan berdasarkan paket yang dipilih
        total_bayar = biaya_langganan + (biaya_langganan * paket_terpilih['biaya_administrasi'])
        print("="*100)
        print("Detail Pembayaran Langganan")
        print("="*100)
        print(f"Anda akan mendapatkan {paket_terpilih['akses']}.")
        print(f"Biaya administrasi: Rp {round(paket_terpilih['biaya_administrasi']*biaya_langganan, 0):,.0f} ({round(paket_terpilih['biaya_administrasi']*100)}% dari biaya langganan).")
        print(f"total biaya langganan untuk {paket_terpilih['nama']} adalah: Rp {total_bayar:,.0f}")
        print("="*100)
    else:
        print("Paket langganan tidak valid. Silakan pilih paket yang tersedia.")
else:
    print("Login gagal! Username atau password salah.") 