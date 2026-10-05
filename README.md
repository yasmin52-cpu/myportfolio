# Portofolio Pribadi

## Deskripsi

Website portofolio pribadi static untuk **Pemrograman Berbasis Platform (CSGE602022)**, Tugas Individu 1, Fakultas Ilmu Komputer, Universitas Indonesia, Semester Gasal 2026/2027.

Website ini menampilkan profil **About Me**, riwayat pendidikan, galeri proyek, pengalaman organisasi, dan **Art Portfolio** dengan kategori bertab.

* **Nama:** Yasmin
* **NPM:** 2506606124

## Teknologi

* HTML5 dengan elemen semantik
* CSS3
* CSS Grid dan Flexbox
* CSS Variables
* `clamp()` untuk ukuran teks responsif
* CSS keyframe animation
* HTML dan CSS native
* Django sebagai template/server untuk menjalankan halaman melalui `manage.py runserver`
* CSS radio-button/label untuk perpindahan tab pada Art Portfolio tanpa JavaScript

Website ini tidak menggunakan JavaScript maupun API untuk fitur pada halaman portofolio, serta tidak menggunakan database untuk menyimpan atau menampilkan data portfolio.

## Struktur Proyek

```text
myportfolio/
├── portfolio/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── ... (foto profil, screenshot proyek, logo organisasi, aset art)
├── templates/
│   └── index.html
├── manage.py
├── requirements.txt
├── db.sqlite3
├── .env
├── .env.prod
├── .gitignore
└── README.md
```

## Cara Menjalankan

1. Clone repository dan masuk ke folder proyek.
2. Buat dan aktifkan virtual environment jika diperlukan.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Jalankan development server:

```bash
python manage.py runserver
```

5. Buka `http://127.0.0.1:8000/` pada browser.

Website juga dapat diakses melalui deployment berikut:

`https://yasmin52-myportfolio.pws.cs.ui.ac.id/`

---

# Tugas 1

## 1. Penggunaan Elemen Semantik HTML5

Pada Tutorial dan Tugas 1, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, dan `<aside>` karena struktur konten pada portofolio saya memang dapat dibagi menjadi beberapa bagian dengan fungsi yang berbeda.

`<header>` digunakan untuk bagian navigasi utama, sedangkan `<main>` menjadi pembungkus konten utama halaman. Setiap bagian utama seperti Profile, Education, Projects, Experiences, dan Art Portfolio menggunakan `<section>` dengan `id` masing-masing, seperti `#profile`, `#education`, `#projects`, `#experiences`, dan `#art-portfolio`. Kartu proyek dan pengalaman organisasi menggunakan `<article>` karena setiap kartu dapat dipahami sebagai satu unit informasi yang berdiri sendiri, misalnya memiliki nama, gambar, deskripsi, dan link.

Pada Art Portfolio, menu kategori ditempatkan dalam `<aside>` karena menu tersebut berfungsi sebagai informasi atau navigasi pelengkap terhadap galeri utama.

Penggunaan elemen semantik juga membantu saya saat membuat static web karena struktur HTML menjadi lebih jelas. Misalnya, navigasi dapat langsung mengarah ke `id` masing-masing section menggunakan `href="#projects"` dan sebagainya, sehingga perpindahan antarbagian dapat dilakukan tanpa JavaScript. Struktur tersebut juga membuat CSS lebih mudah diorganisasi karena saya dapat menggunakan class yang spesifik untuk setiap jenis komponen seperti `.portfolio-section`, `.project-card`, dan `.experience-card`.

Saya juga menggunakan `aria-label` pada elemen navigasi, seperti `aria-label="Primary"` dan `aria-label="Art categories"`, untuk memberikan informasi tambahan mengenai fungsi navigasi tersebut.

## 2. Tantangan Responsive Design

Tantangan responsive terbesar yang saya temukan terdapat pada hero section, navigation, dan Art Portfolio.

Pada hero section, saya menggunakan CSS Grid dengan `grid-template-areas` agar pada layar besar bagian identity dan details berada di sebelah kiri sementara foto berada di sebelah kanan. Pada layar kecil, layout tersebut diubah menjadi satu kolom dengan urutan identity → photo → details. Dengan cara ini, informasi utama tetap dapat dibaca dengan nyaman tanpa mempertahankan layout desktop yang terlalu sempit pada mobile.

Ukuran judul nama juga menggunakan `clamp(3rem, 7vw, 5rem)` sehingga ukurannya dapat menyesuaikan lebar layar secara bertahap tanpa membutuhkan banyak breakpoint khusus.

Pada project grid, saya menggunakan `repeat(auto-fit, minmax(280px, 1fr))`. Dengan pendekatan tersebut, jumlah kolom dapat menyesuaikan ruang yang tersedia secara otomatis. Saya memilih pendekatan ini dibandingkan menetapkan jumlah kolom secara tetap karena ukuran kartu perlu tetap cukup besar agar teks dan gambar dapat dibaca.

Bagian yang paling membutuhkan penyesuaian adalah Art Portfolio. Layout awalnya menggunakan dua kolom dengan sidebar selebar 280px dan galeri pada kolom lainnya. Pada layar kecil, kedua bagian tersebut menjadi terlalu sempit jika tetap diletakkan berdampingan. Oleh karena itu, pada lebar maksimal 768px layout diubah menjadi satu kolom sehingga sidebar kategori dan galeri ditumpuk secara vertikal.

Saya mengevaluasi responsive design dengan mengubah ukuran browser dari desktop hingga sekitar 360px dan memeriksa apakah elemen penting tetap terbaca, tidak keluar dari layar, serta tidak menyebabkan horizontal overflow. Saya juga memperhatikan elemen yang memiliki prioritas informasi lebih tinggi, seperti identitas pada hero section, agar tetap muncul sebelum elemen pendukung ketika ruang layar menjadi terbatas.

## 3. Keterbatasan Static Web dan Rencana Pengembangan

Karena website ini masih merupakan static web, data seperti daftar proyek, pengalaman organisasi, dan gambar Art Portfolio ditulis langsung di dalam HTML. Akibatnya, ketika saya ingin menambahkan proyek atau pengalaman baru, saya harus mengubah HTML secara manual dan mempertahankan struktur elemen yang sudah ada.

Hal tersebut masih sesuai untuk portfolio dengan jumlah konten yang relatif sedikit, tetapi menjadi kurang praktis jika jumlah proyek terus bertambah. Pengelolaan konten juga akan lebih sulit jika suatu saat data perlu diperbarui tanpa mengubah source code secara langsung.

Fitur yang paling ingin saya tambahkan pada iterasi berikutnya adalah form kontak yang benar-benar dapat mengirim atau menyimpan pesan. Saat ini kontak masih menggunakan pendekatan seperti link `mailto:`, sedangkan form yang benar-benar memproses pesan membutuhkan pemrosesan server-side. Fitur tersebut menjadi contoh yang relevan untuk dikembangkan ketika materi database dan arsitektur MVT mulai digunakan pada pertemuan berikutnya.

---

# Pengungkapan Penggunaan AI

Saya menggunakan **Google Gemini** sebagai alat bantu selama proses pengerjaan dan evaluasi proyek. Penggunaan AI terutama dilakukan untuk membantu memecahkan masalah HTML/CSS tertentu, mengevaluasi struktur kode, memperbaiki masalah responsive design, serta membantu dokumentasi dan pengecekan terhadap requirement tugas.

AI digunakan sebagai alat bantu, bukan sebagai pengganti proses evaluasi dan pengujian saya sendiri. Saya tetap memeriksa apakah saran yang diberikan sesuai dengan desain yang saya inginkan dan dengan batasan tugas.

## AI yang Digunakan

### Google Gemini

Google Gemini digunakan terutama untuk menyelesaikan masalah pada bagian **Art Portfolio**, terutama:

* styling tombol tab aktif tanpa mengubah ukuran sidebar;
* mengatur ukuran gambar pada galeri;
* memastikan gambar dapat terlihat utuh;
* membuat infinite marquee carousel;
* menyesuaikan jumlah duplikat item pada marquee agar animasinya dapat berulang dengan mulus;
* beberapa pertanyaan mengenai proses commit, push, dan submission Git.

Percakapan Gemini yang digunakan selama proses pengerjaan dapat dilihat pada:

https://share.gemini.google/bvBy1buPkZr6

## Bagian Proyek yang Dibantu AI

Bantuan AI paling intensif digunakan pada detail interaktif dan visual di **Art Portfolio**, terutama:

* styling tombol tab aktif melalui `.art-nav-btn` dan selector `#tab-* :checked`;
* pengaturan ukuran gambar melalui `.art-slide` dan `.art-slide img`;
* struktur infinite marquee melalui `.art-marquee-track`;
* animasi `@keyframes scrollArtMarquee`;
* penyesuaian struktur HTML agar jumlah item pada marquee sesuai.

Sementara itu, bagian Hero, Education, Projects, dan Experiences terutama dibangun secara mandiri, meskipun beberapa bagiannya juga diperiksa atau didiskusikan dengan AI.

## Keterbatasan dan Kesalahan Output AI

Salah satu bagian yang tidak berhasil dibuat AI sesuai dengan hasil yang saya inginkan adalah styling gambar pada project card. Pada awalnya, AI memberikan beberapa solusi untuk mengatur ukuran gambar, border, dan overflow, tetapi hasilnya masih tidak sesuai dengan desain yang saya inginkan dari wireframe. Beberapa percobaan justru membuat gambar terpotong atau keluar dari area card.

Karena itu, saya melakukan iterasi sendiri sampai menemukan struktur CSS yang lebih sesuai dengan desain. Saya memisahkan styling gambar project dari styling foto profil dengan menggunakan class .card-image, kemudian mengatur gambar menggunakan rasio 16:9, object-fit: cover, dan border-radius agar gambar terlihat seperti rounded rectangle yang "terkunci" di dalam card.

Kemudian, begitu juga ketika saya mencoba memberikan border pada tombol tab yang aktif tanpa menyebabkan perubahan ukuran atau pergeseran layout sidebar.

Pada percobaan pertama, Gemini menyarankan penggunaan `border` biasa pada state aktif. Ketika dicoba di browser, ukuran/layout masih berubah.

Pada percobaan kedua, Gemini menyarankan `box-sizing: border-box` dan border transparan yang sudah disiapkan sejak awal. Pendekatan tersebut juga masih menghasilkan perubahan yang tidak saya inginkan.

Saya kemudian kembali memberikan hasil percobaan tersebut kepada Gemini dan menggunakan pendekatan ketiga, yaitu `box-shadow: inset`. Pendekatan tersebut kemudian digunakan pada versi final karena dapat memberikan efek border di dalam elemen tanpa menambah ukuran box.

Contoh lain terdapat pada styling `.art-slide`. Gemini menyarankan background putih transparan dan border pada setiap slide ketika membantu membuat gambar terlihat utuh. Setelah saya lihat pada desain keseluruhan, kedua elemen tersebut menurut saya tidak diperlukan dan membuat galeri menjadi lebih ramai. Saya kemudian menghapus background dan border tersebut dari versi final.

Saya juga mengganti `height: 280px` menjadi `max-height: 280px` agar gambar dengan aspect ratio berbeda tidak dipaksa memiliki tinggi yang sama secara kaku.

Contoh-contoh tersebut membuat saya menyadari bahwa output AI yang secara teknis masuk akal belum tentu merupakan solusi terbaik untuk kebutuhan desain tertentu. Hasil dari AI tetap perlu dicoba, dibandingkan dengan kebutuhan awal, dan diperbaiki secara manual.

## Review dan Modifikasi yang Saya Lakukan

Beberapa perubahan yang saya lakukan setelah mengevaluasi saran AI adalah:

* mengganti `height: 280px` menjadi `max-height: 280px` pada `.art-slide`;
* menghapus `background-color: rgba(255,255,255,0.5)` dari `.art-slide`;
* menghapus `border: 2px solid var(--line)` dari `.art-slide`;
* memindahkan flex centering dari `.art-slide` ke `.art-gallery-container`;
* menghapus markup `sidebar-preview-box` dan `preview-img` yang tidak saya perlukan pada desain final;
* mengubah pendekatan border tombol aktif menjadi `box-shadow: inset`;
* menyesuaikan warna border aktif menjadi `var(--accent)`;
* memastikan jumlah item pada marquee sesuai antara konten asli dan duplikasinya.

Perubahan tersebut dilakukan setelah melihat hasil implementasi dan membandingkannya dengan kebutuhan desain, bukan hanya menerima output AI secara langsung.

## Hal yang Saya Pelajari dari Proses Koreksi

Dari proses tersebut, saya menjadi lebih memahami bahwa `border` merupakan bagian dari ukuran box yang dapat memengaruhi layout, sedangkan `box-shadow` dapat digunakan untuk memberikan efek visual tanpa mengubah ukuran elemen yang menjadi targetnya. Hal ini membantu saya memahami mengapa pendekatan `box-shadow: inset` lebih sesuai untuk kasus tombol tab pada proyek saya.

Saya juga memahami lebih jelas hubungan antara struktur HTML yang diduplikasi dengan animasi marquee. Ketika track digerakkan dengan `translateX(-50%)`, bagian kedua harus memiliki struktur dan jumlah item yang sesuai dengan bagian pertama agar perpindahan dari akhir satu grup ke awal grup berikutnya tidak menghasilkan lompatan yang terlihat.

Selain itu, proses ini membuat saya lebih terbiasa memperlakukan output AI sebagai sebuah saran yang perlu diuji. Ketika solusi pertama dan kedua tidak menghasilkan perilaku yang diinginkan, saya tidak langsung mempertahankannya, tetapi menguji hasilnya di browser dan mencari pendekatan lain.

## Integrasi AI dalam Proses Pengerjaan

AI digunakan sebagai alat bantu untuk troubleshooting, review, dan dokumentasi. Saya tidak menyimpan semua saran AI apa adanya.

Contohnya, beberapa bagian yang diberikan Gemini untuk `.art-slide` akhirnya saya hapus karena tidak sesuai dengan desain final. Saya juga kembali memberikan feedback ketika solusi border pertama dan kedua tidak berhasil.

Bagian marquee yang disarankan AI dapat digunakan setelah struktur HTML-nya disesuaikan. 

Dengan demikian, proses pengerjaan terdiri dari siklus **mencoba → menguji → mengevaluasi → memperbaiki**, bukan hanya menyalin kode yang diberikan AI.

---

# Log Bantuan AI

| Tahap                                 | AI     | Tujuan/Prompt                                            | Bantuan AI                                                                                                                          | Tindakan Manual Saya                                                                                                 | Hasil                                                 |
| ------------------------------------- | ------ | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Border tombol tab aktif — percobaan 1 | Gemini | Menambahkan border pada tombol tab saat aktif            | Menyarankan `border` biasa pada selector state aktif                                                                                | Mencoba hasilnya di browser                                                                                          | Layout masih berubah, sehingga solusi tidak digunakan |
| Border tombol tab aktif — percobaan 2 | Gemini | Menjaga border agar tidak mengubah ukuran sidebar        | Menyarankan `box-sizing: border-box` dan border transparan sejak awal                                                               | Mencoba hasilnya di browser                                                                                          | Masih menghasilkan perubahan yang tidak diinginkan    |
| Border tombol tab aktif — percobaan 3 | Gemini | Mencari solusi yang tidak memengaruhi layout             | Menyarankan `box-shadow: inset`                                                                                                     | Menerapkan dan menyesuaikan warnanya menjadi `var(--accent)`                                                         | Digunakan pada CSS final                              |
| Ukuran gambar galeri — percobaan 1    | Gemini | Mengatur tinggi gambar galeri                            | Menyarankan `height: 220px` dan `width: auto`                                                                                       | Mengevaluasi kembali kebutuhan desain                                                                                | Tidak digunakan sebagai solusi final                  |
| Ukuran gambar galeri — percobaan 2    | Gemini | Menampilkan gambar secara utuh                           | Menyarankan `height: 280px`, `min-width: 200px`, background, border, dan flex centering                                             | Menghapus background dan border, mengganti `height` menjadi `max-height`, serta memindahkan flex centering ke parent | Versi final lebih sederhana                           |
| Infinite marquee                      | Gemini | Membuat loop marquee berjalan mulus                      | Menjelaskan bahwa kelompok duplikat harus memiliki jumlah item yang sama dengan kelompok awal ketika menggunakan `translateX(-50%)` | Menyesuaikan markup HTML dan menguji animasi                                                                         | Marquee dapat berulang tanpa lompatan yang terlihat   |
| Restrukturisasi Art Portfolio         | Gemini | Memperbaiki struktur HTML marquee                        | Memberikan contoh blok HTML yang telah diperbaiki                                                                                   | Mengadaptasi bagian yang diperlukan dan menghapus elemen yang tidak digunakan                                        | Struktur final disesuaikan dengan desain saya         |
| Git dan submission                    | Gemini | Memahami proses commit, push, dan mendapatkan URL commit | Memberikan langkah `git status`, `git add`, `git commit`, `git push`, dan cara mengambil URL commit                                 | Menjalankan proses Git dan memverifikasi hasil                                                                       | Digunakan untuk proses submission                     |

---

# Tugas 2

## Implementasi Model-View-Template (MVT)

Struktur data yang digunakan pada aplikasi main terdiri dari beberapa model, yaitu:

Education: menyimpan data pendidikan seperti institution, faculty, start_period, end_period, dan logo_url.
Experience: menyimpan data pengalaman seperti title, organization, description, category, is_ongoing, dan image_url.
Project: menyimpan data project seperti title, description, image_url, dan play_url.
ArtItem: menyimpan data art portfolio seperti title, category, dan image_url.

## Pertanyaan Reflektif

### 1. Alur request dari browser sampai halaman ditampilkan

Ketika pengguna membuka halaman portfolio, request dari browser pertama kali diproses oleh urls.py di level project (myportfolio/urls.py). Dari sana, request diteruskan ke main/urls.py menggunakan include().

Di main/urls.py, URL tersebut kemudian diarahkan ke function view yang sesuai di main/views.py. View mengambil data dari model menggunakan Django ORM, misalnya dengan Experience.objects.all() untuk mengambil seluruh data experience.

Data yang sudah diambil kemudian dimasukkan ke dalam context dan dikirim ke template menggunakan render(). Di dalam template seperti experience.html, data tersebut ditampilkan menggunakan Django Template Language, misalnya dengan {% for item in ... %} untuk melakukan perulangan pada setiap data.

Jika tidak ada data yang ditemukan, template juga memiliki {% empty %} untuk menampilkan kondisi ketika queryset kosong.

Setelah template selesai diproses oleh Django, hasilnya berupa HTML dikirim kembali ke browser dan ditampilkan sebagai halaman portfolio.

Secara sederhana, alurnya adalah:

Browser -> URL -> View -> Model/Database -> Template -> HTML -> Browser

Alur ini mengikuti konsep MVT yang digunakan pada bagian Experience di Tutorial 02.


### 2. Mengapa data disimpan di Model, bukan ditulis langsung di Template

Saya menyimpan data portfolio di Model/database supaya data dan tampilan tidak tercampur. Model digunakan untuk menyimpan datanya, sedangkan Template digunakan untuk mengatur bagaimana data tersebut ditampilkan.

Hal ini terasa ketika saya mengganti daftar project yang sebelumnya digunakan. Data project awal diganti menjadi project final seperti Save the Patient!, Road to the Cinema, Survi-vim, Wait, New Rule!, dan Brine & Blades.

Setelah menggunakan Model, perubahan tersebut bisa dilakukan dari data yang dimasukkan ke database tanpa perlu mengubah struktur HTML di template. Saya menggunakan fixture initial_data.json yang kemudian dimasukkan ke database menggunakan manage.py loaddata.

Kalau data masih ditulis langsung di HTML seperti pada Tugas 1, setiap kali ingin mengganti atau menambah project saya harus mengedit HTML secara manual. Selain lebih merepotkan, cara tersebut juga lebih berisiko membuat struktur HTML yang sudah dibuat menjadi berubah atau rusak.

Menurut saya, penggunaan Model juga membuat project lebih mudah dikembangkan. Misalnya, jika nantinya ingin menambahkan field baru atau membuat halaman detail untuk setiap project, perubahan tersebut bisa dilakukan pada Model dan View tanpa harus mengubah keseluruhan struktur Template.

### 3. Perbedaan `makemigrations` dan `migrate`

python manage.py makemigrations digunakan untuk membuat file migration berdasarkan perubahan yang dilakukan pada models.py. File tersebut berisi instruksi perubahan struktur database, misalnya ketika ada model atau field baru.

Perintah ini belum mengubah database secara langsung. Jadi, makemigrations bisa dibilang adalah tahap untuk membuat file yang berisi perubahan yang perlu dilakukan.

Setelah itu, python manage.py migrate digunakan untuk menerapkan migration tersebut ke database. Pada tahap ini, Django benar-benar melakukan perubahan pada database sesuai dengan file migration yang sudah dibuat.

Jadi:

makemigrations -> membuat file migration.
migrate -> menerapkan migration ke database.

Saya sempat mengalami masalah ketika struktur primary key pada model Experience berubah dari UUID menjadi BigAutoField. Migration sebelumnya sudah menggunakan UUID, sedangkan migration baru mencoba mengubahnya menjadi bigint. Akibatnya, saat menjalankan migrate, muncul error:

django.db.utils.ProgrammingError: cannot cast type uuid to bigint

Masalah tersebut terjadi karena data yang sudah ada di database menggunakan tipe UUID, sehingga PostgreSQL tidak bisa langsung mengubah nilainya menjadi bigint.

Untuk mengatasinya, saya melakukan reset pada tabel dan migration yang terkait dengan app main, kemudian membuat migration baru berdasarkan struktur Model yang sudah diperbaiki. Setelah itu saya menjalankan migrate kembali dan migration berhasil diterapkan.

Dari masalah ini, saya jadi lebih memahami bahwa file migration dan kondisi database harus tetap sesuai. Kalau struktur Model sudah berubah tetapi database masih menggunakan struktur lama yang tidak kompatibel, proses migration bisa menghasilkan error.

## Ringkasan AI Log
 
| Tahap | AI | Tujuan/Prompt | Bantuan AI | Tindakan Saya | Hasil |
|---|---|---|---|---|---|
| Debug shell | Gemini 3.1 Pro | Mengatasi `IndentationError` pada blok `with` di Python shell | Menjelaskan penyebab, menyarankan alternatif tanpa `with` | Menjalankan ulang perintah tanpa `with` | `cursor.execute` berhasil dijalankan |
| Migrasi database | Gemini 3.1 Pro | Mengatasi error `cannot cast type uuid to bigint` saat `migrate` | Mendiagnosis konflik tipe id UUID→bigint, memberi langkah drop table + reset migrasi | Drop tabel, hapus record migrasi, reset file migrasi lokal, migrate ulang | Migrasi berhasil (status OK) |
| Seeding data (percobaan 1) | Gemini 3.1 Pro | Mengisi data Education/Experience/Project/ArtItem via shell | Skrip Python multi-baris | Menyalin skrip ke shell | `SyntaxError` akibat copy-paste, tidak berhasil |
| Seeding data (percobaan 2) | Gemini 3.1 Pro | Memperbaiki `SyntaxError` | Menyarankan satu baris per `objects.create()` | Menyalin ulang skrip | Masih menemui kendala copy-paste |
| Seeding data (percobaan 3) | Gemini 3.1 Pro | Menjalankan skrip tanpa masalah interaktif | Menyarankan `manage.py shell -c '...'` | Menjalankan perintah tersebut | Masih ada kendala |
| Seeding data (fixture) | Gemini 3.1 Pro | Mengatasi kendala copy-paste skrip panjang | Menyusun fixture `initial_data.json` + `loaddata` | Membuat file, push ke GitHub, pull di PWS, `loaddata` | Membuat skrip yang bisa masukin datanya dari json gitu gatau |
| Fixture Art Portfolio | Gemini 3.1 Pro | Melengkapi fixture dengan data Art Portfolio | Memperluas `initial_data.json` dengan seluruh ArtItem | Mengganti isi file, `loaddata` ulang | Membuat fixture sesuai data |
| Favicon | Gemini 3.1 Pro | Mengganti favicon default PWS | Menjelaskan tag `<link rel="icon">` | Menambah file favicon, commit, push, hard refresh | Bisa |

---

# Tugas 3 — Form & Data Delivery

## Deskripsi

Bagian ini melanjutkan portofolio yang dibangun pada Tugas 1 (static site) dan Tugas 2 (MVT dengan model, view, dan template). Pada Tugas 3, fitur Form & Data Delivery diterapkan pada **tiga bagian**: **Experience**, **Project**, dan sebuah fitur baru berupa **Message/Contact Form**.

Fitur utama yang ditambahkan:

* Refactor seluruh template agar menggunakan `{% extends 'base.html' %}`, menghilangkan duplikasi header/nav/footer yang sebelumnya ditulis ulang di setiap halaman (*sebenarnya ini sudah lakukan di tugas 2 karena tidak tahu bahwa diminta untuk diimplementasikannya di tugas 3).
* `ModelForm` untuk `Experience` (`ExperienceForm`), `Project` (`ProjectForm`), dan `Message` (`MessageForm`) di `main/forms.py`.
* Create, update, dan delete data untuk `Experience` dan `Project` lewat form.
* Create dan delete data untuk `Message` (fitur kirim pesan/kontak), termasuk pengambilan data lewat JSON dan deserialisasi untuk ditampilkan ulang di halaman.
* Endpoint JSON untuk `Experience`, `Project`, dan `Message`.

## Fitur

* **Template inheritance** — `base.html` menjadi root template dengan `{% block title %}`, `{% block extra_head %}`, `{% block brand_name %}`, `{% block footer_name %}`, dan `{% block content %}`. Seluruh halaman (`index.html`, `experience.html`, `project.html`, `art.html`, `message_form.html`) meng-extend `base.html` ini.
* **CRUD Experience** — `show_experience` (read), `create_experience` (create), `update_experience` (update), `delete_experience` (delete), menggunakan `ExperienceForm` dengan widget `RadioSelect` untuk field `category` dan `CheckboxInput` untuk `is_ongoing`.
* **CRUD Project** — `show_project`, `create_project`, `update_project`, `delete_project`, menggunakan `ProjectForm`.
* **JSON Data Delivery** — `show_json_experiences` (`/experience/json/`) dan `show_json_projects` (`/projects/json/`) mengembalikan seluruh data lewat `django.core.serializers`.
* **Message/Contact Form** — `send_message` (create + tampilkan ulang lewat JSON+deserialize), `get_messages_json` (`/api/messages/`, mendukung filter `?sender=`), `delete_message` (delete via form POST + `{% csrf_token %}` dalam modal popover `message_delete_modal.html`).
* **Empty state** — pesan "Belum ada ... yang ditambahkan" muncul pada `experience.html`, `project.html`, dan "No message yet." pada `message_form.html` ketika data kosong.
* Bagian **Education** dan **Art Portfolio** tetap seperti Tugas 2 — masih read-only (belum ada form create/update/delete untuk kedua bagian ini pada tugas ini karena tidak dilihatnya urgensi menambahkan CRUD experience di kedua bagian ini).

Catatan jujur: `MessageForm` hanya memiliki 2 field selain `id`/`time_sent` (`sender`, `content`), sehingga persyaratan "minimal 3 field selain id dan timestamp" pada tugas ini dipenuhi lewat `ExperienceForm` (6 field: `title`, `organization`, `description`, `category`, `is_ongoing`, `image_url`) dan `ProjectForm` (4 field: `title`, `description`, `image_url`, `play_url`), bukan lewat `MessageForm`.

## Struktur/Implementasi

* **Model** (`main/models.py`) — `Experience`, `Education`, `Project`, `ArtItem` (dari Tugas 2), ditambah `Message` (baru di Tugas 3: `sender`, `content`, `time_sent`).
* **ModelForm** (`main/forms.py`) — `ExperienceForm`, `ProjectForm`, `MessageForm`, masing-masing menentukan `fields`, `labels`, dan `widgets` sesuai tipe data field pada model terkait.
* **Views** (`main/views.py`) — fungsi `show_*` untuk menampilkan data, `create_*`/`update_*`/`delete_*` untuk CRUD, `show_json_*`/`get_messages_json` untuk JSON delivery.
* **URLs** (`main/urls.py`) — setiap fungsi didaftarkan dengan `name` unik, misalnya `create_experience`, `update_project`, `show_json_experiences`.
* **Templates** — `base.html` sebagai root; `experience.html`, `project.html`, `art.html`, `message_form.html` meng-extend `base.html`; `message_delete_modal.html` sebagai partial yang di-`{% include %}` di dalam `message_form.html`.
* **Serialization/Deserialization** — `django.core.serializers.serialize("json", queryset)` dipakai di `show_json_experiences`, `show_json_projects`, dan `get_messages_json` untuk mengubah `QuerySet` menjadi JSON. Di `send_message`, JSON hasil `get_messages_json` di-deserialize kembali lewat `serializers.deserialize("json", ...)` untuk membangun `message_list` yang ditampilkan di template.

## Setup & Installation

1. Clone repository dan masuk ke folder proyek:

```bash
git clone <url-repository-anda>
cd myportfolio
```

2. Buat dan aktifkan virtual environment:

```bash
python -m venv env
env\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Opsional, hanya untuk mode produksi/PostgreSQL) buat file `.env` berisi `PRODUCTION=True` beserta `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`, `SCHEMA` sesuai yang dibaca `portfolio/settings.py`. Untuk pengembangan lokal, `PRODUCTION` default bernilai `False` sehingga otomatis memakai SQLite (`db.sqlite3`) tanpa perlu file `.env`.

5. Jalankan migration:

```bash
python manage.py migrate
```

6. Jalankan development server:

```bash
python manage.py runserver
```

7. Buka `http://127.0.0.1:8000/` pada browser.

Website juga dapat diakses melalui deployment berikut:

`https://yasmin52-myportfolio.pws.cs.ui.ac.id/`

## Cara Menggunakan Fitur

* **Experience** — buka `/experience/`, klik **"+ Tambah Experience Baru"** menuju `/experience/add/`, isi form (Role/Position, Organization, Description, Category via radio button, Ongoing via checkbox, Image URL), lalu submit. Klik **Edit** pada kartu untuk membuka `/experience/edit/<id>/`. Klik **"Yes, delete"** pada kartu untuk menghapus data lewat `/experience/delete/<id>/` (link dengan konfirmasi `confirm()` di browser).
* **Project** — alur yang sama pada `/projects/`, `/projects/add/`, `/projects/edit/<id>/`, `/projects/delete/<id>/`.
* **Data JSON** — akses langsung `/experience/json/` atau `/projects/json/` di browser untuk melihat data mentah dalam format JSON hasil `serializers.serialize`.
* **Message/Contact** — buka `/pesan/`, isi Nama dan Pesan, submit. Pesan tersimpan lalu langsung ditampilkan ulang di bawah form (daftar `message_list`, hasil round-trip JSON + deserialize). Klik tombol **Delete** pada tiap pesan untuk membuka modal konfirmasi popover, lalu submit form POST ke `/pesan/<id>/delete/`. Endpoint `/api/messages/` juga bisa diakses langsung, dan mendukung filter `?sender=nama` untuk menyaring pesan berdasarkan pengirim.

## Progress

### Tutorial 03

* Menambah form message anonymous yang bisa diisi semua orang

### Individual Assignment 3

* Membuat branch `feature/experiences-crud` untuk mengembangkan fitur Experience secara terpisah dari `main`.
* Menambahkan `ExperienceForm` (ModelForm) di `main/forms.py`, serta view `create_experience`, `update_experience`, `delete_experience`, dan `show_json_experiences` di `main/views.py`.
* Mendaftarkan seluruh URL baru tersebut di `main/urls.py`.
* Memperbarui `experience.html` agar menampilkan tombol "Tambah", "Edit", dan "Yes, delete" pada setiap kartu.
* Sempat mengalami masalah workflow Git — progres di branch `feature/projects-crud` belum ter-merge ke `main` sebelum membuat branch baru `feature/experiences-crud`, sehingga terlihat seperti "hilang". Masalah diselesaikan dengan meng-merge `feature/projects-crud` ke `main` terlebih dahulu, lalu membuat ulang branch `feature/experiences-crud` dari `main` yang sudah diperbarui.
* Menyesuaikan komponen UI form: `RadioSelect` untuk field `category`, `CheckboxInput` untuk field `is_ongoing`.
* Menemukan dan memperbaiki error `FieldError: Unknown field(s) (end_date, start_date) specified for Experience` yang muncul karena `ExperienceForm` sempat mendaftarkan field yang tidak ada di model `Experience` — diperbaiki dengan menyesuaikan `fields` di `ExperienceForm` menjadi `category`, `is_ongoing`, dan `image_url`.
* Menghapus baris kode yang tidak terpakai (`projects = Project.objects.all()`) di `show_project` setelah meninjau ulang gaya penulisan context dict.
* Menerapkan pola CRUD + ModelForm + JSON endpoint yang sama untuk `Project` (`ProjectForm`, `create_project`, `update_project`, `delete_project`, `show_json_projects`).
* Menambahkan model `Message` beserta `MessageForm`, view `send_message`, `get_messages_json` (dengan filter `?sender=`), dan `delete_message`, sebagai fitur form kontak tambahan yang juga mendemonstrasikan JSON delivery dan deserialization.
* Melakukan refactor seluruh template (`index.html`, `experience.html`, `project.html`, `art.html`, `message_form.html`) agar menggunakan `{% extends 'base.html' %}`, menghilangkan duplikasi header/nav/footer yang sebelumnya ada di setiap file.
* Melakukan commit dengan pesan Conventional Commits, misalnya `feat(experience): add Experience ModelForm, CRUD views, and JSON endpoint`, lalu `git push origin main`.

### Tugas 3

1. Saya menggunakan `ModelForm` (seperti `ExperienceForm`, `ProjectForm`, dan `MessageForm` di `main/forms.py`) alih-alih menulis form HTML manual karena `ModelForm` langsung menurunkan field form dari definisi `Model` yang bersangkutan lewat `class Meta: model = ...`. Artinya tipe data, panjang maksimum (`max_length`), pilihan (`choices`, seperti `CATEGORY_CHOICES` pada `Experience`), dan status wajib/opsional (`blank`) sudah otomatis konsisten antara database dan form dan saya tidak perlu menulis ulang validasi tersebut secara manual di HTML maupun di view. Django juga otomatis menjalankan validasi (`form.is_valid()`) sebelum data disimpan lewat `form.save()`, sehingga risiko data yang tidak sesuai tipe/skema masuk ke database jauh berkurang dibandingkan menulis HTML form manual lalu mem-parsing `request.POST` sendiri.

   Contoh konkret di project saya: pada `ExperienceForm`, field `category` otomatis menghasilkan pilihan sesuai `CATEGORY_CHOICES` di model (dirender sebagai `RadioSelect`), dan `is_ongoing` otomatis dikenali sebagai `BooleanField` (dirender sebagai `CheckboxInput`). Kalau saya menulis HTML manual, saya harus menulis ulang seluruh elemen tersebut secara manual dan menjaga sinkronisasinya setiap kali model berubah sebagaimana sempat terjadi saat saya salah mendaftarkan field `start_date`/`end_date` di `ExperienceForm` yang ternyata tidak ada di model `Experience` (lihat bagian AI Disclosure di bawah), Django langsung menolak dengan `FieldError` saat aplikasi dijalankan. Ini justru menunjukkan manfaat `ModelForm`: ketidaksesuaian antara form dan model terdeteksi otomatis di level Python, bukan baru ketahuan saat form disubmit oleh pengguna.

   Untuk `{% csrf_token %}`, tag ini wajib pada setiap `<form method="POST">` (dipakai pada form Experience/Project/Message di `message_form.html`, serta pada `message_delete_modal.html`) karena melindungi dari **Cross-Site Request Forgery (CSRF)**. CSRF adalah serangan di mana situs lain mencoba mengirim request (biasanya POST) atas nama pengguna yang sedang memiliki sesi aktif di situs saya, tanpa sepengetahuan pengguna tersebut. Request POST berisiko karena POST digunakan untuk mengubah data (create/update/delete), berbeda dari GET yang seharusnya hanya membaca data. `{% csrf_token %}` menyisipkan token unik per sesi sebagai hidden input; saat form disubmit, `CsrfViewMiddleware` (terdaftar di `MIDDLEWARE` pada `settings.py`) memeriksa apakah token yang dikirim cocok dengan yang diharapkan, dan menolak request jika tidak cocok.

   Sebagai catatan: pada implementasi saat ini, `delete_experience` dan `delete_project` masih dipicu lewat tautan `<a href="...">` (GET request) dengan `confirm()` JavaScript, bukan form POST, berbeda dengan `delete_message` yang sudah memakai form POST + `{% csrf_token %}` lewat `message_delete_modal.html`. Ini adalah area yang idealnya saya samakan ke depannya agar seluruh operasi hapus data terlindungi CSRF secara konsisten.

2. JSON lebih disukai dibandingkan XML dalam pengembangan aplikasi web modern karena beberapa alasan konkret:

   * **Struktur & pemetaan langsung ke bahasa pemrograman.** Struktur JSON (objek `{}` dan array `[]`) memetakan langsung ke struktur data native di JavaScript (object literal, array) maupun Python (`dict`, `list`), tanpa konversi tambahan. XML tidak punya konsep array bawaan — daftar item direpresentasikan lewat elemen yang diulang, yang lebih ambigu untuk diparsing otomatis.
   * **Overhead sintaks.** XML membutuhkan tag pembuka dan penutup untuk setiap elemen, sedangkan JSON hanya membutuhkan `"key": value`. Untuk data berulang seperti daftar `Experience`/`Project` di project saya, ini membuat payload JSON jauh lebih ringkas dibanding XML untuk data yang sama.
   * **Parsing native di JavaScript.** Browser modern menyediakan `JSON.parse()`/`JSON.stringify()` secara bawaan, sedangkan parsing XML di client membutuhkan `DOMParser` atau library tambahan yang lebih verbose.
   * **Kompatibilitas dengan ekosistem API modern.** Django menyediakan `django.core.serializers` yang langsung mendukung `serializers.serialize("json", ...)`, dan hampir seluruh REST API modern (termasuk endpoint `show_json_experiences`, `show_json_projects`, dan `get_messages_json` pada project saya) menggunakan JSON sebagai format default.
   * **Readability.** JSON lebih ringkas dan mudah dibaca manusia untuk struktur data bertingkat sederhana dibandingkan XML yang lebih verbose untuk struktur yang sama.

   Meski begitu, JSON juga punya keterbatasan dibanding XML pada kasus tertentu: JSON tidak mendukung komentar di dalam datanya dan tidak memiliki mekanisme validasi skema resmi sekuat XML Schema (XSD)/DTD
   
   JSON juga kurang cocok untuk dokumen dengan campuran teks dan markup, sedangkan XML cocok untuk penggunaan itu. Untuk kebutuhan project saya yang hanya butuh mengirim data terstruktur sederhana seperti daftar `Experience`/`Project`/`Message`, JSON lebih sesuai karena datanya seragam dan tidak membutuhkan validasi skema yang ketat.

3. Alur yang terjadi ketika view saya (misalnya `show_json_experiences` atau `show_json_projects`) mengembalikan data dalam format JSON adalah:

   1. **Model/Database** — Data tersimpan di tabel `Experience`/`Project` pada database (SQLite untuk development, sesuai `portfolio/settings.py`).
   2. **Queryset/Object** — View memanggil `Experience.objects.all()` atau `Project.objects.all()`, yang mengembalikan `QuerySet` berisi instance `Model` Python — bukan struktur data JSON.
   3. **Serialization** — `QuerySet` tersebut diserialisasi lewat `serializers.serialize("json", data)`. Proses ini diperlukan karena instance `Model` Django adalah objek Python biasa (punya method, tipe field seperti `URLField`/`BooleanField`) yang tidak bisa langsung diubah menjadi teks JSON. JSON hanya mengenal tipe data primitif (string, number, boolean, array, object, null), sehingga field dan struktur objek Django harus diterjemahkan dulu ke representasi yang sesuai standar JSON.
   4. **JSON-compatible representation** — Hasil `serializers.serialize()` adalah string berformat JSON berisi field tiap objek (`pk`, `model`, `fields: {...}`).
   5. **HttpResponse** — String JSON dibungkus dengan `HttpResponse(..., content_type="application/json")` agar client tahu isi response berupa JSON, bukan HTML biasa.
   6. **HTTP response → client/browser** — Response dikirim melalui HTTP ke pihak yang mengakses endpoint (misalnya browser yang membuka `/experience/json/` secara langsung).

   Pada fitur pesan (`Message`), alurnya sedikit berbeda dan melibatkan **deserialization di sisi server**, bukan di client: di dalam view `send_message`, saya memanggil `get_messages_json(request)` untuk mendapatkan `HttpResponse` berisi JSON, lalu memanggil `serializers.deserialize("json", json_response.content.decode("utf-8"))` untuk mengubah JSON tersebut kembali menjadi objek Python (`DeserializedObject`), mengambil `.object` dari masing-masing hasilnya menjadi `message_list`, lalu mengirim `message_list` ke template `message_form.html` untuk ditampilkan. Ini bukan alur yang umum (biasanya deserialization terjadi di sisi client lewat `JSON.parse()` setelah `fetch`), tetapi ini adalah alur aktual yang saya implementasikan: menggunakan endpoint JSON yang sama secara internal untuk menampilkan ulang data pesan di halaman HTML.

   Serialization pada dasarnya diperlukan karena ada dua "dunia" data yang berbeda: dunia objek Python/Django di server, dan dunia teks/JSON yang bisa dikirim lewat HTTP dan dipahami sistem lain (browser, aplikasi lain, dsb). Tanpa serialization, instance `Model` Django tidak bisa dikirim langsung sebagai response HTTP.

## AI Disclosure

### AI Tools Used

| Tool | Tujuan Penggunaan | Jenis Bantuan |
|---|---|---|
| **Google Gemini** | Membangun fitur CRUD & JSON untuk `Experience`, debugging error Django, troubleshooting Git branch/merge, rekomendasi komponen UI form, konvensi commit message | Code generation, debugging, penjelasan konsep, saran best-practice |
| **Claude (Anthropic)** | Audit struktur proyek Tugas 2 terhadap requirement (model, view, template, tes, migration), saran refactor `base.html`, penyusunan draf README Tugas 3 ini (deskripsi, fitur, setup, progress, dan bagian AI disclosure ini sendiri) | Code review/audit, saran refactor, drafting dokumentasi |

### AI Usage & Prompting Strategy

Google Gemini digunakan secara bertahap mengikuti alur pengembangan fitur: meminta kerangka kode (model, form, view, url, template) untuk `Experience`, lalu menempelkan traceback error secara langsung ketika terjadi `FieldError` untuk didiagnosis, menanyakan perbandingan gaya penulisan kode untuk mendapatkan masukan best-practice, dan menanyakan konvensi commit message. Percakapan lengkap dapat dilihat pada log:

`https://share.gemini.google/KLI2UyPFyPHp`

Claude digunakan dengan strategi berbeda: bukan untuk generate fitur baru dari nol, melainkan untuk **meninjau kode yang sudah ada** (memberikan `models.py`, `views.py`, `forms.py`, `urls.py`, template, dan hasil migrasi) dan meminta audit kepatuhan terhadap requirement tugas, identifikasi bug/duplikasi kode, serta penyusunan dokumentasi.

### Parts Assisted by AI

| Bagian | AI digunakan untuk | Peran AI | Verifikasi/Perbaikan Manual |
|---|---|---|---|
| Experience CRUD (model/form/view/url/template) | Membuat kerangka `ModelForm`, view CRUD, routing, dan template untuk fitur Experience | AI-generated suggestion (Gemini) | Menjalankan `runserver`, mengetes create/edit/delete, memperbaiki `FieldError` akibat field `start_date`/`end_date` yang tidak sesuai model, menyesuaikan `fields` di `ExperienceForm` menjadi `category`, `is_ongoing`, `image_url` |
| Pemilihan widget form (`category`, `is_ongoing`) | Meminta rekomendasi UI (radio button/dropdown/checkbox) | AI explanation + suggestion (Gemini) | Menerapkan `RadioSelect` untuk `category` dan `CheckboxInput` untuk `is_ongoing`, disesuaikan dengan field final di model |
| Debugging Git branch/merge | Menjelaskan penyebab progress "hilang" akibat branch belum di-merge | AI explanation (Gemini) | Menjalankan `git branch`, `git merge feature/projects-crud`, membuat ulang branch `feature/experiences-crud` dari `main` yang sudah diperbarui |
| Konsistensi context dict di views | Membandingkan dua gaya penulisan context (`show_experience` vs `show_project`) dan mendeteksi dead code | AI-assisted review (Gemini) | Menghapus variabel `projects = Project.objects.all()` yang tidak terpakai di `show_project` |
| Konvensi commit message | Menyarankan pesan Conventional Commits untuk fitur Experience | AI suggestion (Gemini) | Menjalankan `git commit -m "feat(experience): ..."` |
| Refactor `base.html` (template inheritance) | Audit struktur proyek Tugas 2 dan menyarankan ekstraksi header/nav/footer ke `base.html` dengan `{% block %}` | AI-generated suggestion (Claude) | Mengadaptasi `base.html` ke dalam proyek; menyesuaikan seluruh template (`index.html`, `experience.html`, `project.html`, `art.html`, `message_form.html`) agar menggunakan `{% extends 'base.html' %}` |
| Draf dokumentasi README Tugas 3 | Menyusun struktur README, jawaban pertanyaan reflektif, dan bagian AI disclosure ini berdasarkan kode dan log yang sudah ada | AI-assisted documentation (Claude) | Meninjau ulang draf agar sesuai implementasi aktual sebelum disimpan ke repository |

### Critical Reflection on AI Limitations

* **Gemini sempat mengasumsikan struktur model yang salah.** Pada awal pengembangan `ExperienceForm`, Gemini menyarankan field `start_date` dan `end_date` yang ternyata tidak ada pada model `Experience` yang sudah saya definisikan sebelumnya (yang memakai `category` dan `is_ongoing`). Ini menyebabkan `FieldError` nyata saat `runserver` dijalankan — bukti bahwa AI dapat memberikan kode yang secara sintaks benar tetapi tidak cocok dengan struktur project yang sebenarnya, terutama jika konteks model belum sepenuhnya diberikan dalam percakapan.
* **Claude hanya dapat mengaudit berdasarkan file yang benar-benar dibagikan.** Saat pertama meminta audit Tugas 2, saya belum melampirkan `models.py`, `views.py`, dan migration, sehingga sebagian besar item checklist ditandai "cannot determine" alih-alih diverifikasi. Ini menunjukkan bahwa kualitas audit AI dibatasi oleh konteks yang diberikan, bukan oleh kondisi kode yang sebenarnya.
* **AI tidak menggantikan pengujian langsung.** Baik Gemini maupun Claude tidak benar-benar menjalankan kode saya — semua perbaikan (misalnya perbaikan `FieldError`, hasil merge branch, atau kebenaran refactor `base.html`) tetap perlu saya verifikasi sendiri lewat `runserver`, browser, dan `git log`.

### Manual Improvements & Verification

* Memperbaiki `ExperienceForm.Meta.fields` agar sesuai model asli (`category`, `is_ongoing`, `image_url`), bukan `start_date`/`end_date` yang disarankan AI di awal.
* Menghapus baris `projects = Project.objects.all()` yang tidak terpakai di `show_project` setelah tinjauan gaya kode.
* Menyelesaikan masalah branch/merge secara manual: `git branch`, `git merge feature/projects-crud`, membuat ulang `feature/experiences-crud` dari `main` yang sudah diperbarui.
* Mengadaptasi `base.html` hasil audit Claude ke dalam proyek nyata, lalu mengubah `index.html`, `experience.html`, `project.html`, `art.html`, dan `message_form.html` menjadi `{% extends 'base.html' %}`.
* Menjalankan `python manage.py runserver` dan menguji create/edit/delete untuk Experience dan Project, serta endpoint `/experience/json/` dan `/projects/json/` secara langsung di browser.

### AI Prompting Log

| Tahap | Tujuan | AI Tool | Ringkasan Prompt | Hasil & Tindakan Manual |
|---|---|---|---|---|
| 1 | Membangun fitur CRUD & JSON Experience di branch baru | Gemini | "Lanjut bikin fitur CRUD & JSON untuk Experience di branch feature/experiences-crud" | Mendapat kerangka model/form/view/url/template; diadaptasi & diuji |
| 2 | Debugging branch/merge | Gemini | "eh kok progress ku kayak hilang gitu ya" + output `git branch` | Memahami penyebab (branch belum di-merge), menjalankan merge & membuat ulang branch |
| 3 | Menentukan komponen UI form | Gemini | Menanyakan radio button vs dropdown untuk `category`, dan radio vs checkbox untuk `is_ongoing` | Menerapkan `RadioSelect` dan `CheckboxInput` sesuai rekomendasi |
| 4 | Review code style | Gemini | Membandingkan dua gaya penulisan context dict di `show_experience` vs `show_project` | Menghapus dead code di `show_project` |
| 5 | Penempatan tombol Tambah/Edit/Hapus di template | Gemini | Menanyakan posisi tombol yang tepat pada `experience.html` | Menata tombol create di luar loop, tombol edit/delete di dalam setiap card |
| 6 | Debugging error saat `runserver` | Gemini | Menempelkan traceback `FieldError: Unknown field(s) (end_date, start_date)` | Memperbaiki `ExperienceForm.Meta.fields` agar sesuai model asli |
| 7 | Commit message | Gemini | "commit message nya apa ya" | Menjalankan `git commit -m "feat(experience): ..."` |
| 8 | Push ke Git | Gemini | "cara masukin semua progress tadi ke git" | Menjalankan `git add`, `git commit`, `git checkout main`, `git merge`, `git push` |

## AI Disclosure — Individual Assignment 4

### AI Tools Used

| Tool | Tujuan Penggunaan | Jenis Bantuan |
| --- | --- | --- |
| **Gemini Pro 3.1** | Grup Editor lewat migration, kebocoran username di JSON, tombol Edit untuk Editor di halaman Project, `delete_message`, star hanya lewat POST, redirect `next` setelah login, dan commit message | Code generation, explanation, debugging ringan |

### AI Usage & Prompting Strategy

Di beberapa prompt pertama, poin audit langsung diberikan ke Gemini Pro 3.1 apa adanya (misalnya "Editor group doesn't exist. Why: ... PASS: ...") tanpa melampirkan kode saya. Akibatnya jawaban yang keluar generik dan memakai nama fungsi/URL yang tidak sama dengan proyek saya (lihat bagian keterbatasan). Baru setelah itu saya menempelkan fungsi aslinya (`show_json_experiences`) dan jawabannya menjadi lebih sesuai. Untuk mengecek hasilnya, saya menjalankan `python manage.py runserver` lalu memanggil `/experience/json/` dengan `curl` dan menempelkan outputnya kembali ke AI.

### Parts Assisted by AI

| Bagian TI4 | AI Tool | Bentuk Bantuan | Kontribusi Manual Saya |
| --- | --- | --- | --- |
| Grup Editor otomatis dibuat | Gemini Pro | data migration `RunPython` dengan `get_or_create` | Membuat file data migration (misal `0003_auto_add_editor_group.py`), menjalankan `migrate`, dan memastikan grup muncul di Django Admin. |
| Kebocoran username di JSON | Gemini Pro | Contoh `JsonResponse` yang mengirim jumlah star dan status "sudah di-star" | Menempelkan fungsi asli agar jawaban sesuai; menambahkan kembali field IA3 yang hilang dari dictionary; memastikan URL `/projects/json/` dan `/experience/json/` tidak membocorkan ID atau username. |
| Tombol Edit Editor di Project | Gemini Pro | Contoh view + template dengan `is_admin or is_editor` | Menyesuaikan nama variabel context (`project_list` / `experience_list`) dan memperbaiki penamaan CSS class menjadi `btn-action btn-edit` agar sejajar dengan tombol delete. |
| Restriksi `delete_message`, star hanya POST, redirect `next` | Gemini Pro | Contoh decorator dan template | Mengganti redirect login dari AI menjadi response `403 Forbidden` (`PermissionDenied`) sesuai spesifikasi tugas; memastikan tag `<form>` dipakai untuk star. |
| Commit message | Gemini Pro | Menyusun pesan commit | Memodifikasi pesan commit AI agar lebih akurat merepresentasikan perbaikan database PWS dan UUID yang memakan banyak waktu. |

Bagian lain di TI4 (register/login/logout, cookie `last_login`, pengecekan role di view, model/migrasi/view star) saya kerjakan dengan mengikuti **Tutorial 04**, dikembangkan dari Tugas 3 saya, dan dibantu AI saat terjadi *error* (seperti `NoReverseMatch` dan masalah *database schema* di PWS).

### Critical Reflection on AI Limitations

Contoh-contoh ini saya temukan saat membandingkan saran AI dengan kode proyek saya:

* **Kode generik yang tidak cocok dengan proyek.** Karena kode belum saya lampirkan, saran AI memakai nama yang tidak ada di proyek saya: fungsi `get_experience_json` (yang ada `show_json_experiences`), context `projects` (yang ada `project_list`), URL `add_project`/`edit_project` tanpa namespace (yang ada `main:create_project`/`main:update_project`), `delete_message(request, id)` (URL saya memakai `message_id`), `redirect('message_list')` dan `redirect('home')` (yang ada `main:send_message` dan `main:show_main`), serta modal Bootstrap `data-bs-toggle` padahal modal saya memakai atribut `popover` bawaan HTML. Kalau ditempel langsung, kode ini akan error. Saya secara manual menyesuaikan seluruh tag `{% url %}`, variabel dalam *loop* (mengganti `exp` menjadi `experience`), dan memastikan modal memakai atribut HTML native bawaan proyek saya.
* **Asumsi field yang tidak ada.** Salah satu opsi JSON memakai field `date_created`, padahal model `Experience` saya tidak punya field itu.
* **Saran yang bertentangan dengan requirement.** `user_passes_test` untuk `delete_message` mengalihkan user yang tidak berhak ke halaman login, padahal spesifikasi minta 403 untuk user yang sudah login. Dan `LOGIN_URL` di settings saya tidak diatur. Saran redirect `next` tidak memvalidasi URL (risiko open redirect).
* **AI tidak tahu keadaan database dan riwayat migrasi saya.** Saran `migrate --fake` untuk PostgreSQL PWS cukup berisiko, karena menandai migrasi sebagai sudah dijalankan tanpa benar-benar membuat tabel. Saya akhirnya menggunakan `manage.py shell` dengan `connection.cursor()` untuk melakukan `DROP TABLE` secara aman dan mengulang migrasi dari nol di PWS.
* **Commit message tanpa melihat perubahan.** Pesan commit dari AI hanya menyebut 4 hal keamanan, padahal perbaikan saya melibatkan perombakan tipe data UUID dan integer yang sangat memakan waktu.

Dari sini saya belajar bahwa AI memberi hasil yang jauh lebih cocok kalau saya melampirkan kode dan requirement, dan bahwa jawabannya tetap harus dibandingkan dengan spesifikasi tugas (403 vs redirect, POST vs GET).

### Manual Improvements & Verification

| Saran AI | Masalah / Pertimbangan | Perubahan Manual Saya | Hasil Akhir |
| --- | --- | --- | --- |
| Contoh JSON generik + kode JS frontend | Nama fungsi tidak cocok, dan proyek tidak memakai JS untuk star | Menempelkan fungsi asli lalu memakai versi `JsonResponse` (Opsi 1 dari AI) dan menyesuaikan field manual. | `starred_by` hilang dari `/experience/json/` dan `/projects/json/`. Data aman. |
| `is_admin or is_editor` di template Project | Nama URL dan variabel context tidak sesuai proyek | Memperbaiki variabel dari `projects` ke `project_list`. Memperbaiki `exp` menjadi `experience` di file HTML. Menambah class `btn-action btn-edit` agar UI rapi. | Tombol Edit muncul eksklusif untuk Admin dan Editor tanpa merusak layout CSS. |
| `user_passes_test` untuk `delete_message` | Redirect ke login, bukan 403 Forbidden | Mengganti *decorator* dengan *server-side check* manual: `if not request.user.is_superuser: raise PermissionDenied`. | Menghasilkan error 403 jika diakses secara paksa oleh user non-admin. |
| Redirect `next` tanpa validasi | Risiko open redirect | Memastikan validasi URL menggunakan `url_has_allowed_host_and_scheme` dari modul utilitas Django sebelum melakukan redirect. | Redirect setelah login aman. |
| `migrate --fake` untuk produksi | Tidak sesuai kondisi database saya, tabel fisik PostgreSQL belum ada | Membuka shell di PWS, mengeksekusi sintaks `DROP TABLE IF EXISTS ... CASCADE;` lalu `migrate` ulang dan `loaddata`. | Database produksi PWS tersinkronisasi bersih tanpa konflik UUID/Integer. |

**Yang sudah saya verifikasi sendiri:**

* Menjalankan `python manage.py runserver`. Percobaan `curl` pertama gagal karena server belum menyala; setelah server dijalankan, `curl http://localhost:8000/experience/json/` mengembalikan status 200 tanpa daftar username.
* Melakukan login/logout dan memeriksa cookie `last_login` berhasil ter-set.
* Mengakses sebagai *anonymous*, normal user, Editor, dan superuser ke URL *create*, *update*, dan *delete* secara manual melalui *address bar*; memastikan yang tak berhak mendapat 403 Forbidden atau redirect ke login.
* Memastikan toggle star berfungsi, menolak request dengan method GET, dan meredirect kembali ke halaman asal.
* Mengeksekusi `python manage.py migrate` di database lokal (SQLite) maupun di PWS (PostgreSQL) setelah masalah tipe data UUID terselesaikan.
* Menambahkan akun user biasa ke dalam grup `Editor` lewat Django Admin dan memvalidasi tombol Edit muncul untuk user tersebut.

### AI Prompting Log

| No. | Prompt / Masalah | Solusi dari AI (Gemini Pro) | Keterangan / Tindakan Saya |
| --- | --- | --- | --- |
| 1 | Mengubah tipe data menjadi UUID namun muncul error `NoReverseMatch`. | Menyarankan ubah `<int:id>` ke `<uuid:id>` di `urls.py`, hapus `db.sqlite3` lokal, dan ulang migrasi. | Diterapkan di *local development*. Error URL teratasi. |
| 2 | Tampilan admin hancur/overflow karena tombol bertambah banyak. | Menyarankan tambah properti CSS `flex-wrap: wrap;` pada `card-actions`. | Diterapkan, tampilan UI tombol menjadi *hugged* ke bawah. |
| 3 | `NoReverseMatch` untuk URL `show_projects` saat mencoba memberi star. | Mengingatkan bahwa nama URL saya bentuk tunggal (`show_project`). | Diperbaiki manual di `views.py`. |
| 4 | JSON membocorkan angka ID (user yang memberi star). | Menyuruh menambahkan argumen `use_natural_foreign_keys=True` pada `serializers.serialize()`. | Diterapkan, JSON menampilkan username. (Nanti diubah lagi karena username juga tidak boleh bocor publik). |
| 5 | Minta step-by-step pengerjaan TI4. | Memberi panduan panjang (buat Grup Editor, tambah field relasi star, restrict create/delete, buat toggle star POST). | Dijadikan acuan utama pengerjaan TI4. |
| 6 | Error `NoReverseMatch` dengan argumen `('',)` di halaman experience. | Menyadari ada variabel *looping* yang dipanggil salah (`exp` padahal dideklarasikan `experience`). | Disesuaikan agar semua memakai variabel `experience`. |
| 7 | Tampilan UI tombol Edit berbeda dengan tombol Delete. | Menyuruh menambahkan class `btn-action` berdampingan dengan `btn-edit`. | Diterapkan agar desain seragam (bentuk pil). |
| 8 | Bentrok *primary key* saat `loaddata` di PWS. PostgreSQL menolak UUID masuk ke integer. | Menyarankan hapus skema tabel paksa lewat Django Shell (`DROP TABLE`), hapus `django_migrations`, dan ulangi migrasi dari awal. | Panduan ini sangat krusial dan menyelesaikan isu deployment di PWS. |
| 9 | Mem-paste kriteria lulus (PASS) dari asisten dosen (Group, Leak, UI Editor, Delete auth, dll). | AI memberi contoh kode penambalan keamanan (JsonResponse tanpa array username, decorator check, next redirect). | Banyak *adjustment* manual karena AI menebak nama variabel/fungsi yang tidak sesuai dengan struktur proyek saya. |


---

# Tugas 5 — Web Interactivity with JavaScript

## Deskripsi

Tugas 5 melanjutkan pengembangan website portofolio dari Tugas 3 (Form & Data Delivery) dan Tugas 4 (Authentication, Session, Cookies, serta role/permission). Pada tahap ini, interaktivitas berbasis JavaScript diterapkan pada bagian portfolio yang dikerjakan sebelumnya dengan pola yang dipelajari pada Tutorial 05.

Implementasi menggunakan AJAX dan Fetch API sehingga data dapat dimuat dan diperbarui secara asynchronous tanpa melakukan reload halaman. Fitur yang diterapkan mencakup pemuatan data melalui endpoint JSON, pencarian dengan debouncing, penambahan data melalui modal dan AJAX, notifikasi toast, serta perlindungan terhadap XSS.

### Fitur yang Diimplementasikan

* **AJAX data loading** — halaman daftar hanya menyediakan kerangka halaman pada initial render, sedangkan data diambil dari endpoint JSON menggunakan `fetch()`.
* **Manual `JsonResponse`** — endpoint mengembalikan data yang memang diperlukan frontend, termasuk jumlah star dan status star pengguna yang sedang login.
* **Loading, empty, dan error state** — pengguna mendapatkan feedback yang jelas ketika data sedang dimuat, ketika tidak ada hasil, maupun ketika request gagal.
* **AJAX search** — pencarian dilakukan melalui endpoint JSON tanpa reload halaman.
* **Search debouncing** — request pencarian tidak dikirim pada setiap karakter, melainkan setelah pengguna berhenti mengetik selama jeda tertentu.
* **Modal form** — penambahan data dilakukan melalui form di dalam modal pada halaman daftar.
* **AJAX POST** — form dikirim menggunakan Fetch API dengan validasi `ModelForm`.
* **HTTP status yang sesuai** — response membedakan kondisi berhasil (`201`), validation error (`400`), dan akses ditolak (`403`).
* **Server-side permission check** — hak akses tetap diverifikasi di view sehingga menyembunyikan tombol pada template bukan satu-satunya lapisan keamanan.
* **CSRF protection** — request POST AJAX menyertakan token CSRF.
* **No-reload update** — daftar diperbarui setelah data berhasil ditambahkan tanpa memuat ulang seluruh halaman.
* **Toast notification** — keberhasilan, validation error, permission error, dan kegagalan request ditampilkan melalui toast.
* **XSS protection** — data yang berasal dari server di-escape sebelum dimasukkan ke DOM melalui JavaScript.
* **Server-side sanitization** — field teks pada `ModelForm` dibersihkan menggunakan `strip_tags` melalui method `clean_<field>`.
* **Graceful error recovery** — kegagalan pemuatan data memberikan feedback yang jelas dan memungkinkan pengguna mencoba kembali.

## Alur Interaktivitas

Secara umum, alur halaman daftar adalah:

```text
Browser membuka halaman
        |
        v
Template merender struktur halaman
        |
        v
JavaScript menjalankan fetch()
        |
        v
Django JSON endpoint
        |
        v
Query Model / Database
        |
        v
JsonResponse
        |
        v
JavaScript menerima JSON
        |
        v
Render data secara aman ke DOM
```

Untuk penambahan data:

```text
User mengisi form modal
        |
        v
JavaScript intercept submit
        |
        v
Fetch POST + CSRF token
        |
        v
Django permission check
        |
        v
ModelForm validation
        |
   +----+----+
   |         |
 valid     invalid
   |         |
  201       400
   |         |
   +----+----+
        |
        v
JSON response
        |
        v
Toast + refresh data dengan AJAX
        |
        v
Modal ditutup tanpa page reload
```

---

## Pertanyaan Reflektif

### Tugas 5

### 1. Jelaskan apa itu *debouncing* dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!

*Debouncing* adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan suatu aktivitas selama interval waktu tertentu. Pada fitur pencarian, aktivitas tersebut biasanya berupa event `input`, yaitu ketika pengguna mengetik di kotak pencarian.

Tanpa debouncing, jika fungsi pencarian langsung menjalankan `fetch()` setiap kali event `input` terjadi, setiap karakter yang diketik akan menghasilkan satu request. Misalnya, ketika pengguna mengetik `Django`, browser dapat mengirim request untuk `D`, `Dj`, `Dja`, `Djan`, `Djang`, dan `Django`. Jika pengguna mengetik dengan cepat, beberapa request dapat dikirim dalam waktu yang sangat berdekatan.

Dengan debouncing, setiap input baru membatalkan timer sebelumnya. Request hanya dikirim setelah pengguna berhenti mengetik selama interval tertentu, misalnya 300 milidetik. Secara sederhana, mekanismenya adalah:

```javascript
let debounceTimer;

searchInput.addEventListener("input", () => {
    clearTimeout(debounceTimer);

    debounceTimer = setTimeout(() => {
        fetchData(searchInput.value);
    }, 300);
});
```

Jika pengguna terus mengetik sebelum 300 milidetik selesai, `clearTimeout()` membatalkan timer sebelumnya dan membuat timer baru. Akibatnya, request baru hanya dilakukan ketika pengguna benar-benar berhenti mengetik.

Debouncing penting pada pencarian berbasis AJAX karena dapat mengurangi jumlah request yang dikirim ke server. Hal ini mengurangi beban server dan database, mengurangi lalu lintas jaringan, serta membuat aplikasi lebih efisien. Dari sisi pengguna, pencarian juga terasa lebih stabil karena browser tidak harus memproses response dari terlalu banyak request yang sebenarnya tidak diperlukan.

Debouncing juga berbeda dengan throttling. Debouncing menunggu sampai aktivitas berhenti sebelum menjalankan fungsi, sedangkan throttling membatasi fungsi agar hanya dapat dijalankan paling banyak sekali dalam interval tertentu. Untuk search-as-you-type, debouncing lebih sesuai karena saya biasanya ingin mencari berdasarkan query yang sudah selesai diketik, bukan berdasarkan setiap bagian query.

Dalam implementasi Tugas 5, debouncing digunakan pada event pencarian sehingga AJAX request dikirim setelah pengguna berhenti mengetik, bukan untuk setiap karakter.

### 2. Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`! Apa yang akan terjadi jika kita tidak menggunakan `await`?

`fetch()` merupakan fungsi asynchronous yang mengembalikan sebuah `Promise`. Promise tersebut merepresentasikan hasil dari operasi HTTP yang belum tentu selesai ketika baris kode tersebut dijalankan.

`await` digunakan di dalam fungsi `async` untuk menunggu Promise tersebut selesai sebelum melanjutkan ke baris berikutnya.

Contohnya:

```javascript
const response = await fetch(url);
const data = await response.json();
```

Pada baris pertama, JavaScript menunggu sampai request `fetch()` menghasilkan response. Setelah response tersedia, nilai tersebut disimpan ke dalam `response`. Kemudian `await response.json()` menunggu proses membaca body response dan mengubahnya menjadi object JavaScript.

`await` tidak berarti seluruh browser berhenti bekerja. Karena `fetch()` menggunakan Promise dan JavaScript berjalan dengan mekanisme asynchronous/event loop, browser tetap dapat menangani pekerjaan lain. Yang ditunda adalah kelanjutan fungsi asynchronous tersebut sampai Promise selesai.

Jika `await` tidak digunakan, nilai yang diperoleh dari `fetch()` bukan response langsung, melainkan sebuah `Promise`. Contohnya:

```javascript
const response = fetch(url);
console.log(response);
```

`response` pada contoh tersebut masih berupa Promise sehingga kita belum dapat langsung menggunakan:

```javascript
response.json();
```

untuk memperoleh data JSON. Kode akan salah karena method `json()` dimiliki oleh `Response`, bukan oleh Promise.

Alternatif tanpa `await` adalah menggunakan `.then()`:

```javascript
fetch(url)
    .then(response => response.json())
    .then(data => {
        // menggunakan data
    });
```

Jadi `await` bukan satu-satunya cara untuk menangani `fetch()`, tetapi membuat alur asynchronous terlihat lebih seperti kode sinkron sehingga lebih mudah dibaca. Dalam Tugas 5, `await` digunakan agar proses pengambilan response, pembacaan JSON, dan penanganan hasil dapat dilakukan secara berurutan dan mudah dipahami.

Perlu diperhatikan juga bahwa `await fetch()` tidak otomatis menganggap HTTP 400 atau 500 sebagai JavaScript exception. Karena itu, response tetap perlu diperiksa menggunakan `response.ok` atau `response.status`. Inilah alasan error handling pada AJAX perlu membedakan antara network error dan HTTP error dari server.

### 3. Jelaskan apa itu serangan XSS (*Cross-Site Scripting*) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui *template* Django!

XSS (*Cross-Site Scripting*) adalah serangan ketika penyerang berhasil memasukkan konten yang dianggap sebagai HTML atau JavaScript ke halaman web sehingga browser korban mengeksekusinya sebagai kode, bukan sekadar menampilkannya sebagai data.

Contoh payload sederhana adalah:

```html
<img src="x" onerror="alert('XSS!')">
```

Jika nilai tersebut dimasukkan ke halaman menggunakan `innerHTML` tanpa escaping, browser dapat memperlakukannya sebagai elemen HTML dan event handler `onerror` dapat dijalankan.

Pada template Django, output variabel secara default menggunakan HTML escaping ketika ditampilkan melalui template syntax biasa seperti:

```django
<h3>{{ project.title }}</h3>
```

Karakter khusus seperti `<`, `>`, `&`, dan tanda kutip akan diubah menjadi representasi HTML yang aman. Karena itu, string seperti `<img ...>` biasanya ditampilkan sebagai teks, bukan dibuat menjadi elemen HTML aktif.

Namun, ketika data JSON dari AJAX diterima oleh JavaScript, Django tidak lagi berada di tahap yang langsung menghasilkan HTML untuk nilai tersebut. JavaScript sendiri yang menentukan bagaimana data dimasukkan ke DOM. Jika developer melakukan:

```javascript
element.innerHTML = data.title;
```

maka browser akan mem-parsing `data.title` sebagai HTML. Jika `data.title` berasal dari user atau sumber yang tidak dipercaya, string berbahaya dapat menjadi markup aktif.

Karena itu, data yang ditampilkan melalui AJAX bukan secara otomatis aman hanya karena berasal dari endpoint Django. Keamanan tetap bergantung pada bagaimana JavaScript memasukkan data tersebut ke DOM.

Dalam Tugas 5, saya menggunakan dua lapisan perlindungan:

1. **Client-side escaping / safe DOM manipulation**

   Nilai teks yang berasal dari server di-escape sebelum digunakan dalam HTML yang dibangun JavaScript. Jika suatu elemen tidak membutuhkan HTML, pendekatan yang lebih aman adalah menggunakan `textContent`, karena browser memperlakukannya sebagai teks dan bukan sebagai markup.

2. **Server-side sanitization**

   Input teks pada `ModelForm` juga dibersihkan menggunakan `strip_tags` dalam method `clean_<field>`. Jika sebuah input hanya terdiri dari tag HTML berbahaya, validasi dapat menolaknya.

Kedua mekanisme tersebut memiliki fungsi yang berbeda. `strip_tags` bukan pengganti HTML escaping. Sanitization dilakukan ketika data masuk, sedangkan escaping diperlukan ketika data ditampilkan. Data lama yang sudah tersimpan sebelum sanitization juga tidak otomatis menjadi aman hanya karena validasi form baru telah diperbaiki.

Dengan demikian, prinsip utama yang digunakan adalah **jangan mempercayai data hanya karena data tersebut berasal dari database atau endpoint milik sendiri**. Data tetap harus diperlakukan sebagai untrusted data ketika dimasukkan ke dalam DOM.

---

## Verifikasi Implementasi

Sebelum submission, implementasi Tugas 5 diperiksa terhadap kondisi berikut:

* halaman dapat dimuat oleh pengunjung yang belum login;
* data daftar diambil melalui endpoint JSON;
* loading state muncul selama proses pengambilan data;
* empty state muncul ketika hasil pencarian kosong;
* error state ditampilkan ketika request gagal;
* pencarian tidak menyebabkan page reload;
* debounce mencegah request untuk setiap karakter;
* form tambah data berada di modal;
* POST menggunakan CSRF token;
* server melakukan permission check;
* response berhasil menggunakan status `201`;
* validation error menggunakan status `400`;
* akses yang tidak diperbolehkan menggunakan status `403`;
* data baru muncul pada daftar tanpa reload halaman;
* toast success/error memberikan feedback;
* pesan validation dari server diteruskan ke pengguna;
* data yang dirender melalui JavaScript di-escape;
* input teks dibersihkan melalui `clean_<field>` dan `strip_tags`;
* payload XSS tidak dieksekusi;
* implementasi tidak mengubah atau merusak fitur authentication, role, dan star dari Tugas 4.

---

## Progress

### Individual Assignment 5

* Menerapkan pola AJAX dari Tutorial 05 pada bagian portfolio yang sudah dikembangkan pada Tugas sebelumnya.
* Menambahkan endpoint JSON dengan `JsonResponse` manual.
* Mempertahankan informasi jumlah star dan status star pengguna pada response JSON.
* Mengubah rendering daftar menjadi asynchronous dengan Fetch API.
* Menambahkan loading, empty, dan error state.
* Menambahkan pencarian AJAX dengan debouncing.
* Memindahkan proses penambahan data ke modal pada halaman daftar.
* Menambahkan POST AJAX dengan `ModelForm`.
* Memastikan status HTTP membedakan keberhasilan, validation error, dan forbidden access.
* Mempertahankan permission check di sisi server.
* Menambahkan CSRF protection pada request AJAX.
* Memperbarui daftar setelah penambahan data tanpa page reload.
* Menggunakan toast untuk feedback success dan error.
* Menambahkan escaping pada data yang dirender melalui JavaScript.
* Menambahkan sanitization `strip_tags` pada field teks melalui `clean_<field>`.
* Menambahkan graceful error recovery untuk request AJAX.

---

# AI Disclosure — Individual Assignment 5

## AI Tools Used

| Tool | Tujuan Penggunaan | Jenis Bantuan |
|---|---|---|
| **Google Gemini** | Mengerjakan dan memahami Tutorial 05 sebagai prasyarat IA5, terutama AJAX/Fetch API, debouncing, modal, toast, CSRF, dan XSS protection | Penjelasan konsep, code suggestion, debugging, troubleshooting |
| **Claude (Anthropic)** | Membantu mengaudit requirement, memeriksa struktur kode, dan melakukan rubric review | Code generation, code review, security review, requirement audit, debugging |

## AI Usage & Prompting Strategy

Untuk Tutorial 05, Google Gemini digunakan secara bertahap berdasarkan instruksi tutorial. Prompt diberikan dengan konteks struktur project yang sudah ada sehingga solusi dapat disesuaikan dengan model, form, URL, dan template yang digunakan. Beberapa bagian yang dibahas meliputi implementasi AJAX, pencarian dengan debouncing, modal menggunakan Popover API, pengiriman form menggunakan Fetch API, toast, CSRF, dan XSS.

`https://share.gemini.google/ZHOTEV25B89q`
`https://share.gemini.google/o4oIK1KtdGna`

## Parts Assisted by AI

| Bagian | AI | Bantuan AI | Verifikasi/Perbaikan Manual |
|---|---|---|---|
| Adaptasi AJAX ke bagian portfolio | Claude | Menyusun endpoint JSON, fetch, dan rendering data | Menyesuaikan hasil dengan struktur model, URL, template, dan fitur existing |
| Search debouncing | Claude + Gemini | Menjelaskan dan mengimplementasikan debounce | Memeriksa perilaku pencarian dan memastikan tidak terjadi reload |
| Modal + AJAX POST | Claude + Gemini | Menyusun alur submit form melalui Fetch API | Mempertahankan struktur modal dan UI project yang sudah ada |
| CSRF | Claude + Gemini | Menyusun pengiriman token melalui `X-CSRFToken` / form data | Memastikan CSRF tetap aktif dan tidak menggunakan `csrf_exempt` |
| Permission check | Claude | Mengaudit agar akses tidak hanya dibatasi melalui template | Memastikan role dari Tugas 4 tetap menjadi sumber aturan akses |
| Final rubric audit | Claude | Membandingkan implementasi dengan checklist dan target rubric | Melakukan pengecekan akhir pada source code dan aplikasi |

## Critical Reflection on AI Limitations

AI tidak selalu menghasilkan kode yang langsung cocok dengan project. Pengalaman pada tugas sebelumnya menunjukkan bahwa AI dapat membuat asumsi berdasarkan contoh generik, misalnya menggunakan nama fungsi, field, URL, atau struktur model yang tidak ada pada project saya. Karena itu, pada IA5 saya memberikan source code yang relevan dan requirement lengkap sebelum meminta implementasi.

Pada Tutorial 05, beberapa contoh kode dari AI awalnya menggunakan struktur yang berasal dari tutorial Projects. Struktur tersebut tidak dapat langsung dipindahkan ke bagian portfolio lain karena nama field, URL, permission, dan komponen UI project saya berbeda. Kode perlu disesuaikan dengan project aktual.

Hal lain yang perlu diperhatikan adalah bahwa AI dapat menyatakan sebuah implementasi "sudah memenuhi checklist" berdasarkan source code tanpa benar-benar mengetahui seluruh kondisi runtime, database, browser, atau konfigurasi deployment. Oleh karena itu, klaim dari AI tetap saya perlakukan sebagai hasil review, bukan sebagai bukti pengujian.

## Manual Improvements & Verification

Perubahan manual dan proses verifikasi yang dilakukan dalam pengembangan IA5 meliputi:

* membandingkan nama field yang disarankan AI dengan field yang benar-benar ada pada model;
* memastikan URL yang digunakan JavaScript sesuai dengan `main/urls.py`;
* mempertahankan role dan permission dari Tugas 4;
* memastikan guest tetap dapat membaca data;
* memastikan permission tetap diperiksa di backend;
* memeriksa response status sesuai requirement, bukan hanya response body;
* menguji state loading, empty, dan error;
* memeriksa bahwa search tidak melakukan page reload;
* memastikan form POST menggunakan CSRF;
* menguji validation error dari `ModelForm`;
* menguji payload XSS seperti `<img src="x" onerror="alert('XSS!')">`;
* mengaudit penggunaan `innerHTML` agar tidak ada nilai server yang dimasukkan tanpa escaping;
* mempertahankan fungsi star dari Tugas 4;
* menghindari refactor yang tidak diperlukan.

AI diposisikan sebagai reviewer dan coding assistant. Keputusan akhir mengenai apakah suatu solusi sesuai dengan requirement, struktur project, dan desain tetap dilakukan berdasarkan source code dan hasil pengujian project.

## AI Prompting Log — Individual Assignment 5

| Tahap | AI | Tujuan | Strategi Prompt | Hasil |
|---|---|---|---|---|
| Tutorial 05 | Gemini | Memahami implementasi AJAX | Memberikan instruksi tutorial dan struktur project | Implementasi Fetch API dan JSON |
| Tutorial 05 | Gemini | Search debouncing | Meminta penjelasan sekaligus adaptasi ke struktur project | Search dijalankan setelah jeda input |
| Tutorial 05 | Gemini | Modal + AJAX POST | Memberikan model/form/template existing | Form dikirim tanpa page reload |
| Tutorial 05 | Gemini | XSS protection | Memberikan contoh payload dan source code rendering | `escapeHtml` + `strip_tags` diterapkan |
| TI5 | Claude | Target rubric 4 | Memberikan rubric secara eksplisit | Code quality dan UX diaudit terhadap kriteria nilai 4 |
| TI5 | Claude | Security audit | Meminta audit CSRF, permission, XSS, dan HTTP status | Kekurangan security/error handling diidentifikasi dan diperbaiki |
| TI5 | Claude | Final self-review | Meminta checklist audit setelah coding | Implementasi dibandingkan ulang dengan seluruh requirement |
