import os

# ===================== VARIABEL GLOBAL =====================

user_data = {
    "admin":    {"password": "admin1",    "role": "admin"},
    "pengguna": {"password": "pengguna1", "role": "pengguna"}
}

layanan_data = ["Reguler", "Express", "Same Day"]
kurir_data = ["Budi", "Sinta", "Andi"]
lokasi_data = ["Balikpapan", "Samarinda", "Bontang", "Tenggarong", "Penajam"]
status_data = ["Diproses", "Dikirim", "Sampai", "Dibatalkan"]

jarak_data = {
    "Balikpapan": {"Samarinda": 115, "Bontang": 235, "Tenggarong": 130, "Penajam": 40},
    "Samarinda":  {"Balikpapan": 115, "Bontang": 120, "Tenggarong": 35, "Penajam": 150},
    "Bontang":    {"Balikpapan": 235, "Samarinda": 120, "Tenggarong": 155, "Penajam": 275},
    "Tenggarong": {"Balikpapan": 130, "Samarinda": 35, "Bontang": 155, "Penajam": 165},
    "Penajam":    {"Balikpapan": 40, "Samarinda": 150, "Bontang": 275, "Tenggarong": 165}
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

next_paket_id = 2
next_req_id = 1
username_aktif = ""
role_aktif = ""
clear = "cls" if os.name == "nt" else "clear"