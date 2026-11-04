from django.utils.html import strip_tags  # Memakai pembersihan teks yang juga digunakan form lama.
from rest_framework import serializers  # Mengimpor kelas serializer dan error validasi DRF.
from main.models import Experience, Project  # Memakai model Project yang sudah ada, tanpa membuat tabel baru.


class ProjectSerializer(serializers.ModelSerializer):  # Menentukan bentuk baca dan tulis Project pada API.
    star_count = serializers.SerializerMethodField()  # Menghasilkan jumlah star sebagai field hanya baca.
    is_starred = serializers.SerializerMethodField()  # Menghasilkan status star untuk pengguna saat ini.
    starred_by_names = serializers.SerializerMethodField()  # Mempertahankan nama pemberi star yang sudah tampil di UI.

    class Meta:  # Menyimpan pemetaan serializer ke model dan field publik.
        model = Project  # Menghubungkan serializer dengan model Project yang ada.
        fields = ["id", "title", "description", "image_url", "play_url", "star_count", "is_starred", "starred_by_names"]  # Menyatakan kontrak JSON sesuai field project Anda.
        read_only_fields = ["id"]  # Mencegah klien menentukan UUID proyek saat membuat data.

    def validate_title(self, value):  # Menerapkan aturan judul yang setara dengan ProjectForm.
        value = strip_tags(value).strip()  # Membuang tag HTML dan spasi di tepi judul.
        if not value:  # Menolak judul yang kosong setelah dibersihkan.
            raise serializers.ValidationError("Judul proyek tidak boleh kosong.")  # Menghasilkan error field dengan status 400.
        return value  # Mengirim judul bersih ke proses penyimpanan.

    def validate_description(self, value):  # Menerapkan pembersihan deskripsi dari form lama.
        return strip_tags(value).strip()  # Menyimpan deskripsi tanpa tag HTML dan spasi tepi.

    def get_star_count(self, obj):  # Menghitung star untuk representasi GET.
        return obj.starred_by.count()  # Mengambil jumlah pengguna pada relasi star.

    def get_is_starred(self, obj):  # Menentukan keadaan tombol star bagi peminta API.
        request = self.context.get("request")  # Mengambil request yang diberikan oleh API view.
        if request is None or not request.user.is_authenticated:  # Menangani serializer tanpa request atau pengunjung anonim.
            return False  # Pengunjung anonim tidak memiliki star pribadi.
        return obj.starred_by.filter(pk=request.user.pk).exists()  # Memeriksa apakah pengguna saat ini sudah memberi star.

    def get_starred_by_names(self, obj):  # Membuat teks tooltip yang dipakai kartu proyek lama.
        return ", ".join(user.username for user in obj.starred_by.all())  # Menggabungkan nama pengguna dari relasi star.
    
class ExperienceSerializer(serializers.ModelSerializer):  # Menentukan kontrak API untuk pengalaman.
    category_display = serializers.CharField(source="get_category_display", read_only=True)  # Menyediakan label kategori untuk kartu.
    stars_count = serializers.SerializerMethodField()  # Menyediakan jumlah star untuk frontend Experience.
    has_starred = serializers.SerializerMethodField()  # Menyediakan keadaan star pengguna saat ini.

    class Meta:  # Menyimpan konfigurasi model dan field API.
        model = Experience  # Memakai model Experience yang sudah ada.
        fields = ["id", "title", "organization", "description", "category", "category_display", "is_ongoing", "image_url", "stars_count", "has_starred"]  # Memakai field aktual dan nilai turunan.
        read_only_fields = ["id"]  # Mencegah klien mengatur ID pengalaman.

    def validate_title(self, value):  # Menyamakan aturan judul dengan ExperienceForm.
        value = strip_tags(value).strip()  # Membersihkan tag dan spasi tepi.
        if not value:  # Menolak judul kosong setelah pembersihan.
            raise serializers.ValidationError("Role tidak boleh kosong.")  # Mengirim error pada field title.
        return value  # Mengembalikan judul yang bersih.

    def validate_organization(self, value):  # Menyamakan aturan organisasi dengan form lama.
        value = strip_tags(value).strip()  # Membersihkan tag dan spasi tepi.
        if not value:  # Menolak organisasi kosong.
            raise serializers.ValidationError("Organisasi tidak boleh kosong.")  # Mengirim error pada field organization.
        return value  # Mengembalikan organisasi yang bersih.

    def validate_description(self, value):  # Menyamakan aturan deskripsi dengan form lama.
        value = strip_tags(value).strip()  # Membersihkan tag dan spasi tepi.
        if not value:  # Menolak deskripsi kosong.
            raise serializers.ValidationError("Deskripsi tidak boleh kosong.")  # Mengirim error pada field description.
        return value  # Mengembalikan deskripsi yang bersih.

    def validate_image_url(self, value):  # Menyamakan pembersihan URL gambar dengan form lama.
        return strip_tags(value).strip()  # Mengembalikan path atau URL gambar yang sudah dibersihkan.

    def get_stars_count(self, obj):  # Menghitung star untuk respons API.
        return obj.starred_by.count()  # Mengambil jumlah relasi star.

    def get_has_starred(self, obj):  # Memeriksa apakah peminta API sudah memberi star.
        request = self.context.get("request")  # Mengambil pengguna dari context serializer.
        if request is None or not request.user.is_authenticated:  # Menangani guest atau pemanggilan tanpa request.
            return False  # Guest tidak memiliki star pribadi.
        return obj.starred_by.filter(pk=request.user.pk).exists()  # Memeriksa star milik akun saat ini.