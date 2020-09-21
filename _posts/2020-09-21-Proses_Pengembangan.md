---
title: "Proses Pengembangan Perangkat Lunak"
date: 2020-09-21
header:
    image: "/assets/images/SDLC_PRPL/TeaserSDLC.jpg"
---
# Incremental Model dan Concurrent Development Model

## Incremental Model
![Incremental Model](/assets/images/SDLC_PRPL/IM.png)
Incremental Model adalah sistem pengembangan model pada Rekayasa Perangkat Lunak berdasarkan Requirement Software yang dipecah menjadi beberapa fungsi atau bagian, yang menjadikan proses pengembangannya menjadi bertahap. (increment)
Incremental Model merupakan kombinasi dari waterfall model yaitu dengan melakukan tahapan waterfall secara increment. HAsil dari increment menjadi dasar perbaikan untuk increment selanjutnya, dan akan dilakukan seterusnya hingga produk dianggap sempurna. 

Kelebihan | Kekurangan
------------ | -------------
Nilai pengguna dapat ditentukan pada setiap increment sehingga fungsionalitas sistem disediakan lebih awal | Setiap tambahan yang dibangun harus dimasukkan kedalam struktur yang ada tanpa menurunkan kualitas dari yang telah dibangun
Klien dibiasakan perlahan-lahan menggunakan produknya bagian per bagian | Kemungkinan tiap bagian tidak dapat diintegrasikan
Resiko kegagalan proyek lebih rendah | Sulitnya memetakan kebutuhan pengguna ke dalam rencana spesifik masing-masing hasil increment
Model menejemen yang sederhana | Membutuhkan waktu yang relative lama untuk produk yang lengkap 

## Concurrent Development Model
![Concurrent Development Model](/assets/images/SDLC_PRPL/CDM.png)
Concurrent Development Model Adalah sistem pengembangan dimana tahapan yang berbeda akan dikerjakan secara bersamaan bukan secara berurutan. Dimana setiap proses yang terhubung akan memiliki pemicu, baik proses itu akan dikerjakan atau tidak. 
Proses pada CDM menggambarkan aktivitas di dua dimensi, yaitu dimensi sistem dan dimensi komponen. Dimensi sistem ditujukan untuk aktivitas Design, Perakitan, dan Pengguaan. Sedangkan dimensi Komponen ditujukan untuk aktivitas Design dan Realisasi.

Kelebihan | Kekurangan
------------ | -------------
Perencanaan lebih matang | Perubahan besar-besaran memakan waktu yang lama
Sistem Lebih baik dan matang | Pembengkakan Biaya
#
#
#
#
# Kelebihan dan Kekurangan V Model, RAD Model, dan Spiral Model

## V Model

Kelebihan | Kekurangan
------------ | -------------
Fleksibel | Hanya bisa digunakan sekali dalam suatu project
Mudahnya proses penambahan Method dan Tool | Project Oriented
Bisa digunakan untuk project Tailoring | Beberapa aktivitas menjadi terlalu abstarak
User berpartisipasi dalam change board | Ketidakjelasan aktivitas

## RAD Model

Kelebihan | Kekurangan
------------ | -------------
Lebih Efektif dari Sequential model | Tidak cocok untuk sistem yang mempunyai resiko teknik yang tinggi
Waktu lebih singkat dan efisien | Membutuhkan tenaga kerja yang banyak untuk menyelesaikan proyek dalam skala besar
Memiliki kemampuan untuk menggunakan kembali komponen yang ada | Harus adanya kontrak baru jika ada perubahan di tengah

## Spiral Model

Kelebihan | Kekurangan
------------ | -------------
Dapat disesuaikan secara terus menerus | Resiko planning cukup besar
Cocok untuk pengembangan skala besar | Sulit diimplementasikan dalam projek kecil
Mudahnya Pengembangan | Alur proses kompleks
Produksi lebih cepat | Memakan waktu lama
Manajemen dan analisis resiko lebih cepat dan mudah | Penyelarasan dalam jadwal pengembangan dan anggaran
#
#
#
#
# Specialized Process Model, Agile Method, dan Scrum

## Specialized Process Model
Specialized Process Model merupakan gambaran yang mempresentasikan RPL agar mudah dipahami dan proses dapat dilakukan sesuai aturannya. Ada tiga pembahasan dalam Model ini.
1. Component Based Development
![Component Based Development](/assets/images/SDLC_PRPL/CBD.png)
Mengedepankan konsep reusability (dalam bentuk komponen). Kelebihannya akan ada banyak proses yang dipersingkat dan meningnkatnya reusability. Namun memiliki kekurangan dimana masalah compatibility menjadi masalah karena model terdahulu sering kali tidak kompatibel.
2. Formal Methods Model
![Formal Methods Model](/assets/images/SDLC_PRPL/FMM.png)
Menggunakan Model Matematis Untuk menghilangkan ambiguitas dan inkonsisten. Keuntungan menggunakan teknik formal method adalah meminimalkan resiko dengan adanya perhitungan komputasi. Namun kerugiannya ada pada biaya yang tinggi, kompleksitas, dan tidak umum untuk proyek software pada umumnya
3. Aspect Oriented Programming
![Aspect Oriented Programming](/assets/images/SDLC_PRPL/AOP.jpg)
Mengedepankan Separation of concern untuk fungsi yang tersebar. Kelebihan model ini adalah ia sudah mencakup orientasi objek (OOP) dan mudahnya maintainability. Namun menjadi lebih rumit untuk dipahami.

## Agile Method
![Agile Method](/assets/images/SDLC_PRPL/Agile.jpg)
Agile Method merupakan metode dalam manajemen Proyek yang digunakan dalam pengembangan perangkat lunak. Metode ini membantu tim dalam menanggapi ketidapkpastian karena adanya hubungan secara terus menerus dengan client. Metode ini menggunakan urutan kerja tambahan dan berulang yang dikenal dengan Sprint. 
Sprint adalah periode waktu yang dialokasikan untuk fase proyek tertentu. Sprint dianggap selesai ketika jangka waktunya habis. Pada metode ini juga mengedepankan fungsi sebagai ukuran utama dari kemajuan. 

Kelebihan | Kekurangan
------------ | -------------
Lebih fleksibel ketimbang metode lama | Lebih fokus pada pengembangan ketimbang user
Kerangka kerja lebih ringan | kurang fokus pada desain produk
Pembuatan produk yang lebih tepat dengan dengan perencanaan berulang dan feedback | Kurang efisien pada perusahaan besar

## Scrum
Scrum merupakan pengembangan dari Agile method, dimana pada setiap harinya selama sprint akan dilakukan pengecekan untuk melihat progress dari pekerjaan tersebut. 
![Scrum](/assets/images/SDLC_PRPL/Scrum.jpg)
Scrum terbagi menjadi beberapa tahapan sebagai berikut:
- Backlog
Merupakan daftar kebutuhan atau fitur proyek yang diprioritaskan yang memberikan nilai bisnis bagi client. Dimana perubahan bisa ditambahkan kapan saja dan Manajer produk akan menilai backlog dan memperbaruinya.
- Sprint
Terdiri dari unit kerja yang diperlukan untuk mencapai kebutuhan yang ditentukan dalam jaminan yang harus sesuai dengan waktu yang sudah ditentukan. Perubahan tidak diperbolehkan selama Sprint.
- Scrum Meeting
Pertemuan singkat yang diadakan setiap hari oleh tim Srum. Yaitu berupa evaluasi pengerjaan seperti apa yang sudah anda (anggota) lakukan sejak meeting terakhir, Kenadala yang terjadi, dan Rencana yang akan dicapai pada meeting berikutnya.

- Demos 
Penyampaian software increment ke client sehingga client dapat mengevaluasi dan memberikan feedback.

Kelebihan | Kekurangan
------------ | -------------
Penghematan waktu | Membutuhkan orang yang sudah berpengalaman
Monitoring aktivitasa lebih jelas |  Setiap tugas harus dapat didefinisikan dengan baik, karena mempengaruhi biaya dan waktu pengerjaan
Adanya short sprint dan constant feedback membuat SCRUM mudah mengatasi perubahan | Jika anggota tidak berkomitmen dengan baik, maka akan terjadi kegagalan

