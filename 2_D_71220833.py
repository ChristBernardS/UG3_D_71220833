input_plat_nomor_kendaraan = input('Masukkan Plat Nomor : ').lower().split(' ')
try:
    nomor = int(input_plat_nomor_kendaraan[1])
    if nomor >= 0 and nomor <= 3000:
        print('Plat nomor tersebut diperuntukan untuk mobil')
    elif nomor > 3000 and nomor <= 4000:
        print('Plat nomor tersebut diperuntukan untuk motor')
    elif nomor > 4000 and nomor <= 5000:
        print('Plat nomor tersebut diperuntukan untuk angkutan umum')
    elif nomor > 5000:
        print('Plat nomor tidak terindikasi ketiga angkutan tersebut')
except:
    print('Plat Nomor Tidak Terindikasi, setelah kode dearah harus berupa nomor kendaraan')