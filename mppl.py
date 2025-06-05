import mysql.connector

# Koneksi ke database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # kosongkan jika default XAMPP
    database="mppl"
)

cursor = db.cursor()

# Fungsi CRUD Mahasiswa
def tambah_mahasiswa(nama, nim, jurusan):
    sql = "INSERT INTO mahasiswa (nama, nim, jurusan) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nama, nim, jurusan))
    db.commit()
    print("Mahasiswa berhasil ditambahkan!")

def lihat_mahasiswa():
    cursor.execute("SELECT * FROM mahasiswa")
    for row in cursor.fetchall():
        print(row)

def update_mahasiswa(id, nama, nim, jurusan):
    sql = "UPDATE mahasiswa SET nama=%s, nim=%s, jurusan=%s WHERE id=%s"
    cursor.execute(sql, (nama, nim, jurusan, id ))
    db.commit()
    print("Mahasiswa berhasil diupdate!")

def hapus_mahasiswa(id):
    sql = "DELETE FROM mahasiswa WHERE id=%s"
    cursor.execute(sql, (id,))
    db.commit()
    print("Mahasiswa berhasil dihapus!")

# Menu Sederhana
while True:
    print("\n--- MENU MAHASISWA ---")
    print("1. Tambah Mahasiswa")
    print("2. Lihat Mahasiswa")
    print("3. Update Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")
    pilihan = input("Pilih: ")

    if pilihan == "1":
        nama = input("Nama: ")
        nim = input("NIM: ")
        jurusan = input("Jurusan: ")
        tambah_mahasiswa(nama, nim, jurusan)
    elif pilihan == "2":
        lihat_mahasiswa()
    elif pilihan == "3":
        id = input("ID mahasiswa yang ingin diupdate: ")
        nama = input("Nama baru: ")
        nim = input("NIM baru: ")
        jurusan = input("Jurusan baru: ")
        update_mahasiswa(id, nama, nim, jurusan)
    elif pilihan == "4":
        id = input("ID mahasiswa yang ingin dihapus: ")
        hapus_mahasiswa(id)
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid.")
