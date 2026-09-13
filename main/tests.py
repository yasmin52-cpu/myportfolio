from django.test import TestCase, Client
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
            category="COMMITTEE",
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
        self.assertEqual(exp.category, "COMMITTEE")
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
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)