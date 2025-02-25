📌 Sistem Manajemen Karyawan PT FJBS

Sistem ini merupakan program berbasis Python untuk mengelola data karyawan PT FJBS. Sistem ini memiliki fitur seperti autentikasi pengguna, manajemen data karyawan, pencarian karyawan, rekomendasi proyek, serta laporan ringkasan status karyawan.

📜 Fitur Utama

Login User & Admin

Admin: Username: admin, Password: admin123

User: Username: user, Password: user123

Manajemen Data Karyawan

Menampilkan daftar karyawan dalam bentuk tabel.

Menambahkan data karyawan (hanya admin).

Mengedit informasi karyawan (hanya admin).

Menghapus data karyawan (hanya admin).

Filter & Pencarian

Filter berdasarkan Nama atau Divisi.

Rekomendasi Proyek

Menampilkan rekomendasi proyek berdasarkan divisi karyawan.

Laporan Ringkasan Status Karyawan

Menampilkan total karyawan, jumlah aktif, dan jumlah cuti.

🛠 Cara Menjalankan Program

1. Persyaratan

Pastikan Anda memiliki Python terinstal di sistem Anda.
Program ini menggunakan pustaka tabulate, jika belum terinstal, jalankan perintah berikut:

pip install tabulate

2. Menjalankan Program

Jalankan file Python dengan perintah:

python capstone.py

📝 Struktur Data Karyawan

Data karyawan disimpan dalam bentuk list of dictionary dengan struktur berikut:

{
    'NIP': 'Abc111',
    'Nama': 'Fahmi Zaitulah',
    'Jabatan': 'Administrator IT',
    'Divisi': 'IT',
    'Status': 'Aktif'
}

🚀 Fitur Login

Setiap pengguna harus login terlebih dahulu untuk mengakses sistem.

Admin dapat menambah, mengedit, dan menghapus data.

User hanya dapat melihat data.

🎯 Fitur Tambah Data Karyawan

Admin harus memasukkan NIP unik dengan format 3 huruf + 3 angka (contoh: Abc123).

Nama hanya boleh mengandung alfabet.

Admin memilih Jabatan, Divisi, dan Status dari daftar yang tersedia.

Admin dapat memilih untuk menyimpan atau membatalkan data yang telah dimasukkan.

🔍 Fitur Filter Karyawan

Pengguna dapat mencari karyawan berdasarkan:

Nama (Input sebagian atau seluruh nama)

Divisi (Misalnya: "IT", "Keuangan", dll.)

📊 Laporan Ringkasan Status Karyawan

Menampilkan:

Total jumlah karyawan.

Jumlah karyawan dengan status "Aktif".

Jumlah karyawan dengan status "Cuti".

💡 Rekomendasi Proyek

Sistem akan memberikan rekomendasi proyek berdasarkan divisi karyawan.
Contoh:

Divisi IT → "Pengembangan Sistem Keamanan PT FJBS"

Divisi Keuangan → "Membantu Proses Analisis Risiko Keuangan PT FJBS"

🤝 Kontribusi

Jika Anda ingin mengembangkan sistem ini lebih lanjut, silakan fork repository ini dan ajukan pull request dengan perbaikan atau fitur tambahan.

📌 Lisensi

Proyek ini bersifat open-source dan bebas digunakan serta dikembangkan lebih lanjut.

📧 Kontak

Jika ada pertanyaan atau saran, silakan hubungi Frans Julian Bryan Sagala
melalui email: fransjulian741@gmail.com

