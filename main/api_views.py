from django.shortcuts import get_object_or_404  # Menghasilkan 404 jika UUID tidak menunjuk proyek.
from rest_framework import status  # Menyediakan konstanta status HTTP yang mudah dibaca.
from rest_framework.authentication import SessionAuthentication  # Memakai session login Django yang sudah ada.
from rest_framework.decorators import api_view, authentication_classes, permission_classes  # Mengonfigurasi function based API views.
from rest_framework.permissions import IsAuthenticated  # Membatasi pemberian star ke pengguna login.
from rest_framework.response import Response  # Mengirim data melalui renderer DRF.
from main.models import Experience, Project  # Memakai tabel Project yang sama dengan halaman HTML.
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly  # Memakai hak pemilik dan Editor yang sudah disesuaikan.
from main.serializers import ExperienceSerializer, ProjectSerializer  # Memakai kontrak data dan validasi API.


@api_view(["GET", "HEAD", "POST"])  # Daftar dapat dibaca; POST membuat proyek baru.
@authentication_classes([SessionAuthentication])  # Membaca pengguna dari cookie session Django.
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])  # Hanya pemilik dapat melakukan POST.
def project_list(request):  # Menangani koleksi proyek pada satu URL.
    if request.method in ("GET", "HEAD"):  # Memilih jalur baca tanpa mengubah data.
        projects = Project.objects.prefetch_related("starred_by").order_by("title", "id")  # Mengurutkan hasil dan memuat relasi star.
        title = request.query_params.get("title", "").strip()  # Membaca kata pencarian yang dipakai frontend lama.
        if title:  # Menyaring hanya bila pengguna memberi kata pencarian.
            projects = projects.filter(title__icontains=title)  # Mencari judul tanpa membedakan huruf besar.
        serializer = ProjectSerializer(projects, many=True, context={"request": request})  # Mengubah kumpulan model menjadi daftar data.
        return Response(serializer.data)  # Mengirim daftar, termasuk [] bila tidak ada hasil.
    serializer = ProjectSerializer(data=request.data, context={"request": request})  # Membaca JSON atau form dari request POST.
    serializer.is_valid(raise_exception=True)  # Menghasilkan 400 dan error per field bila input salah.
    serializer.save()  # Menyimpan proyek setelah validasi berhasil.
    return Response(serializer.data, status=status.HTTP_201_CREATED)  # Mengirim proyek baru dengan status 201.


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])  # Menyediakan baca, ubah, dan hapus pada satu proyek.
@authentication_classes([SessionAuthentication])  # Memakai session login yang sama.
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])  # Editor hanya boleh PUT atau PATCH.
def project_detail(request, project_id):  # Menangani proyek yang ID-nya berasal dari URL.
    project = get_object_or_404(Project.objects.prefetch_related("starred_by"), pk=project_id)  # Mengambil objek atau menghasilkan 404.
    if request.method in ("GET", "HEAD"):  # Memilih jalur baca detail.
        serializer = ProjectSerializer(project, context={"request": request})  # Mengubah satu proyek menjadi data respons.
        return Response(serializer.data)  # Mengirim detail dengan status 200.
    if request.method == "DELETE":  # Memilih jalur penghapusan yang hanya diizinkan untuk superuser.
        project.delete()  # Menghapus proyek yang diminta.
        return Response(status=status.HTTP_204_NO_CONTENT)  # Mengirim keberhasilan tanpa body JSON.
    serializer = ProjectSerializer(project, data=request.data, partial=request.method == "PATCH", context={"request": request})  # PATCH mengizinkan hanya field yang berubah.
    serializer.is_valid(raise_exception=True)  # Menghasilkan 400 jika data pengganti tidak valid.
    serializer.save()  # Memperbarui objek yang sudah ada.
    return Response(serializer.data)  # Mengirim nilai terbaru dengan status 200.


@api_view(["POST"])  # Star adalah aksi toggle yang hanya menerima POST.
@authentication_classes([SessionAuthentication])  # Mengenali akun dari session browser.
@permission_classes([IsAuthenticated])  # Semua akun login boleh memberi atau membatalkan star.
def project_star(request, project_id):  # Menangani star untuk satu proyek.
    project = get_object_or_404(Project, pk=project_id)  # Memastikan proyek yang dituju ada.
    if project.starred_by.filter(pk=request.user.pk).exists():  # Memeriksa star pengguna yang sedang login.
        project.starred_by.remove(request.user)  # Membatalkan star bila relasi sudah ada.
    else:  # Menangani pengguna yang belum memberi star.
        project.starred_by.add(request.user)  # Menambahkan star tanpa menerima ID pengguna dari klien.
    serializer = ProjectSerializer(project, context={"request": request})  # Menghitung keadaan star terbaru.
    return Response(serializer.data)  # Mengirim proyek terbaru dengan status 200.

@api_view(["GET", "HEAD", "POST"])  # Menyediakan daftar publik dan pembuatan Experience.
@authentication_classes([SessionAuthentication])  # Memakai session login situs.
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])  # Hanya superuser dapat membuat.
def experience_list(request):  # Menangani koleksi pengalaman.
    if request.method in ("GET", "HEAD"):  # Memilih jalur daftar.
        experiences = Experience.objects.prefetch_related("starred_by").order_by("id")  # Memuat relasi star dan menjaga urutan.
        query = request.query_params.get("q", "").strip()  # Membaca parameter pencarian yang sudah dipakai halaman.
        if query:  # Menyaring hanya jika ada kata pencarian.
            from django.db.models import Q  # Mengimpor pembentuk kondisi OR untuk dua field pencarian.
            experiences = experiences.filter(Q(title__icontains=query) | Q(organization__icontains=query))  # Mencari role atau organisasi.
        serializer = ExperienceSerializer(experiences, many=True, context={"request": request})  # Mengubah kumpulan pengalaman ke daftar data.
        return Response(serializer.data)  # Mengirim daftar dengan status 200.
    serializer = ExperienceSerializer(data=request.data, context={"request": request})  # Membaca data pengalaman baru.
    serializer.is_valid(raise_exception=True)  # Menolak input salah dengan status 400.
    serializer.save()  # Menyimpan pengalaman yang sudah valid.
    return Response(serializer.data, status=status.HTTP_201_CREATED)  # Mengirim objek baru dengan status 201.


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])  # Menyediakan detail dan perubahan Experience.
@authentication_classes([SessionAuthentication])  # Memakai session situs yang sama.
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])  # Editor dapat update; hanya superuser dapat delete.
def experience_detail(request, experience_id):  # Menangani satu pengalaman berdasarkan ID integer.
    experience = get_object_or_404(Experience.objects.prefetch_related("starred_by"), pk=experience_id)  # Mengambil objek atau menghasilkan 404.
    if request.method in ("GET", "HEAD"):  # Memilih jalur baca.
        return Response(ExperienceSerializer(experience, context={"request": request}).data)  # Mengirim detail dengan status 200.
    if request.method == "DELETE":  # Memilih jalur hapus yang dibatasi permission.
        experience.delete()  # Menghapus pengalaman.
        return Response(status=status.HTTP_204_NO_CONTENT)  # Mengirim respons kosong sesuai kontrak DELETE.
    serializer = ExperienceSerializer(experience, data=request.data, partial=request.method == "PATCH", context={"request": request})  # Menyiapkan PUT lengkap atau PATCH sebagian.
    serializer.is_valid(raise_exception=True)  # Memastikan perubahan valid sebelum disimpan.
    serializer.save()  # Memperbarui pengalaman yang ada.
    return Response(serializer.data)  # Mengirim pengalaman terbaru.


@api_view(["POST"])  # Star Experience hanya berubah melalui POST.
@authentication_classes([SessionAuthentication])  # Mengenali akun dari session.
@permission_classes([IsAuthenticated])  # Mengizinkan semua akun login.
def experience_star(request, experience_id):  # Menangani toggle star satu pengalaman.
    experience = get_object_or_404(Experience, pk=experience_id)  # Memastikan ID pengalaman benar.
    if experience.starred_by.filter(pk=request.user.pk).exists():  # Memeriksa star pengguna ini.
        experience.starred_by.remove(request.user)  # Membatalkan star yang sudah ada.
    else:  # Menangani keadaan belum memberi star.
        experience.starred_by.add(request.user)  # Memberi star atas nama pengguna login.
    return Response(ExperienceSerializer(experience, context={"request": request}).data)  # Mengirim keadaan star terbaru.