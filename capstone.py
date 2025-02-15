from tabulate import tabulate
import re

# Data karyawan dan proyek
data_karyawan = [
    {'NIP': 'Abc111', 'Nama': 'Fahmi Zaitulah', 'Jabatan': 'Administrator IT', 'Divisi': 'IT', 'Status': 'Aktif'},
    {'NIP': 'Abc112', 'Nama': 'Darius Erwin', 'Jabatan': 'Manager Pergudangan', 'Divisi': 'Pergudangan', 'Status': 'Aktif'},
    {'NIP': 'Abc113', 'Nama': 'Laila Amalia', 'Jabatan': 'Analyst Keuangan', 'Divisi': 'Keuangan', 'Status': 'Aktif'},
    {'NIP': 'Abc114', 'Nama': 'Rizky Pratama', 'Jabatan': 'Manajer Pemasaran', 'Divisi': 'Pemasaran', 'Status': 'Aktif'},
    {'NIP': 'Abc115', 'Nama': 'Siti Nurhaliza', 'Jabatan': 'Spesialis SDM', 'Divisi': 'Sumber Daya Manusia', 'Status': 'Cuti'}
]

rekomendasi_proyek = {
    'IT': 'Pengembangan Sistem Keamanan PT FJBS',
    'Pergudangan': 'Optimasi Rantai Pasokan PT FJBS',
    'Keuangan': 'Membantu Proses Analisis Risiko Keuangan PT FJBS',
    'Pemasaran': 'Menentukan Strategi Digital Marketing di PT FJBS',
    'Sumber Daya Manusia': 'Implementasi HRIS (Human Resources Information System) di PT FJBS'
}

# Data user untuk autentikasi dengan role masing-masing
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

# Variabel global untuk menyimpan user yang sedang login
current_user = None

def login():
    global current_user
    attempts = 3
    while attempts > 0:
        print('\nJIKA ANDA ADALAH USER, MASUKKAN USERNAME: "user", PASSWORD "user123"')
        print("\n=== Login ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        if username in users and users[username]["password"] == password:
            current_user = {"username": username, "role": users[username]["role"]}
            print(f"\nSelamat datang, {username}! Anda login sebagai {current_user['role']}.")
            return True  # Login berhasil
        else:
            attempts -= 1
            print(f"Username atau Password salah. {attempts} kesempatan tersisa.")
    print("Akses ditolak. Program dihentikan.")
    return False  # Login gagal

# Daftar valid untuk divisi dan status
daftar_divisi = {'IT', 'Pergudangan', 'Keuangan', 'Pemasaran', 'Sumber Daya Manusia'}
daftar_status = {'Aktif', 'Cuti'}

# Mendapatkan daftar jabatan dari data_karyawan
daftar_jabatan = {karyawan['Jabatan'] for karyawan in data_karyawan}

# Regex pattern untuk NIP
nip_pattern = re.compile(r'^[A-Za-z]{3}\d{3}$')  # Contoh: Abc111

# Fungsi validasi pilihan dari daftar yang tersedia
def validasi_pilihan(prompt, daftar_pilihan):
    daftar_pilihan = sorted(list(daftar_pilihan))  # Ubah ke list dan urutkan agar konsisten
    while True:
        print(f"\nPilihan {prompt.lower()} yang tersedia:")
        for i, pilihan in enumerate(daftar_pilihan, 1):
            print(f"  {i}. {pilihan}")  # Menampilkan pilihan dengan nomor urut

        value = input(f"\nMasukkan angka pilihan {prompt}: ").strip()
        if value.isdigit():  # Memastikan input adalah angka
            index = int(value) - 1  # Sesuaikan dengan indeks list (mulai dari 0)
            if 0 <= index < len(daftar_pilihan):
                return daftar_pilihan[index]  # Kembalikan pilihan yang sesuai
        print(f"❌ Input tidak valid. Pilih angka dari daftar di atas.")

# Fungsi validasi spesifik
def validasi_jabatan():
    return validasi_pilihan('Jabatan', daftar_jabatan)

def validasi_divisi():
    return validasi_pilihan('Divisi', daftar_divisi)

def validasi_status():
    return validasi_pilihan('Status', daftar_status)

# Fungsi input alfabet untuk nama
def input_alphabet(prompt):
    while True:
        value = input(prompt).strip().title()
        if value.replace(" ", "").isalpha():
            return value
        print("❌ Inputan tidak valid, mohon gunakan alphabet.")

def daftar(data):
    if data:
        print(tabulate(data, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nTidak ada data karyawan.")

# Fungsi menambahkan data karyawan dengan validasi tambahan
def tambah_karyawan():
    if current_user["role"] != "admin":
        print("⚠️ Hanya admin yang dapat menambah data karyawan.")
        return

    while True:
        print('''\n++++++++++++++++++++++++++++\n    Tambah Data Karyawan:\n++++++++++++++++++++++++++++\n  1. Tambah Data Karyawan\n  2. Kembali Ke Menu Utama''')
        pilihan = input('Pilih Menu (1 - 2): ').strip()
        if pilihan not in ['1', '2']:
            print("Pilihan tidak valid. Silakan pilih angka 1 - 2.")
            continue

        if pilihan == '1':
            while True:
                nip = input('Masukkan NIP Karyawan: ').strip().capitalize()
                if not nip_pattern.match(nip):
                    print("❌ Format NIP tidak valid! Harus berupa 3 huruf + 3 angka (contoh: Abc123).")
                    continue
                if any(k['NIP'] == nip for k in data_karyawan):
                    print("⚠️ NIP tersebut sudah ada.")
                    continue
                break  # Keluar dari loop jika valid

            nama = input_alphabet('Masukkan Nama: ')
            jabatan = validasi_jabatan()
            divisi = validasi_divisi()
            status = validasi_status()

            simpan_data = input('Simpan Data? (Y/N): ').strip().lower()
            if simpan_data == 'y':
                data_karyawan.append({
                    'NIP': nip,
                    'Nama': nama,
                    'Jabatan': jabatan,
                    'Divisi': divisi,
                    'Status': status
                })
                print('✅ Data Karyawan Berhasil Disimpan.')
            else:
                print('❌ Data Karyawan Batal Disimpan.')
        else:
            break


def edit_karyawan():
    # Hanya admin yang dapat mengedit data karyawan
    if current_user["role"] != "admin":
        print("⚠️ Hanya admin yang dapat mengedit data karyawan.")
        return

    while True:
        nip = input('Masukkan NIP Karyawan yang ingin diedit: ').strip().capitalize()
        karyawan = next((k for k in data_karyawan if k['NIP'] == nip), None)
        
        if karyawan:
            karyawan['Nama'] = input_alphabet(f"Masukkan Nama Baru (NAMA SEBELUMNYA -> {karyawan['Nama']}): ") or karyawan['Nama']
            karyawan['Jabatan'] = validasi_jabatan()
            karyawan['Divisi'] = validasi_divisi()
            karyawan['Status'] = validasi_status()
            print('✅ Data Karyawan Berhasil Diperbarui!')
            break  # Keluar dari loop setelah update
        else:
            print('⚠️ Data Karyawan Tidak Ditemukan. Silakan coba lagi.')

def hapus_karyawan():
    # Hanya admin yang dapat menghapus data karyawan
    if current_user["role"] != "admin":
        print("⚠️ Hanya admin yang dapat menghapus data karyawan.")
        return

    while True:
        daftar(data_karyawan)
        print('''
++++++++++++++++++++++++++++
    Hapus Data Karyawan:
++++++++++++++++++++++++++++
  1. Hapus Data Karyawan
  2. Kembali Ke Menu Utama
        ''')
        inputhapus = input('Pilih Menu (1 - 2): ').strip()
        if inputhapus not in ['1', '2']:
            print("Pilihan tidak valid. Silakan pilih angka 1 - 2.")
            continue

        if inputhapus == '1':
            nip = input('Masukkan NIP Karyawan: ').strip().capitalize()
            found = False
            for i, karyawan in enumerate(data_karyawan):
                if karyawan['NIP'] == nip:
                    found = True
                    konfirmasi = input('Apakah Anda yakin ingin menghapus? (Y/N): ').strip().lower()
                    if konfirmasi == 'y':
                        del data_karyawan[i]
                        print('✅ Data Karyawan Berhasil Dihapus.')
                    else:
                        print('❌ Data Karyawan Batal Dihapus.')
                    break
            if not found:
                print('⚠️ Data Karyawan Tidak Ditemukan.')
        else:
            break

def filter_karyawan():
    pilihan = input("Cari berdasarkan Nama (N) atau Divisi (D)? ").strip().lower()
    keyword = input("Masukkan keyword pencarian: ").strip().lower()

    if pilihan == 'n':
        hasil = [k for k in data_karyawan if keyword in k['Nama'].lower()]
    elif pilihan == 'd':
        hasil = [k for k in data_karyawan if keyword in k['Divisi'].lower()]
    else:
        print("Pilihan tidak valid. Silakan masukkan N atau D.")
        return

    daftar(hasil) if hasil else print('⚠️ Tidak ada hasil yang ditemukan.')

def rekomendasi():
    daftar(data_karyawan)
    while True:
        nip = input('🔍 Masukkan NIP Karyawan: ').strip()
        # Sesuaikan case input agar cocok dengan data
        karyawan = next((k for k in data_karyawan if k['NIP'].lower() == nip.lower()), None)
        if karyawan:
            divisi = karyawan['Divisi']
            rekomendasi_proyek_text = rekomendasi_proyek.get(divisi, '❌ Belum ada rekomendasi proyek')
            data_tabel = [
                ["📌 NIP", karyawan['NIP']],
                ["👤 Nama", karyawan['Nama']],
                ["🏢 Divisi", divisi],
                ["💡 Rekomendasi Proyek", rekomendasi_proyek_text]
            ]
            print("\n✨ Rekomendasi Proyek Karyawan ✨")
            print(tabulate(data_tabel, tablefmt="fancy_grid"))
            break  # Keluar dari loop setelah menemukan karyawan yang sesuai
        else:
            print('⚠️ Data Karyawan Tidak Ditemukan. Silakan coba lagi')
            
def laporan_ringkasan():
    total_karyawan = len(data_karyawan)
    aktif = sum(1 for k in data_karyawan if k['Status'].lower() == 'aktif')
    cuti = total_karyawan - aktif
    data_ringkasan = [
        ["Total Karyawan", total_karyawan],
        ["Karyawan Aktif", aktif],
        ["Karyawan Cuti", cuti]
    ]
    print("\n📊 Ringkasan Data Status Karyawan 📊")
    print(tabulate(data_ringkasan, headers=["Kategori", "Jumlah"], tablefmt="fancy_grid"))

def menu():
    while True:
        print('''
        ++++++++++++++++++++++++++++
            MENU UTAMA PT FJBS:
        ++++++++++++++++++++++++++++
          1. Data Karyawan
          2. Tambah Data Karyawan
          3. Edit Karyawan
          4. Filter Divisi Karyawan
          5. Hapus Data Karyawan
          6. Rekomendasi Proyek Karyawan
          7. Laporan Ringkasan Status Karyawan
          8. Keluar
        ''')
        inputmenu = input('Pilih Menu (1 - 8): ').strip()
        if inputmenu not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Pilihan tidak valid. Silakan pilih angka 1 - 8.")
            continue

        if inputmenu == '1':
            daftar(data_karyawan)
        elif inputmenu == '2':
            tambah_karyawan()
        elif inputmenu == '3':
            edit_karyawan()
        elif inputmenu == '4':
            filter_karyawan()
        elif inputmenu == '5':
            hapus_karyawan()
        elif inputmenu == '6':
            rekomendasi()
        elif inputmenu == '7':
            laporan_ringkasan()
        elif inputmenu == '8':
            print('Terima Kasih!')
            break

# Program Utama
if login():
      menu()
