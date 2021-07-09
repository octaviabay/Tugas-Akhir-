import os
print("-----------------------------------------------------")
print("|\tSelamat Datang di Cek Diagnosa Covid 19\t|")
print("-----------------------------------------------------")
nama = input("Nama\t : ")
pilihan = input("Halo, "+nama+"\nApakah anda ingin melakukan diagnosa? (y/n)")

os.system("clear")

while pilihan == "y":
    print("\nApakah anda merasakan gejala berikut ini?")
    print("1. Demam")
    print("2. Batuk kering")
    print("3. Mudah lelah")
    print("4. Nyeri tenggorokan")
    print("5. Diare")
    print("6. Mata memerah")
    print("7. Indra penciuman hilang")
    print("8. Sakit kepala")
    print("9. Perubahan warna pada jari tangan atau kaki")
    diag1 = input("Jawab (y/n)")

    if diag1 == "y":
        print("\nApakah anda juga mengalami jelaja berikut ini?")
        print("1. Sesak napas")
        print("2. Nyeri pada dada atau dada merasa tertekan")
        print("3. Hilangnya kemampuan berbicara atau bergerak")
        diag2 = input("Jawab (y/n")
        
        if diag2 == "y":
            print("\nHi, "+nama+"Hasil awal diagnosa anda adalah: ")
            print("Anda terpapar virus COVID 19, segera lakukan tes swab dan hubungi dokter")
        elif diag2 == "n":
            print("Hi, "+nama+"anda memiliki tanda terpapar virus COVID 19, sebaiknya lakukan tes dan hubungi dokter")
        else:
            print("Hi, "+nama+"Alhamdulillah anda sehat wal afiyat")

    else :
        print("Hi, "+nama+"Alhamdulillah anda sehat wal afiyat")

print("--------------------------------------------------------")
pilihan = input("Halo, "+nama+"Apakah anda ingin melakukan diagnosa ulang?(y/n) ")

if pilihan == "y":
    os.system("clear")
    print("----------------------------------------------------")
    print("|\tSelamat Datang di Cek Diagnosa Covid 19\t|")
    print("----------------------------------------------------")
else:
    print("-------------------TERIMA KASIH---------------------")

