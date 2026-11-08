from django.test import TestCase, Client
from django.urls import reverse
from main.models import Education, Experience, Project, ArtItem


class PortfolioModelTests(TestCase):
    def setUp(self):
        Education.objects.create(
            institution="Universitas Indonesia",
            faculty="Faculty of Computer Science",
            start_period="Feb 2026",
            end_period="Present",
            logo_url="/static/img/Fasilkom.png"
        )
        Project.objects.create(
            title="KALANANTI",
            description="A narrative mystery game following two college students investigating their classmate's disappearance while exploring mental health and gender equality.",
            image_url="/static/img/KALANANTI.png",
            play_url="https://drive.google.com/file/d/1OK_3xH_K_dboh0rw14Nva7aNlUxKsUlb/view?usp=drive_link"
        )
        Experience.objects.create(
            title="Manager of Creative Development",
            organization="Open House Fasilkom UI 2026",
            description="Managing design sprints, visual identity, and event theme execution.",
            category="ORGANIZATION",
            is_ongoing=True,
            image_url="/static/img/OH26.jpg"
        )
        ArtItem.objects.create(
            title="Spritesheet 2",
            category="spritesheets",
            image_url="/static/img/sprite2.png"
        )

    def test_education_data(self):
        edu = Education.objects.get(institution="Universitas Indonesia")
        self.assertEqual(edu.faculty, "Faculty of Computer Science")
        self.assertEqual(edu.logo_url, "/static/img/Fasilkom.png")

    def test_project_data(self):
        proj = Project.objects.get(title="KALANANTI")
        self.assertTrue("mystery game" in proj.description)
        self.assertEqual(proj.play_url, "https://drive.google.com/file/d/1OK_3xH_K_dboh0rw14Nva7aNlUxKsUlb/view?usp=drive_link")

    def test_experience_data(self):
        exp = Experience.objects.get(title="Manager of Creative Development")
        self.assertEqual(exp.category, "ORGANIZATION")
        self.assertEqual(exp.organization, "Open House Fasilkom UI 2026")
        self.assertTrue(exp.is_ongoing)

    def test_artitem_data(self):
        art = ArtItem.objects.get(title="Spritesheet 2")
        self.assertEqual(art.category, "spritesheets")
        self.assertEqual(art.image_url, "/static/img/sprite2.png")


class PortfolioViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_routing(self):
        response = self.client.get(reverse('main:show_main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # ---- Projects page ----

    def test_projects_url_uses_correct_template(self):
        response = self.client.get(reverse('main:show_project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project.html')

    def test_projects_empty_state_appears_when_no_data(self):
        response = self.client.get(reverse('main:show_project'))
        self.assertContains(response, "Belum ada proyek yang ditambahkan.")

    # ---- Experience page ----

    def test_experience_url_uses_correct_template(self):
        response = self.client.get(reverse('main:show_experience'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience.html')

    def test_projects_data_appears_when_it_exists(self):  # Memastikan halaman menyediakan grid dan API menyediakan proyek.
        Project.objects.create(title="KALANANTI", description="A narrative mystery game.", image_url="/static/img/KALANANTI.png", play_url="https://example.com")  # Menyiapkan proyek dengan field wajib.
        page = self.client.get(reverse("main:show_project"))  # Mengambil HTML halaman Projects.
        self.assertContains(page, 'id="grid"')  # Memastikan wadah kartu AJAX tersedia.
        data = self.client.get(reverse("api:project-list")).json()  # Mengambil data dari API DRF yang dipakai halaman baru.
        self.assertEqual(data[0]["title"], "KALANANTI")  # Memastikan judul proyek dikirim API.

    def test_experience_data_appears_when_it_exists(self):  # Memastikan halaman Experience dan endpoint DRF menampilkan data yang sesuai.
        Experience.objects.create(  # Membuat Experience sebagai data awal pengujian.
            title="Manager of Creative Development",  # Menentukan title Experience.
            organization="Open House Fasilkom UI 2026",  # Menentukan organisasi Experience.
            description="Managing design sprints.",  # Menentukan deskripsi Experience.
            category="ORGANIZATION",  # Menggunakan kategori yang valid.
            is_ongoing=True,  # Menentukan bahwa pengalaman masih berlangsung.
            image_url="/static/img/OH26.jpg",  # Menentukan path gambar.
        )  # Mengakhiri pembuatan Experience.

        page = self.client.get(reverse("main:show_experience"))  # Mengambil HTML halaman Experience.
        self.assertContains(page, 'id="experience-grid"')  # Memastikan container untuk hasil API tersedia.

        data = self.client.get(reverse("api:experience-list")).json()  # Mengambil daftar Experience melalui API DRF baru.
        self.assertEqual(data[0]["organization"], "Open House Fasilkom UI 2026")  # Memastikan field organization tersedia pada respons API.
        self.assertNotIn("fields", data[0])  # Memastikan format respons tidak lagi menggunakan struktur JSON Django lama.


    def test_experience_empty_state_appears_when_no_data(self):
        response = self.client.get(reverse('main:show_experience'))
        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    # ---- Art page ----

    def test_art_url_uses_correct_template(self):
        response = self.client.get(reverse('main:show_art'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'art.html')

    def test_art_data_appears_when_it_exists(self):
        ArtItem.objects.create(
            title="Spritesheet 2",
            category="spritesheets",
            image_url="/static/img/sprite2.png"
        )
        response = self.client.get(reverse('main:show_art'))
        self.assertContains(response, "Spritesheet 2")

    def test_art_empty_state_appears_when_no_data(self):
        response = self.client.get(reverse('main:show_art'))
        self.assertContains(response, "Belum ada gambar karakter.")