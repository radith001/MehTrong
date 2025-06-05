from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="db",
    user="root",
    password="",
    database="perkuliahan"
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def index():
    cursor.execute("SELECT * FROM mahasiswa")
    data = cursor.fetchall()
    return render_template("index.html", mahasiswa=data)

@app.route("/create", methods=["POST"])
def create():
    nama = request.form["nama"]
    nim = request.form["nim"]
    semester = request.form["semester"]
    jurusan = request.form["jurusan"]
    cursor.execute("INSERT INTO mahasiswa (nama, nim, semester, jurusan) VALUES (%s, %s, %s, %s)", (nama, nim, semester, jurusan))
    db.commit()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    cursor.execute("DELETE FROM mahasiswa WHERE id = %s", (id,))
    db.commit()
    return redirect("/")

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "GET":
        cursor.execute("SELECT * FROM mahasiswa WHERE id = %s", (id,))
        mhs = cursor.fetchone()
        return render_template("update.html", mhs=mhs)
    else:
        nama = request.form["nama"]
        nim = request.form["nim"]
        semester = request.form["semester"]
        jurusan = request.form["jurusan"]
        cursor.execute("UPDATE mahasiswa SET nama=%s, nim=%s, semester=%s, jurusan=%s WHERE id=%s",
                       (nama, nim, semester, jurusan, id))
        db.commit()
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


