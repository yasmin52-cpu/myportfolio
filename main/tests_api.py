import uuid  # Membuat UUID acak untuk uji objek yang tidak ada.
from django.contrib.auth.models import Group, User  # Membuat akun dan grup Editor di database test.
from django.urls import reverse  # Mencari URL berdasarkan nama route.
from rest_framework.test import APIClient, APITestCase  # Memakai klien dan kelas test DRF.
from main.models import Experience, Project  # Memeriksa perubahan model Experience & Project di database test.


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
        

class ExperienceAPITest(APITestCase):  # Mengelompokkan seluruh pengujian API Experience.
    def setUp(self):  # Menyiapkan akun dan data baru sebelum setiap test dijalankan.
        self.owner = User.objects.create_superuser("exp_owner", "exp_owner@example.com", "test-password")  # Membuat superuser yang memiliki semua hak CRUD.
        self.visitor = User.objects.create_user("exp_visitor", password="test-password")  # Membuat pengguna biasa yang hanya boleh membaca dan memberi star.
        self.editor = User.objects.create_user("exp_editor", password="test-password")  # Membuat pengguna yang akan diberi hak Editor.
        self.editor.groups.add(Group.objects.create(name="Editor"))  # Memasukkan pengguna Editor ke grup yang diperiksa permission class.

        self.experience = Experience.objects.create(  # Membuat satu Experience sebagai data awal pengujian.
            title="Creative Manager",  # Menentukan nama posisi atau peran.
            organization="Open House Fasilkom",  # Menentukan nama organisasi.
            description="Managing creative projects",  # Menentukan deskripsi pengalaman.
            category="ORGANIZATION",  # Memilih kategori yang valid sesuai model.
            is_ongoing=True,  # Menandai pengalaman masih berlangsung.
            image_url="/static/img/example.png",  # Memberikan path gambar contoh.
        )  # Mengakhiri pembuatan Experience.

        self.list_url = reverse("api:experience-list")  # Mengambil URL API daftar Experience berdasarkan nama route.
        self.detail_url = reverse("api:experience-detail", args=[self.experience.id])  # Mengambil URL API detail Experience yang sudah dibuat.
        self.star_url = reverse("api:experience-star", args=[self.experience.id])  # Mengambil URL API untuk toggle Star.

        self.payload = {  # Menyimpan data valid yang dapat digunakan berulang kali dalam test.
            "title": "Game Developer",  # Menentukan title Experience baru.
            "organization": "Indie Studio",  # Menentukan nama organisasi baru.
            "description": "Developing indie games",  # Menentukan deskripsi Experience baru.
            "category": "INTERNSHIP",  # Menggunakan pilihan kategori yang valid.
            "is_ongoing": False,  # Menentukan bahwa pengalaman sudah selesai.
            "image_url": "/static/img/game.png",  # Menentukan path gambar baru.
        }  # Mengakhiri dictionary payload.
    
    def test_public_list_and_detail(self):  # Memastikan Guest dapat membaca daftar dan detail Experience.
        response = self.client.get(self.list_url)  # Mengirim GET ke endpoint daftar tanpa login.
        self.assertEqual(response.status_code, 200)  # Memastikan GET daftar menghasilkan HTTP 200.
        self.assertEqual(len(response.data), 1)  # Memastikan terdapat satu Experience dari setUp.
        self.assertEqual(response.data[0]["title"], "Creative Manager")  # Memastikan title sesuai data awal.
        self.assertEqual(response.data[0]["stars_count"], 0)  # Memastikan jumlah star awal adalah nol.
        self.assertFalse(response.data[0]["has_starred"])  # Memastikan Guest belum memberikan star.
        self.assertNotIn("fields", response.data[0])  # Memastikan respons menggunakan format DRF, bukan format JSON Django lama.
        self.assertEqual(self.client.get(self.detail_url).status_code, 200)  # Memastikan endpoint detail juga dapat diakses Guest.

    def test_search_and_empty_results(self):  # Memastikan parameter pencarian bekerja pada title dan organization.
        response = self.client.get(self.list_url, {"q": "creative"})  # Mencari berdasarkan title tanpa memperhatikan kapitalisasi.
        self.assertEqual(len(response.data), 1)  # Memastikan pencarian title menemukan Experience.
        response = self.client.get(self.list_url, {"q": "fasilkom"})  # Mencari berdasarkan nama organisasi.
        self.assertEqual(len(response.data), 1)  # Memastikan pencarian organization juga berhasil.
        response = self.client.get(self.list_url, {"q": "tidak-ada"})  # Mencari kata yang tidak cocok dengan data mana pun.
        self.assertEqual(response.data, [])  # Memastikan hasil kosong berupa array kosong.

    def test_missing_experience(self):  # Memastikan permintaan detail untuk ID yang tidak ada menghasilkan 404.
        missing_url = reverse("api:experience-detail", args=[999999])  # Membentuk URL untuk ID Experience yang tidak tersimpan.
        response = self.client.get(missing_url)  # Mengirim request GET ke ID tersebut.
        self.assertEqual(response.status_code, 404)  # Memastikan server mengembalikan HTTP 404.

    def test_guest_and_visitor_cannot_manage(self):  # Menguji penolakan operasi CRUD untuk Guest dan User biasa.
        for user in (None, self.visitor):  # Menjalankan pengujian untuk Guest dan akun biasa.
            with self.subTest(user=user):  # Memisahkan hasil pengujian berdasarkan identitas pengguna.
                self.client.force_authenticate(user=user)  # Mengatur identitas request tanpa proses login browser.
                response = self.client.post(self.list_url, self.payload, format="json")  # Mencoba membuat Experience baru.
                self.assertEqual(response.status_code, 403)  # Memastikan pembuatan ditolak.
                response = self.client.patch(self.detail_url, {"title": "Hacked"}, format="json")  # Mencoba mengubah title Experience.
                self.assertEqual(response.status_code, 403)  # Memastikan PATCH ditolak.
                response = self.client.put(self.detail_url, self.payload, format="json")  # Mencoba mengganti seluruh data Experience.
                self.assertEqual(response.status_code, 403)  # Memastikan PUT ditolak.
                response = self.client.delete(self.detail_url)  # Mencoba menghapus Experience.
                self.assertEqual(response.status_code, 403)  # Memastikan DELETE ditolak.
                self.experience.refresh_from_db()  # Membaca ulang Experience dari database setelah request ditolak.
                self.assertEqual(self.experience.title, "Creative Manager")  # Memastikan title tidak berubah.
                self.assertEqual(Experience.objects.count(), 1)  # Memastikan tidak ada Experience yang dibuat atau dihapus.

    def test_editor_can_update_but_not_create_or_delete(self):  # Memeriksa hak Editor sesuai requirement IA6.
        self.client.force_authenticate(user=self.editor)  # Mengautentikasi request sebagai anggota grup Editor.
        response = self.client.patch(self.detail_url, {"title": "Updated by Editor"}, format="json")  # Mengubah satu field melalui PATCH.
        self.assertEqual(response.status_code, 200)  # Memastikan PATCH berhasil.
        self.experience.refresh_from_db()  # Mengambil data terbaru dari database.
        self.assertEqual(self.experience.title, "Updated by Editor")  # Memastikan perubahan benar-benar tersimpan.
        response = self.client.put(self.detail_url, self.payload, format="json")  # Mengirim seluruh field melalui PUT.
        self.assertEqual(response.status_code, 200)  # Memastikan Editor juga boleh menggunakan PUT.
        response = self.client.post(self.list_url, self.payload, format="json")  # Mencoba membuat Experience baru.
        self.assertEqual(response.status_code, 403)  # Memastikan Editor tidak boleh membuat Experience.
        response = self.client.delete(self.detail_url)  # Mencoba menghapus Experience.
        self.assertEqual(response.status_code, 403)  # Memastikan Editor tidak boleh menghapus Experience.
        self.experience.refresh_from_db()  # Memastikan objek masih tersedia setelah DELETE ditolak.
        self.assertEqual(self.experience.title, self.payload["title"])  # Memastikan nilai dari PUT tetap tersimpan.
        self.assertEqual(Experience.objects.count(), 1)  # Memastikan jumlah Experience tidak berubah akibat request terlarang.

    def test_owner_can_create_and_delete(self):  # Memastikan pemilik portofolio memiliki hak membuat dan menghapus Experience.
        self.client.force_authenticate(user=self.owner)  # Mengautentikasi request sebagai superuser.
        response = self.client.post(self.list_url, self.payload, format="json")  # Mengirim request POST untuk membuat Experience.
        self.assertEqual(response.status_code, 201)  # Memastikan pembuatan menghasilkan HTTP 201.
        new_id = response.data["id"]  # Mengambil ID Experience yang baru dibuat.
        self.assertTrue(Experience.objects.filter(pk=new_id).exists())  # Memastikan Experience baru benar-benar tersimpan.
        detail_url = reverse("api:experience-detail", args=[new_id])  # Membentuk URL detail untuk Experience baru.
        response = self.client.delete(detail_url)  # Mengirim DELETE untuk menghapus Experience tersebut.
        self.assertEqual(response.status_code, 204)  # Memastikan penghapusan menghasilkan HTTP 204.
        self.assertEqual(response.content, b"")  # Memastikan respons 204 tidak memiliki body.
        self.assertFalse(Experience.objects.filter(pk=new_id).exists())  # Memastikan Experience baru sudah terhapus dari database.
        
    
    def test_validation_rejects_invalid_text(self):  # Menguji validasi field teks pada ExperienceSerializer.
        self.client.force_authenticate(user=self.owner)  # Memakai superuser agar request mencapai serializer.
        invalid_cases = [  # Menyimpan pasangan field dan nilai yang seharusnya ditolak.
            ("title", "   "),  # Menguji title yang hanya berisi spasi.
            ("title", "<b></b>"),  # Menguji title yang menjadi kosong setelah tag HTML dibuang.
            ("organization", "   "),  # Menguji organization yang hanya berisi spasi.
            ("description", "<p></p>"),  # Menguji description yang hanya berisi tag HTML.
        ]  # Mengakhiri daftar kasus validasi.
        for field, value in invalid_cases:  # Menjalankan pengujian untuk setiap input tidak valid.
            with self.subTest(field=field, value=value):  # Memberi identitas terpisah pada setiap kasus.
                payload = {**self.payload, field: value}  # Membuat payload baru dengan satu field tidak valid.
                response = self.client.post(self.list_url, payload, format="json")  # Mengirim data tidak valid ke API.
                self.assertEqual(response.status_code, 400)  # Memastikan serializer mengembalikan HTTP 400.
                self.assertIn(field, response.data)  # Memastikan respons menyebutkan field yang bermasalah.
        self.assertEqual(Experience.objects.count(), 1)  # Memastikan tidak ada data tidak valid yang tersimpan.

    def test_validation_strips_html_tags(self):  # Memastikan serializer membersihkan tag HTML pada input valid.
        self.client.force_authenticate(user=self.owner)  # Mengautentikasi request sebagai superuser.
        payload = {**self.payload, "title": "<b>Game Developer</b>"}  # Membuat title yang mengandung tag HTML.
        response = self.client.post(self.list_url, payload, format="json")  # Mengirim payload ke API.
        self.assertEqual(response.status_code, 201)  # Memastikan data valid tetap diterima.
        self.assertEqual(response.data["title"], "Game Developer")  # Memastikan tag HTML dihapus dari respons.
        self.assertEqual(Experience.objects.get(pk=response.data["id"]).title, "Game Developer")  # Memastikan database menyimpan teks yang sudah dibersihkan.

    
    def test_star_requires_login_and_toggles(self):  # Menguji autentikasi serta perubahan status star.
        response = self.client.post(self.star_url)  # Guest mencoba memberikan star tanpa login.
        self.assertEqual(response.status_code, 403)  # Memastikan Guest ditolak.
        self.assertEqual(self.experience.starred_by.count(), 0)  # Memastikan request Guest tidak menambahkan star.

        self.client.force_authenticate(user=self.visitor)  # Mengautentikasi request sebagai User biasa.
        response = self.client.post(self.star_url)  # Mengirim POST pertama untuk memberikan star.
        self.assertEqual(response.status_code, 200)  # Memastikan request berhasil.
        self.assertTrue(response.data["has_starred"])  # Memastikan API menyatakan pengguna sudah memberi star.
        self.assertEqual(response.data["stars_count"], 1)  # Memastikan jumlah star bertambah menjadi satu.
        self.assertTrue(self.experience.starred_by.filter(pk=self.visitor.pk).exists())  # Memastikan relasi star benar-benar tersimpan.

        response = self.client.post(self.star_url)  # Mengirim POST kedua untuk membatalkan star.
        self.assertEqual(response.status_code, 200)  # Memastikan pembatalan berhasil.
        self.assertFalse(response.data["has_starred"])  # Memastikan status star menjadi false.
        self.assertEqual(response.data["stars_count"], 0)  # Memastikan jumlah star kembali menjadi nol.
        self.assertFalse(self.experience.starred_by.filter(pk=self.visitor.pk).exists())  # Memastikan relasi star sudah dihapus.
        
    def test_computed_star_fields_are_read_only(self):  # Memastikan field hasil perhitungan tidak dapat diubah langsung oleh klien.
        self.client.force_authenticate(user=self.owner)  # Memakai superuser yang diizinkan membuat Experience.
        payload = {**self.payload, "stars_count": 999, "has_starred": True, "starred_by": [self.visitor.id]}  # Menyisipkan nilai star palsu ke request.
        response = self.client.post(self.list_url, payload, format="json")  # Mengirim payload yang mengandung field read-only.
        self.assertEqual(response.status_code, 201)  # Memastikan field tambahan tidak menghalangi pembuatan data valid.
        self.assertEqual(response.data["stars_count"], 0)  # Memastikan jumlah star tidak mengikuti nilai palsu.
        self.assertFalse(response.data["has_starred"])  # Memastikan status star tetap false.
        self.assertEqual(Experience.objects.get(pk=response.data["id"]).starred_by.count(), 0)  # Memastikan tidak ada relasi star palsu di database.
    
    def test_session_without_csrf_is_rejected(self):  # Memastikan request POST dengan session tetapi tanpa CSRF ditolak.
        client = APIClient(enforce_csrf_checks=True)  # Membuat API client dengan pemeriksaan CSRF aktif.
        self.assertTrue(client.login(username="exp_owner", password="test-password"))  # Melakukan login melalui session Django.
        response = client.post(self.list_url, self.payload, format="json")  # Mengirim POST tanpa header X-CSRFToken.
        self.assertEqual(response.status_code, 403)  # Memastikan SessionAuthentication menolak request tanpa CSRF.
        self.assertEqual(Experience.objects.count(), 1)  # Memastikan request yang ditolak tidak membuat Experience baru.

    def test_session_with_csrf_succeeds(self):  # Memastikan request POST dengan token CSRF yang valid berhasil.
        client = APIClient(enforce_csrf_checks=True)  # Membuat client dengan pemeriksaan CSRF aktif.
        self.assertTrue(client.login(username="exp_owner", password="test-password"))  # Login menggunakan akun superuser.
        response = client.get(self.list_url, HTTP_ACCEPT="text/html")  # Membuka Browsable API agar cookie CSRF dibuat.
        self.assertEqual(response.status_code, 200)  # Memastikan Browsable API dapat diakses.
        token = client.cookies["csrftoken"].value  # Mengambil token CSRF dari cookie client.
        response = client.post(self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token)  # Mengirim POST dengan header CSRF yang valid.
        self.assertEqual(response.status_code, 201)  # Memastikan API menerima request dengan token CSRF.
        self.assertEqual(Experience.objects.count(), 2)  # Memastikan Experience baru tersimpan di database.

