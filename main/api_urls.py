from django.urls import path  # Mengimpor pembuat pola URL Django.
from main import api_views  # Menghubungkan pola URL ke view API yang baru.

app_name = "api"  # Memberi namespace terpisah dari URL halaman utama.
urlpatterns = [  # Menyimpan seluruh endpoint Project versi pertama.
    path("projects/", api_views.project_list, name="project-list"),  # GET daftar dan POST tambah.
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),  # GET, PUT, PATCH, dan DELETE satu proyek.
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),  # POST untuk memberi atau membatalkan star.
    path("experiences/", api_views.experience_list, name="experience-list"),  # GET daftar dan POST tambah Experience.
    path("experiences/<int:experience_id>/", api_views.experience_detail, name="experience-detail"),  # GET, PUT, PATCH, DELETE Experience.
    path("experiences/<int:experience_id>/star/", api_views.experience_star, name="experience-star"),  # POST toggle star Experience.
]