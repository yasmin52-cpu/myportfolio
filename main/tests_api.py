import uuid  # Membuat UUID acak untuk uji objek yang tidak ada.
from django.contrib.auth.models import Group, User  # Membuat akun dan grup Editor di database test.
from django.urls import reverse  # Mencari URL berdasarkan nama route.
from rest_framework.test import APIClient, APITestCase  # Memakai klien dan kelas test DRF.
from main.models import Project  # Memeriksa perubahan model Project di database test.


class ProjectAPITest(APITestCase):  # Mengelompokkan test kontrak API Project.
    def setUp(self):  # Menyiapkan data baru sebelum setiap test.
        self.owner = User.objects.create_superuser("owner", "owner@example.com", "test-password")  # Membuat pemilik untuk operasi tulis.
        self.visitor = User.objects.create_user("visitor", password="test-password")  # Membuat akun biasa untuk uji izin.
        self.editor = User.objects.create_user("editor", password="test-password")  # Membuat akun Editor untuk uji update.
        self.editor.groups.add(Group.objects.create(name="Editor"))  # Memasukkan akun Editor ke grup yang dipakai project.
        self.project = Project.objects.create(title="Portfolio", description="My website", image_url="/static/img/example.png", play_url="https://example.com/")  # Membuat proyek awal dengan field wajib aktual.
        self.list_url = reverse("api:project-list")  # Menyimpan URL daftar API.
        self.detail_url = reverse("api:project-detail", args=[self.project.id])  # Menyimpan URL detail proyek awal.
        self.star_url = reverse("api:project-star", args=[self.project.id])  # Menyimpan URL star proyek awal.
        self.payload = {"title": "New project", "description": "A useful app", "image_url": "/static/img/new.png", "play_url": "https://example.com/new/"}  # Menyimpan input valid untuk operasi create dan PUT.

    def test_public_list_and_detail(self):  # Memastikan baca publik dan bentuk data datar.
        response = self.client.get(self.list_url)  # Meminta daftar tanpa login.
        self.assertEqual(response.status_code, 200)  # Daftar publik harus berhasil.
        self.assertEqual(response.data[0]["id"], str(self.project.id))  # UUID harus muncul sebagai string.
        self.assertNotIn("fields", response.data[0])  # Format lama tidak boleh muncul pada API baru.
        self.assertEqual(self.client.get(self.detail_url).status_code, 200)  # Detail juga harus publik.

    def test_search_and_empty_results(self):  # Memeriksa filter judul dan daftar kosong.
        self.assertEqual(len(self.client.get(self.list_url, {"title": "PORT"}).data), 1)  # Pencarian tidak peka huruf besar.
        self.assertEqual(self.client.get(self.list_url, {"title": "tidak-ada"}).data, [])  # Hasil kosong berupa daftar, bukan 404.

    def test_missing_project(self):  # Memastikan detail UUID asing menghasilkan 404.
        url = reverse("api:project-detail", args=[uuid.uuid4()])  # Membentuk URL untuk UUID yang belum tersimpan.
        self.assertEqual(self.client.get(url).status_code, 404)  # Objek yang tidak ada harus ditolak sebagai 404.

    def test_guest_and_visitor_cannot_manage(self):  # Memeriksa create, update, delete tanpa hak.
        for user in (None, self.visitor):  # Menguji guest dan akun biasa.
            self.client.force_authenticate(user=user)  # Memilih identitas test tanpa proses login browser.
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)  # Create harus ditolak.
            self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 403)  # Update harus ditolak.
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)  # Delete harus ditolak.
        self.assertEqual(Project.objects.count(), 1)  # Penolakan tidak boleh menambah atau menghapus data.

    def test_owner_can_create(self):  # Memeriksa pembuatan oleh superuser.
        self.client.force_authenticate(user=self.owner)  # Memberi identitas pemilik pada request test.
        response = self.client.post(self.list_url, self.payload, format="json")  # Mengirim proyek valid sebagai JSON.
        self.assertEqual(response.status_code, 201)  # Pembuatan harus menghasilkan 201.
        self.assertTrue(Project.objects.filter(pk=response.data["id"]).exists())  # Proyek baru benar-benar tersimpan.

    def test_validation(self):  # Memeriksa judul dan URL yang salah.
        self.client.force_authenticate(user=self.owner)  # Memakai akun yang diizinkan agar validasi dapat dijalankan.
        for value, field in [("   ", "title"), ('<img src="x">', "title"), ("javascript:alert(1)", "play_url")]:  # Menentukan kasus input salah.
            changes = {field: value}  # Mengubah satu field untuk setiap kasus.
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")  # Mengirim payload invalid.
            self.assertEqual(response.status_code, 400)  # Serializer harus menolak input.
            self.assertIn(field, response.data)  # Respons harus menunjukkan field bermasalah.
        self.assertEqual(Project.objects.count(), 1)  # Input salah tidak boleh tersimpan.

    def test_patch_put_and_delete(self):  # Memeriksa tiga method perubahan pada detail.
        self.client.force_authenticate(user=self.owner)  # Memakai pemilik untuk semua operasi.
        self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 200)  # PATCH satu field harus berhasil.
        self.assertEqual(self.client.put(self.detail_url, {"title": "Incomplete"}, format="json").status_code, 400)  # PUT tanpa field wajib harus gagal.
        self.assertEqual(self.client.put(self.detail_url, self.payload, format="json").status_code, 200)  # PUT lengkap harus berhasil.
        response = self.client.delete(self.detail_url)  # Menghapus proyek melalui API.
        self.assertEqual(response.status_code, 204)  # Penghapusan berhasil dengan 204.
        self.assertEqual(response.content, b"")  # Respons 204 tidak mempunyai body.
        self.assertFalse(Project.objects.filter(pk=self.project.id).exists())  # Proyek benar-benar terhapus.

    def test_star_requires_login_and_toggles(self):  # Memeriksa hak login serta dua keadaan star.
        self.assertEqual(self.client.post(self.star_url).status_code, 403)  # Guest tidak boleh memberi star.
        self.client.force_authenticate(user=self.visitor)  # Memakai akun biasa yang sudah login.
        self.assertTrue(self.client.post(self.star_url).data["is_starred"])  # POST pertama memberi star.
        self.assertFalse(self.client.post(self.star_url).data["is_starred"])  # POST kedua membatalkan star.

    def test_computed_fields_are_read_only(self):  # Memeriksa field star tidak bisa dipalsukan melalui create.
        self.client.force_authenticate(user=self.owner)  # Memakai pemilik yang boleh membuat proyek.
        response = self.client.post(self.list_url, {**self.payload, "star_count": 99, "is_starred": True, "starred_by": [self.visitor.id]}, format="json")  # Menyisipkan field yang tidak boleh ditulis.
        self.assertEqual(response.status_code, 201)  # Field read-only tidak menghalangi field valid disimpan.
        self.assertEqual(response.data["star_count"], 0)  # Nilai palsu harus diabaikan.
        self.assertFalse(response.data["is_starred"])  # Proyek baru belum diberi star.

    def test_editor_can_update_but_not_create_or_delete(self):  # Mempertahankan hak Editor dari project Anda.
        self.client.force_authenticate(user=self.editor)  # Memakai anggota grup Editor.
        self.assertEqual(self.client.patch(self.detail_url, {"title": "Edited"}, format="json").status_code, 200)  # Editor boleh mengubah proyek.
        self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)  # Editor tidak boleh membuat proyek.
        self.assertEqual(self.client.delete(self.detail_url).status_code, 403)  # Editor tidak boleh menghapus proyek.

    def test_wrong_method(self):  # Memeriksa penolakan method yang tidak terdaftar.
        self.client.force_authenticate(user=self.owner)  # Memakai pemilik agar permission tidak menutupi hasil method.
        self.assertEqual(self.client.delete(self.list_url).status_code, 405)  # DELETE tidak berlaku untuk URL daftar.

    def test_session_without_csrf_is_rejected(self):  # Memeriksa CSRF pada session browser sungguhan.
        client = APIClient(enforce_csrf_checks=True)  # Mengaktifkan pemeriksaan CSRF di klien test.
        self.assertTrue(client.login(username="owner", password="test-password"))  # Masuk lewat session Django.
        self.assertEqual(client.post(self.list_url, self.payload, format="json").status_code, 403)  # POST tanpa token harus ditolak.

    def test_session_with_csrf_succeeds(self):  # Memeriksa POST session yang menyertakan token.
        client = APIClient(enforce_csrf_checks=True)  # Mengaktifkan pemeriksaan CSRF sungguhan.
        self.assertTrue(client.login(username="owner", password="test-password"))  # Membuat session pemilik.
        self.assertEqual(client.get(self.list_url, HTTP_ACCEPT="text/html").status_code, 200)  # Membuka Browsable API untuk mendapatkan cookie CSRF.
        token = client.cookies["csrftoken"].value  # Membaca token yang dibuat oleh halaman Browsable API.
        response = client.post(self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token)  # Mengirim JSON dengan header CSRF.
        self.assertEqual(response.status_code, 201)  # POST dengan session dan token harus berhasil.