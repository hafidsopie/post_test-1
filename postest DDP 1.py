# Pesan Awal

print('''
SELAMAT DATANG DI PROGRAM MENGHITUNG VOLUME BANGUN RUANG 
SILAHKAN LOGIN TERLEBIH DAHULU YA :)
''')

# DESKRIPSIKAN VARIABLE USERNAME, NIM DAN PASSWORD
user = 'SOPI'
nim = '2309116048'
password = '246810'

 # BUAT INPUT UNTUK MEMASUKAN USERNAME, NIM DAN PASSWORD
username = input("Masukkan Username: ")
nim = input("Masukkan NIM: ")
password = input("Masukkan Password: ")

    # Memeriksa username, NIM, dan password
if username == user and nim == nim and password == password:
        print(20*"=")
        print("ANDA BERHASIL LOGIN")
        print(20*"=")
        print(20*"=")
        print("MASUKAN PILIHAN")
        print(20*"=")
        print("[1]. Volume Tabung")
        print("[2]. Volume Bola")
        print("[3]. Volume Limas Segitiga")
        print("[4]. Keluar ")

        # MENGAMBIL PILIHAN DARI USER
        pilihan = int(input("Masukkan Pilihan (1/2/3/4): "))
        

        #  Menghitung Volume tabung
        if pilihan == 1:
            tinggi = float(input("Masukkan Tinggi  : "))
            r = float(input("Masukkan Jari-jari : "))
            if r % 7 == 0:
                print("Gunakan phi = 22/7 ")
                phi = 22/7
            else:
                print("Gunakan phi = 3.14 ")
                phi = 3.14
            hasil = phi * r * r * tinggi
            print(f" VOLUME TABUNG = {hasil}")
            

        # Menghitung volume bola
        elif pilihan == 2:
            r = float(input("Masukkan Jari-jari : "))
            if r % 7 == 0:
                print("Gunakan phi = 22/7  ")
                phi = 22/7
            else:
                print("Gunakan phi = 3.14 ")
                phi = 3.14
            hasil = 4/3 * phi * r * r * r
            print(f"VOLUME BOLA = {hasil}")
            
                
        # Menghitung Volume limas segitiga
        elif pilihan == 3:
            luas_alas = float(input("Masukkan Luas Alas : "))
            tinggi_limas = float(input("Masukkan Tinggi Limas : "))
            hasil = luas_alas * tinggi_limas
            print(f"VOLUME LIMAS SEGITIGA = {hasil}")
            
        elif pilihan == 4:
            print("terima kasih wassalamualaikum :)")