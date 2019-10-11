#TUGAS : buat fungsi _APA_SAJA_YANG_KALIAN_TAHU
#DAN GUNAKAN

nama = 'Muhammad Munajat'
program = 'Gerak Lurus Berubah Beraturan'

print(f'program {program} oleh {nama}')



def hitung_gaya(massa, kecepatan):
    gaya = massa / kecepatan
    print(f'massa = {massa / 1000}kg dengan kecepatan = {kecepatan / 60}m/s')
    print(f'sehingga gaya = {gaya} kgm/s')

    return massa / kecepatan

#massa = 1000
#kecepatan = 60
gaya = hitung_gaya(1000, 60)
gaya = hitung_gaya(10000, 60)
