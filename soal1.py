activity_points = {
    "Prestasi": 30,
    "Organisasi": 10,
    "Kepanitiaan": 5,
    "Rekognisi": 2
}

total_points = 0
activities = {}

def add_activity(activity, date, category):
    global total_points
    if activity.lower() in [a.lower() for a in activities]:
        return "Kegiatan sudah pernah diinput. Tidak boleh double claim!"
    else:
        activities[activity] = [date, category, activity_points[category]]
        total_points += activity_points[category]
        return "\nKegiatan berhasil ditambahkan.\n"

while True:
    print('******* Kredit Keaktifan Mahasiswa ******\n(Student Activities Credit)')
    print("1. Menambahkan Kegiatan")
    print("2. Menampilkan Jumlah Poin")
    print("3. Keluar")
    print("-"*25)
    choice = input("Silahkan masukan pilihan Anda: ")
    
    if choice == "1":
        activity = input("Nama Kegiatan: ")
        date = input("Tanggal Kegiatan: ")
        print("Pilihan Kategori Kegiatan:")
        for category in activity_points:
            print(f" - {category}")

        valid_input = False
        while not valid_input:
            category = input("Masukan Kategori Kegiatan: ").title()
            if category in activity_points:
                valid_input = True
            else:
                print()
        print(add_activity(activity, date, category))
    elif choice == "2":
        print("\nTotal Poin:")
        print("Nama Kegiatan\tTanggal\tKategori\tPoin")
        total_points = 0
        for i, registered_activity in enumerate(activities, start=1):
            print(f"{i}. {registered_activity}", end="\t")
            print(*activities[registered_activity], sep="\t")
            total_points += activities[registered_activity][-1]
        print(f"JUMLAH TOTAL POIN\t: {total_points}")
        print()
    else:
        print("Sistem Berhenti...")
        break
