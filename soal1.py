poinKeaktifan = {
    "Prestasi": 30,
    "Organisasi": 10,
    "Kepanitiaan": 5,
    "Rekognisi": 2
}

print("*"*6,"Kredit Keaktifan Mahasiswa","*"*6)
print("(Students Activities Credit)")
print("1. Menambahkan Kegiatan\n2. Menampilkan Jumlah Poin\n3. Keluar")
print("-"*30)
pilihan = int(input("Silahkan masukan pilihan yang Anda: "))

while pilihan == True:
    if pilihan == 1:
        kegiatan = str(input("Nama Kegiatan: "))
        tanggal = str(input("Tanggal Kegiatan: "))
        print("Pilihan Kategori Kegiatan:")
        print(poinKeaktifan)
        pilihanKategori = str(input("Masukkan Kategori Kegiatan: "))
        print("Kategori berhasil ditambahkan.")

    if pilihan == 2:
        print()
        print("-"*30)
        print("Nama Kegiatan     ","Tanggal      ","Kategori      ","Poin      ")
        
        
    if pilihan == 3:
        print("Sistem Berhenti...")
        break







#cadangan
# activity_data = {}
# activity_points = {
#     "Prestasi": 30,
#     "Organisasi": 10,
#     "Kepanitiaan": 5,
#     "Rekognisi": 2
# }

# def add_activity(date, category, points):
#   if date in activity_data:
#     print("Kegiatan sudah pernah diinput. Tidak boleh double claim!")
#   else:
#     activity_data[date] = (category, points)

# print("*"*6,"Kredit Keaktifan Mahasiswa","*"*6)
# print("(Students Activities Credit)")
# print("1. Menambahkan Kegiatan\n2. Menampilkan Jumlah Poin\n3. Keluar")
# print("-"*30)

# while True:
#   add_activity_choice = int(input("Silahkan masukkan pilihan Anda: "))
#   if add_activity_choice == 1:
#     activity_name = str(input("Nama Kegiatan: "))
#     date = input("Tanggal kegiatan: ")
#     print("Kategori kegiatan:")
#     for category in activity_points:
#         print(f" - {category}")
#         category = input("Pilih kategori kegiatan: ")

  
#   if add_activity_choice == 3:
#     print("Sistem Berhenti...")
#     break

#   date = input("Tanggal kegiatan: ")
#   print("Kategori kegiatan:")
#   for category in activity_points:
#     print(f" - {category}")
#   category = input("Pilih kategori kegiatan: ")

#   # Menambahkan data kegiatan ke dictionary
#   points = activity_points[category]
#   add_activity(date, category, points)

# #jumlah total poin
# total_points = sum([points for _, (category, points) in activity_data.items()])
# print(f"JUMLAH POIN TOTAL POIN   : {total_points}")