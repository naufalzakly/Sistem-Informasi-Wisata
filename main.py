import getpass
import json

data_wisata = "data_wisata.json"
data_admin = "data_admin.json"
data_saran_wisata = "data_saran_wisata.json"

def login_Admin():
    with open (data_admin, "r") as data:
        isi_data = json.load(data)
    username = input("Masukan Username Anda: ")
    password = str(getpass.getpass("Masukan Password: "))
    ulang = 0
    while ulang <= 2 and username != isi_data['username'] and password != isi_data['password']:
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

def insert_wisata():
    temp = {}
    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    
    nama = input("Masukan nama wisata: ")
    alamat = input("Masukan alamat wisata: ")
    harga_tiket_weekday = int(input("Masukan harga saaat weekday: "))
    harga_tiket_weekend= int(input("Masukan harga saaat weekend: "))
    temp.append({
        'nama':nama,
        'alamat':alamat,
        'harga_tiket_weekday':harga_tiket_weekday,
        'harga_tiket_weekend':harga_tiket_weekend
    })

    with open (data_wisata, "w") as data_file:
        dataa = json.dumps(temp, indent=4)
        data_file.write(dataa)
        print("Berhasil ditambahkan")

def insert_saran_wisata():
    temp = {}
    with open (data_saran_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    
    nama = input("Masukan nama wisata: ")
    alamat = input("Masukan alamat wisata: ")
    harga_tiket_weekday = int(input("Masukan harga saaat weekday: "))
    harga_tiket_weekend= int(input("Masukan harga saaat weekend: "))
    temp.append({
        'nama':nama,
        'alamat':alamat,
        'harga_tiket_weekday':harga_tiket_weekday,
        'harga_tiket_weekend':harga_tiket_weekend
    })

    with open (data_wisata, "w") as data_file:
        dataa = json.dumps(temp, indent=4)
        data_file.write(dataa)
        print("Berhasil ditambahkan")


def show_wisata():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    
    print('Nama','\t\tAlamat','\t\tHarga Tiket Weekday','\tHarga Tiket Weekend')
    print('='*150)
    for i in temp:
        print(f"{i['nama']}\t\t{i['alamat']}\t{i['harga_tiket_weekday']}\t\t{i['harga_tiket_weekend']}")
def show_saran_wisata():
    temp = []

    with open (data_saran_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    
    print('Nama','\t\tAlamat','\t\t\tHarga Tiket Weekday','\tHarga Tiket Weekend')
    print('='*150)
    for i in temp:
        print(f"{i['nama']}\t\t{i['alamat']}\t{i['harga_tiket_weekday']}\t\t\t{i['harga_tiket_weekend']}")

def total_tiket_weekday():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    sum = 0
    for i in temp:
        sum = sum +i['harga_tiket_weekday']
        print("Total Harga Tiket Weekday",sum)

def total_tiket_weekend():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    sum = 0
    for i in temp:
        sum = sum +i['harga_tiket_weekend']
        print("Total Harga Tiket Weekend",sum)
def total_tiket():
    temp = []

    with open (data_wisata, "r") as data:
        isi_data = json.load(data)
    temp = isi_data
    sum = 0
    for i in temp:
        sum = sum +i['harga_tiket_weekend']+i['harga_tiket_weekend']
        print("Total Harga Tiket Weekend dan weekday",sum)


def show_menu_user():
    print ("\n")
    print ("----------- Halo Kak, Selamat Beraktivitas ----------")
    print ("[1] Melihat Wisata")
    print ("[2] Mengajukan Wisata")
    print ("[3] Total Harga Tiket Masuk Weekday Semua Wisata")
    print ("[4] Total Harga Tiket Masuk Weekend Semua Wisata")
    print ("[5] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")

    if menu == 1:
        show_wisata()
    elif menu == 2:
        show_saran_wisata()
    elif menu == 3:
        total_tiket_weekday()
    elif menu == 4:
        total_tiket_weekend()
    elif menu == 5:
        exit()
    else:
        print ("Salah pilih!")

def show_menu_admin():
    print ("\n")
    print ("----------- Halo Admin, Selamat Beraktivitas ----------")
    print ("[1] Melihat Wisata")
    print ("[2] Menambahkan Wisata")
    print ("[3] Melihat Saran Wisata")
    print ("[4] Exit")
    menu = int(input("PILIH MENU: "))
    print ("\n")

    if menu == 1:
        show_wisata()
    elif menu == 2:
        insert_wisata()
    elif menu == 3:
        exit()
    else:
        print ("Salah pilih!")

def show_menu():
    print ("\n")
    print ("----------- Selamat Datang di Nuasa.co ----------")
    print ("[1] Melihat Wisata sebagai User")
    print ("[2] Melihat Wisata Sebagai Admin")
    print ("[3] Update Password Admin")
    print ("[4] Exit")
    
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

    while(True):
        show_menu()