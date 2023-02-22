input_angka_awal = int(input('Masukkan awal deret: '))
input_angka_akhir = int(input('Masukkan akhir deret: '))

for i in range(input_angka_awal, input_angka_akhir):
    print(f'{i}', end=' ') if i%6!=0 and i%8!=0 else None