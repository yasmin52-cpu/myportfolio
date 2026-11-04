from rest_framework.permissions import BasePermission, SAFE_METHODS  # Memakai dasar permission DRF dan daftar method baca.


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):  # Menjaga aturan Project dan Experience yang sudah berlaku.
    message = "Anda tidak memiliki izin untuk mengubah data ini."  # Memberi pesan yang jelas ketika akses ditolak.

    def has_permission(self, request, view):  # Memeriksa hak sebelum isi API view dijalankan.
        if request.method in SAFE_METHODS:  # Mengizinkan GET, HEAD, dan OPTIONS untuk semua pengunjung.
            return True  # Bacaan publik tetap tersedia.
        if not request.user.is_authenticated:  # Memisahkan pengunjung anonim dari akun yang login.
            return False  # Pengunjung anonim tidak boleh menulis.
        if request.user.is_superuser:  # Memeriksa pemilik portofolio sesuai pola view lama.
            return True  # Pemilik boleh membuat, mengubah, dan menghapus.
        return request.method in ("PUT", "PATCH") and request.user.groups.filter(name="Editor").exists()  # Editor hanya boleh memperbarui.