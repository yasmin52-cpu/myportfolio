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
