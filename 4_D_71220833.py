nama_lo = input('Masukkan Nama Lengkap Anda: ')
prodi_lo = input('Masukkan Prodi Anda: ')
nilai_lo = input('Masukkan Nilai (dalam Huruf) yang Anda Dapat: ')
try:
    nilai_lo = int(nilai_lo)
    print('Inputan nilai yang anda masukkan tidak valid')
except:
    if nilai_lo == 'A':
        print('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai_lo == 'A-':
        print('Nilai anda adalah 3.75, kamu keren!')
    elif nilai_lo == 'B+':
        print('Nilai anda adalah 3.25, kamu hebat')
    elif nilai_lo == 'B':
        print('Nilai anda adalah 3.0, nilai minimal untuk memenuhi standar ortu')
    elif nilai_lo == 'B-':
        print('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai_lo == 'C+':
        print('Nilai anda adalah 2.25, belajar yang bener')
    elif nilai_lo == 'C':
        print('Nilai anda adalah 2.0, banyak mata kuliah yang harus kamu ulangi')
    elif nilai_lo == 'D':
        print('Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai_lo == 'E':
        print('Nilai anda adalah 0, niat kuliah nggak sih???')