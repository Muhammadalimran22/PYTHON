from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data sementara (disimpan di memori)
daftar_mahasiswa = []

# Halaman utama
@app.route('/')
def index():
    return render_template('index.html', daftar_mahasiswa=daftar_mahasiswa)

# Tambah mahasiswa
@app.route('/tambah', methods=['POST'])
def tambah():
    nama = request.form['nama']
    nim = request.form['nim']
    nilai = int(request.form['nilai'])

    daftar_mahasiswa.append({'nama': nama, 'nim': nim, 'nilai': nilai})
    return redirect(url_for('index'))

# Hapus mahasiswa
@app.route('/hapus/<nim>')
def hapus(nim):
    global daftar_mahasiswa
    daftar_mahasiswa = [m for m in daftar_mahasiswa if m['nim'] != nim]
    return redirect(url_for('index'))

# Edit mahasiswa
@app.route('/edit/<nim>', methods=['GET', 'POST'])
def edit(nim):
    mahasiswa = next((m for m in daftar_mahasiswa if m['nim'] == nim), None)
    if request.method == 'POST':
        mahasiswa['nama'] = request.form['nama']
        mahasiswa['nilai'] = int(request.form['nilai'])
        return redirect(url_for('index'))
    return render_template('edit.html', mahasiswa=mahasiswa)

if __name__ == '__main__':
    app.run(debug=True)
