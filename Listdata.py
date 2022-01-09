list_data = [9,4,5,8,10]
waktu_terkecil = list_data[0] 
waktu_terbesar = list_data[0] 
nilai_rata_rata = 0
jumlah_waktu = 0
jumlah_apk = 0

for nilai_waktu in list_data:
  jumlah_apk = jumlah_apk + 1
  jumlah_waktu = jumlah_waktu + nilai_waktu
  if waktu_terbesar < nilai_waktu: 
    waktu_terbesar = nilai_waktu
  if waktu_terkecil > nilai_waktu:
    waktu_terkecil = nilai_waktu



print('isi list: ', list_data)
print('waktu terbesar pada list: ',waktu_terbesar)
print('waktu terkecil pada list: ',waktu_terkecil)
print('Jumlah waktu apk pada list: ',jumlah_apk)
print('Akumulasi jumlah nilai elemen pada list: ',jumlah_waktu)
