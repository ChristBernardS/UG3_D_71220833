nama_lo = input('Masukkan Nama Lengkap Anda: ')
prodi_lo = input('Masukkan Prodi Anda: ')
nilai_lo = input('Masukkan Nilai (dalam Huruf) yang Anda Dapat: ')
try:
    if nilai_lo == 'A':
        print('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai_lo == 'A-':
        print('Nilai anda adalah 3.75, kamu keren!')
    elif nilai_lo == 'B+':
        print('Nilai anda adalah 3.25')
    elif nilai_lo == 'B':
        print('Nilai anda adalah 3.0')
    elif nilai_lo == 'B-':
        print('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai_lo == 'C+':
        print('Nilai anda adalah 2.25')
    elif nilai_lo == 'C':
        print('Nilai anda adalah 2.0')
    elif nilai_lo == 'D':
        print('Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai_lo == 'E':
        print('Nilai anda adalah 0, niat kuliah nggak sih???')
except:
    print('Inputan nilai yang anda masukkan tidak valid')