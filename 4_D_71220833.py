nama_lo = input('Masukkan Nama Lengkap Anda: ')
prodi_lo = input('Masukkan Prodi Anda: ')
nilai_lo = input('Masukkan Nilai (dalam Huruf) yang Anda Dapat: ').lower()
try:
    if nilai_lo == 'a':
        print('Nilai anda adalah 4.0')
    elif nilai_lo == 'a-':
        print('Nilai anda adalah 3.75, kamu keren!')
    elif nilai_lo == 'b+':
        print('Nilai anda adalah 3.25')
    elif nilai_lo == 'b':
        print('Nilai anda adalah 3.0')
    elif nilai_lo == 'b-':
        print('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai_lo == 'c+':
        print('Nilai anda adalah 2.25')
    elif nilai_lo == 'c':
        print('Nilai anda adalah 2.0')
    elif nilai_lo == 'd':
        print('Nilai anda adalah 1.0, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai_lo == 'e':
        print('Nilai anda adalah 0, niat kuliah nggak sih???')
except:
    print('Inputan nilai yang anda masukkan tidak valid')