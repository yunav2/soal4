from flask import Flask, request, render_template, redirect, url_for
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

# Konfigurasi ke database
app.secret_key = 'jempot'
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'kar'
mysql = MySQL(app)

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/registrasi_karyawan', methods=['GET', 'POST'])
def registrasi_karyawan():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        no_telp = request.form['no_telp']
        divisi = request.form['divisi']
        jabatan = request.form['jabatan']
        gaji = request.form['gaji']
        jam = request.form['jam']
        kode = request.form['kode']

        # Simpan data ke database
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO data (nama, email, no_telp, divisi, jabatan, gaji, jam, kode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (nama, email, no_telp, divisi, jabatan, gaji, jam, kode)
        cursor.execute(sql, values)
        mysql.connection.commit()

        return redirect(url_for('landingpage'))

    return render_template('regis.html')

@app.route('/data_karyawan', methods=['GET', 'POST'])
def data_karyawan():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM data")
    data = cursor.fetchall()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True) 