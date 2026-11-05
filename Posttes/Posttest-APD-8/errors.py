# ===================== ERROR (EXCEPTION) KUSTOM =====================

class NamaPaketError(Exception):
    """Dilempar jika nama paket kosong atau lebih dari 15 karakter."""
    pass


class LokasiSamaError(Exception):
    """Dilempar jika lokasi asal sama dengan lokasi tujuan."""
    pass


class AkunError(Exception):
    """Dilempar jika data login / register tidak valid."""
    pass