from tabulate import tabulate

data_karyawan = [
    {'NIP': 'Abc111', 'Nama': 'Fahmi Zaitulah', 'Jabatan': 'Administrator IT', 'Divisi': 'IT', 'Status': 'Aktif'},
    {'NIP': 'Abc112', 'Nama': 'Darius Erwin', 'Jabatan': 'Manager Pergudangan', 'Divisi': 'Pergudangan', 'Status': 'Aktif'},
    {'NIP': 'Abc113', 'Nama': 'Laila Amalia', 'Jabatan': 'Analyst Keuangan', 'Divisi': 'Keuangan', 'Status': 'Aktif'},
    {'NIP': 'Abc114', 'Nama': 'Rizky Pratama', 'Jabatan': 'Manajer Pemasaran', 'Divisi': 'Pemasaran', 'Status': 'Aktif'},
    {'NIP': 'Abc115', 'Nama': 'Siti Nurhaliza', 'Jabatan': 'Spesialis SDM', 'Divisi': 'Sumber Daya Manusia', 'Status': 'Cuti'}
]

project_karyawan = [
    {'NIP': 'Abc111', 'Nama': 'Fahmi Zaitulah', 'Project': 'Pembuatan website DPRD Kota Bandung'},
    {'NIP': 'Abc112', 'Nama': 'Darius Erwin', 'Project': 'Aplikasi pengelolaan stok PT Mayora'},
    {'NIP': 'Abc113', 'Nama': 'Laila Amalia', 'Project': 'Penyusunan anggaran PT Indofood'},
    {'NIP': 'Abc114', 'Nama': 'Rizky Pratama', 'Project': 'Peningkatan pemasaran PT Mustika Ratu'},
    {'NIP': 'Abc115', 'Nama': 'Siti Nurhaliza', 'Project': 'Pengembangan fitur rekrutmen online'}
]

rekomendasi_proyek = {
    'IT': 'Pengembangan Sistem Keamanan Perusahaan',
    'Pergudangan': 'Optimasi Rantai Pasokan PT Unilever',
    'Keuangan': 'Analisis Risiko Keuangan Bank BRI',
    'Pemasaran': 'Strategi Digital Marketing PT Gojek',
    'Sumber Daya Manusia': 'Implementasi HRIS di PT Telkom'
}
# Validasi input hanya boleh alfabet dan angka
def input_alphabet_numeric(prompt):
  while True:
      value = input(prompt).strip().title()
      if value.replace(" ", "").isalnum():  # Mengizinkan spasi dan angka
          return value
      print("❌ Inputan tidak valid, mohon gunakan alphabet atau angka.")

# Validasi input hanya boleh alfabet
def input_alphabet(prompt):
    while True:
        value = input(prompt).strip().title()
        if value.replace(" ", "").isalpha():  # Mengizinkan spasi
            return value
        print("❌ Inputan tidak valid, mohon gunakan alphabet.")

def daftar(data_karyawan):
    if data_karyawan:
        print(tabulate(data_karyawan, headers="keys", tablefmt="fancy_grid"))
    else:
        print("\nTidak ada data karyawan.")

def hapus_karyawan():
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

def rekomendasi():
    daftar(data_karyawan)

    nip = input('🔍 Masukkan NIP Karyawan: ').strip()

    # Menyesuaikan case input agar cocok dengan data
    karyawan = next((k for k in data_karyawan if k['NIP'].lower() == nip.lower()), None)

    if karyawan:
        divisi = karyawan['Divisi']
        rekomendasi = rekomendasi_proyek.get(divisi, '❌ Belum ada rekomendasi proyek')

        data_tabel = [
            ["📌 NIP", karyawan['NIP']],
            ["👤 Nama", karyawan['Nama']],
            ["🏢 Divisi", divisi],
            ["💡 Rekomendasi Proyek", rekomendasi]
        ]

        print("\n✨ Rekomendasi Proyek Karyawan ✨")
        print(tabulate(data_tabel, tablefmt="fancy_grid"))

    else:
        print('⚠️ Data Karyawan Tidak Ditemukan.')

def edit_karyawan():
    nip = input('Masukkan NIP Karyawan yang ingin diedit: ').strip().capitalize()
    for karyawan in data_karyawan:
        if karyawan['NIP'] == nip:
            karyawan['Nama'] = input(f"Nama ({karyawan['Nama']}): ") or karyawan['Nama']
            karyawan['Jabatan'] = input(f"Jabatan ({karyawan['Jabatan']}): ") or karyawan['Jabatan']
            karyawan['Divisi'] = input(f"Divisi ({karyawan['Divisi']}): ") or karyawan['Divisi']
            karyawan['Status'] = input(f"Status ({karyawan['Status']}): ") or karyawan['Status']
            print('✅ Data Karyawan Berhasil Diperbarui!')
            return
    print('⚠️ Data Karyawan Tidak Ditemukan.')

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

menu()
