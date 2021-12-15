import getpass
import json
import statistics
from tabulate import tabulate


data_wisata = "data_wisata.json"
data_admin = "data_admin.json"
data_saran_wisata = "data_saran_wisata.json"

def login_Admin():
    with open (data_admin, "r") as data:
        isi_data = json.load(data)
    username = input("Masukan Username Anda: ")
    password = str(getpass.getpass("Masukan Password: "))
    ulang = 0
    while ulang <= 2 and username != isi_data['username'] or password != isi_data['password']:
        print("Password yang anda masukan Salah!")
        username = input("\nMasukan Username Anda: ")
        password = str(getpass.getpass("Masukan Password: "))
        if username == isi_data['username'] and password == isi_data['password']:
            print("login Berhasil\n")
            show_menu_admin()
        elif username != isi_data['username'] or password != isi_data['password']:
                ulang +=1
                if ulang > 2:
                    print("Silahkan Melakukan Update ")
                    show_menu()
    if username == isi_data['username'] and password == isi_data['password']:
            print("Login Berhasil\n")
            show_menu_admin()

def update_PasswordAdmin():
    temp={}
    with open (data_admin, "r") as data:
        isi_data = json.load(data)
        temp = isi_data
    i = 0
    pass_lama = str(getpass.getpass("Masukan Password Lama: "))
    while i <= 2 and pass_lama != temp['password']:
        print("Passowrd Lama Anda Salah")
        pass_lama = str(getpass.getpass("\nMasukan Password Lama: "))
        if pass_lama == temp['password']:
            pass_update = str(getpass.getpass("Masukan Password Baru Anda: "))
            temp['password'] = pass_update
            with open (data_admin, "w") as data_file:
                dataa = json.dumps(temp, indent=4)
                data_file.write(dataa)
                if temp['password'] == pass_update:
                    print("Passowrd Berhasil diperbarui")
                else:
                    print("Password Gagal Diperbarui")
        elif pass_lama != temp['password']:
            i+=1
            if i > 2:
                print("Reset data anda")
                exit()
    else:
        pass_update = str(getpass.getpass("Masukan Password Baru Anda: "))
        temp['password'] = pass_update
        with open (data_admin, "w") as data_file:
            dataa = json.dumps(temp, indent=4)
            data_file.write(dataa)
            if temp['password'] == pass_update:
                print("Passowrd Berhasil diperbarui")
            else:
                print("Password Gagal Diperbarui")

def show_wisata_admin():
    temp = []
    nama = []
    alamat = []
    kategori = []
    tiket_weekend = []
    tiket_weekday = []
    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    header = ['Nama','Alamat','Ketegori','Tiket Ketika Weekend','Harga Ketika Weekday']
    table1 = []
    
    for i in temp:
        nama = i['nama']
        alamat = i['alamat']
        kategori = i['kategori']
        tiket_weekend = i['harga_tiket_weekend']
        tiket_weekday = i['harga_tiket_weekday']
        table1.append([nama,alamat,kategori,tiket_weekday,tiket_weekend])
        
    print(tabulate(table1,header,tablefmt='grid'))
    print("\n")
    show_menu2_admin()

def show_saran_wisata_admin():
    temp = []
    nama = []
    alamat = []
    kategori = []
    tiket_weekend = []
    tiket_weekday = []
    with open (data_saran_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    header = ['Nama','Alamat','Kategori','Tiket Ketika Weekend','Harga Ketika Weekday']
    table = []
    for i in temp:
        nama = i['nama']
        alamat = i['alamat']
        kategori = i['kategori']
        tiket_weekend = i['harga_tiket_weekend']
        tiket_weekday = i['harga_tiket_weekday']
        table.append([nama,alamat,kategori,tiket_weekday,tiket_weekend])
    print(tabulate(table,header,tablefmt='fancy_grid'))
    show_menu2_admin()

def insert_wisata():
    temp = {}
    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    
    nama = input("Masukan Nama Wisata: ")
    alamat = input("Masukan Alamat Wisata: ")
    kategori = input("Masukan Kategori Wisata: ")
    harga_tiket_weekday = int(input("Masukan harga saaat weekday: "))
    harga_tiket_weekend= int(input("Masukan harga saaat weekend: "))
    temp.append({
        'nama':nama,
        'alamat':alamat,
        'kategori':kategori,
        'harga_tiket_weekday':harga_tiket_weekday,
        'harga_tiket_weekend':harga_tiket_weekend
    })

    with open (data_wisata, "w") as data_file:
        dataa = json.dumps(temp, indent=4)
        data_file.write(dataa)
        print("Berhasil ditambahkan")
    show_menu2_admin()

def update_wisata():
    temp = {}
    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    print ("----------- Halo Kak, Berikut Daftar Wisata ----------")
    print ("[1] Pantai Papuma")
    print ("[2] Taman Nasional Meru Beitri")
    print ("[3] Kebun Teh Gunung Gambir")
    print ("[4] Air Terjun Tancak")
    print ("[5] Air Terjun Antrokan")
    print ("[6] Pantai Bandealit")
    print ("[7] Pantai Payangan")
    print ("[8] Taman Edukasi Botani")
    print ("[9] Taman Galaxy")
    print ("[10] Kebun Belimbing")
    print ("[11] Pantai Puger")
    input_userr = int(input("Masukan Pilihan: "))
    if input_userr == 1 or input_userr == 2 or input_userr == 3 or input_userr == 4 or input_userr == 5 or input_userr == 6 or input_userr == 7 or input_userr == 8 or input_userr == 9 or input_userr == 10 or input_userr == 11 :
        for i in range(len(temp)):
            
            input_user = input("Masukan Nama Wisata: ")
            if temp[i]['nama'] == input_user:
                nama = input("Masukan Nama Wisata: ")
                alamat = input("Masukan Alamat Wisata: ")
                kategori = input("Masukan Kategori Wisata: ")
                harga_tiket_weekday = int(input("Masukan harga saaat weekday: "))
                harga_tiket_weekend= int(input("Masukan harga saaat weekend: "))
                temp[i]['nama'] = nama
                temp[i]['alamat'] = alamat
                temp[i]['kategori'] = kategori
                temp[i]['harga_tiket_weekday'] = harga_tiket_weekday
                temp[i]['harga_tiket_weekend'] = harga_tiket_weekend
                with open (data_wisata, "w") as data_file:
                    dataa = json.dumps(temp, indent=4)
                    data_file.write(dataa)
                    print("Berhasil diubah")
            else:
                print("Salah input")
                break


def show_wisata_user():
    temp = []
    nama = []
    alamat = []
    kategori = []
    tiket_weekend = []
    tiket_weekday = []
    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    header = ['Nama','Alamat','Ketegori','Tiket Ketika Weekend','Harga Ketika Weekday']
    table = []
    
    for i in temp:
        nama = i['nama']
        alamat = i['alamat']
        kategori = i['kategori']
        tiket_weekend = i['harga_tiket_weekend']
        tiket_weekday = i['harga_tiket_weekday']
        table.append([nama,alamat,kategori,tiket_weekday,tiket_weekend])
        
    print(tabulate(table,header,tablefmt='fancy_grid'))
    print("\n")
    show_menu2_user()

def insert_saran_wisata():
    temp = []
    with open (data_saran_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    inputan_user = int(input("Apa Anda Setuju mengisi data dengan sebenar-benarnya ?\n1.Iya\t.Tidak "))
    if inputan_user == 1:  
        nama = input("Masukan nama wisata: ")
        alamat = input("Masukan alamat wisata: ")
        kategori = input("Masukan Kategori Wisata: ")
        harga_tiket_weekday = int(input("Masukan harga saaat weekday: "))
        harga_tiket_weekend= int(input("Masukan harga saaat weekend: "))
        temp.append({
            'nama':nama,
            'alamat':alamat,
            'kategori':kategori,
            'harga_tiket_weekday':harga_tiket_weekday,
            'harga_tiket_weekend':harga_tiket_weekend
        })

        with open (data_saran_wisata, "w") as data_file:
            dataa = json.dumps(temp, indent=4)
            data_file.write(dataa)
            print("Berhasil ditambahkan")
    elif inputan_user == 2:
        show_menu_user()
    else:
        print("inputan Tidak Tersedia")
        show_menu_user()


def jumlah_wisata():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    print ("----------- Berikut Daftar Kategori ----------")
    print ("[1] Air Terjun\n[2] Kebun\n[3] Pantai\n[4] Taman\n[5] Semua Kategori\n[6] Menu Utama User")
    input_user = int(input("Pilih Kategori: "))
    if input_user == 1:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Air Terjun':
                sum +=1
        print("="*100)
        print("\t\tJumlah Wisata untuk Kategori Air Terjun: ",sum)
        print("="*100)
        jumlah_wisata()
    elif input_user == 2:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Kebun':
                sum +=1
        print("="*100)
        print("\t\tJumlah Wisata untuk Kategori Kebun: ",sum)
        print("="*100)
        jumlah_wisata()
    elif input_user == 3:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Pantai':
                sum +=1
        print("="*100)
        print("\t\tJumlah Wisata untuk Kategori Pantai: ",sum)
        print("="*100)
        jumlah_wisata()
    elif input_user == 4:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Taman':
                sum +=1
        print("="*100)
        print("\t\tJumlah Wisata untuk Kategori Taman: ",sum)
        print("="*100)
        jumlah_wisata()
    elif input_user == 5:
        print("="*100)
        print("\t\t\t\tJumlah Wisata pada Sistem: ",len(temp))
        print("="*100)
        jumlah_wisata()
    elif input_user == 6:
        show_menu_user()
    else:
        print("Inputan Salah")
        jumlah_wisata()

def total_tiket_weekday():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    print ("----------- Berikut Daftar Kategori ----------")
    print ("[1] Air Terjun\n[2] Kebun\n[3] Pantai\n[4] Taman\n[5] Semua Kategori\n[6] Menu Utama User")
    input_user = int(input("Pilih Kategori: "))
    if input_user == 1:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Air Terjun':

                sum = sum +i['harga_tiket_weekday']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekday untuk Kategori Air Terjun Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 2:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Kebun':

                sum = sum +i['harga_tiket_weekday']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekday untuk Kategori Kebun Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 3:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Pantai':

                sum = sum +i['harga_tiket_weekday']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekday untuk Kategori Pantai Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 4:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Taman':
                sum = sum +i['harga_tiket_weekday']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekday untuk Kategori Taman Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 5:
        sum = 0
        for i in temp:
            sum = sum +i['harga_tiket_weekday']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekday untuk Semua Kategori  Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 6:
        show_menu_user()
    else:
        print("Inputan Salah")
        total_tiket_weekend()

def total_tiket_weekend():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    print ("----------- Berikut Daftar Kategori ----------")
    print ("[1] Air Terjun\n[2] Kebun\n[3] Pantai\n[4] Taman\n[5] Semua Kategori\n[6] Menu Utama User")
    input_user = int(input("Pilih Kategori: "))
    if input_user == 1:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Air Terjun':

                sum = sum +i['harga_tiket_weekend']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekend untuk Kategori Air Terjun Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 2:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Kebun':

                sum = sum +i['harga_tiket_weekend']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekend untuk Kategori Kebun Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 3:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Pantai':

                sum = sum +i['harga_tiket_weekend']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekend untuk Kategori Pantai Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 4:
        sum = 0
        for i in temp:
            if i['kategori'] == 'Taman':
                sum = sum +i['harga_tiket_weekend']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekend untuk Kategori Taman Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 5:
        sum = 0
        for i in temp:
            sum = sum +i['harga_tiket_weekend']
        print("="*100)
        print("\t\tTotal Harga Tiket Weekend untuk Semua Kategori  Rp.",sum,",-")
        print("="*100)
        total_tiket_weekend()
    elif input_user == 6:
        show_menu_user()
    else:
        print("Inputan Salah")
        total_tiket_weekend()


def mean_weekend():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    print ("----------- Berikut Daftar Kategori ----------")
    print ("[1] Air Terjun\n[2] Kebun\n[3] Pantai\n[4] Taman\n[5] Semua Kategori\n[6] Menu Utama User")
    input_user = int(input("Pilih Kategori: "))
    if input_user == 1:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Air Terjun':
                sum = sum +i['harga_tiket_weekend']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekend untuk Kategori Air Terjun Rp.",rerata,",-")
        print("="*100)
        mean_weekend()
    elif input_user == 2:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Kebun':
                sum = sum +i['harga_tiket_weekend']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekend untuk Kategori Kebun Rp.",rerata,",-")
        print("="*100)
        mean_weekend()
    elif input_user == 3:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Pantai':
                sum = sum +i['harga_tiket_weekend']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekend untuk Kategori Pantai Rp.",rerata,",-")
        print("="*100)
        mean_weekend()
    elif input_user == 4:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Taman':
                sum = sum +i['harga_tiket_weekend']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekend untuk Kategori Taman Rp.",rerata,",-")
        print("="*100)
        mean_weekend()
    elif input_user == 5:
        sum = 0
        data = []
        for i in temp:
            sum = sum +i['harga_tiket_weekend']
            data.append(sum)
            rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekend untuk Semua Kategori  Rp.",rerata,",-")
        print("="*100)
        mean_weekend()
    elif input_user == 6:
        show_menu_user()
    else:
        print("Inputan Salah")
        mean_weekend()


def mean_weekday():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    print ("----------- Berikut Daftar Kategori ----------")
    print ("[1] Air Terjun\n[2] Kebun\n[3] Pantai\n[4] Taman\n[5] Semua Kategori\n[6] Menu Utama User")
    input_user = int(input("Pilih Kategori: "))
    if input_user == 1:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Air Terjun':
                sum = sum +i['harga_tiket_weekday']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekday untuk Kategori Air Terjun Rp.",rerata,",-")
        print("="*100)
        mean_weekday()
    elif input_user == 2:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Kebun':
                sum = sum +i['harga_tiket_weekday']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekday untuk Kategori Kebun Rp.",rerata,",-")
        print("="*100)
        mean_weekday()
    elif input_user == 3:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Pantai':
                sum = sum +i['harga_tiket_weekday']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekday untuk Kategori Pantai Rp.",rerata,",-")
        print("="*100)
        mean_weekday()
    elif input_user == 4:
        sum = 0
        data = []
        for i in temp:
            if i['kategori'] == 'Taman':
                sum = sum +i['harga_tiket_weekday']
                data.append(sum)
                rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekday untuk Kategori Taman Rp.",rerata,",-")
        print("="*100)
        mean_weekday()
    elif input_user == 5:
        sum = 0
        data = []
        for i in temp:
            sum = sum +i['harga_tiket_weekday']
            data.append(sum)
            rerata = statistics.mean(data)
        print("="*100)
        print("\t\tRata-Rata Harga Tiket Weekday untuk Semua Kategori  Rp.",rerata,",-")
        print("="*100)
        mean_weekday()
    elif input_user == 6:
        show_menu_user()
    else:
        print("Inputan Salah")
        mean_weekday()

def show_menu_user():
    print ("\n")
    print ("----------- Halo Kak, Selamat Beraktivitas ----------")
    print ("[1] Melihat Wisata")
    print ("[2] Mengajukan Wisata")
    print ("[3] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")
    if menu == 1:
        show_wisata_user()
    elif menu == 2:
        insert_saran_wisata() 
    elif menu == 3:
        exit()
    else:
        print ("Salah pilih!")
def show_menu2_user():
    print ("\n")
    print ("----------- Halo Kak, Selamat Beraktivitas ----------")
    print ("[1] Menu Utama User")
    print ("[2] Jumlah Wisata Berdasarkan Kategori")
    print ("[3] Total Harga Tiket Berdasarkan Kategori Wisata pada Weekend")
    print ("[4] Total Harga Tiket Berdasarkan Kategori Wisata pada Weekday")
    print ("[5] Rata-Rata Harga Tiket Berdasarkan Kategori Wisata pada Weekend")
    print ("[6] Rata-Rata Harga Tiket Berdasarkan Kategori Wisata pada Weekday")
    print ("[7] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")
    if menu == 1:
        show_menu_user()
    elif menu == 2:
        jumlah_wisata()
    elif menu == 3:
        total_tiket_weekend()
    elif menu == 4:
        total_tiket_weekday()
    elif menu == 5:
        mean_weekend()
    elif menu == 6:
        mean_weekday()    
    elif menu == 7:
        exit()
    else:
        print ("Salah pilih!")
def show_menu_admin():
    print ("\n")
    print ("----------- Halo Admin, Selamat Beraktivitas ----------")
    print ("[1] Melihat Wisata\n[2] Melihat Saran Wisata\n[3] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")
    if menu == 1:
        show_wisata_admin()
    elif menu == 2:
        show_saran_wisata_admin()
    elif menu == 3:
        exit()
    else:
        print ("Salah pilih!")

def show_menu2_admin():
    print ("\n")
    print ("----------- Halo Admin, Selamat Beraktivitas ----------")
    print ("[1] Menu Utama Admin\n[2] Menambahkan Wisata\n[3] Mengedit Wisata\n[4] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")
    if menu ==1 :
        show_menu_admin()
    elif menu == 2:
        insert_wisata()
    elif menu == 3:
        update_wisata()
    elif menu == 4:
        exit()
    else:
        print ("Salah pilih!")

def show_menu():
    print ("\n")
    print ("----------- Selamat Datang di Nuasa.co ----------")
    print ("[1] Melihat Wisata sebagai User\n[2] Melihat Wisata Sebagai Admin\n[3] Update Password Admin\n[4] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")
    if menu == 1:
        show_menu_user()
    elif menu == 2:
        login_Admin()
    elif menu == 3:
        update_PasswordAdmin()
    elif menu == 4:
        exit()
    else:
        print ("Salah pilih!")
if __name__ == "__main__":
    show_menu()
