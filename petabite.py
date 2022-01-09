ram = int(input("Masukkan kapasitas RAM : "))
petabite = int(input("Masukkan kapasitas petbite : "))
os = int(input("Berapa ROM OS (GB): "))
apk1 = int(input("Aplikasi 1 (GB): "))
apk2 = int(input("Aplikasi 2 (GB): "))
#Rumus perhitungan
petabid = (ram / petabite )
pakai = (os + apk1 + apk2 )
os  = (ram - os - apk1 - apk2 )
alokasi1 = (ram / petabite )
alokas0 = (ram - apk1 - apk2 ) 



#hasil akhir5
print("-------------------------")
print("kapasitas ram :",ram)
print("kapasitas petabite:",petabite)
print("Kapasitas peta bid adalah : %d KBps" % petabid)
print("alokasi 0 : %d " % alokasi1)
print("alokasi 1 : %d " % alokas0)
print("sisa RAM terpakai : %d RAM" % pakai)
print("sisa RAM : %d RAM" % os)