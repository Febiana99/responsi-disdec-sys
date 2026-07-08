from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        port="5433",
        database="yugabyte",
        user="yugabyte",
        password=""
    )


@app.route("/")
def home():
    return jsonify({
        "message": "REST API YugabyteDB berhasil dijalankan"
    })


@app.route("/mahasiswa")
def mahasiswa():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM mahasiswa")
    rows = cur.fetchall()

    data = []

    for row in rows:
        data.append({
            "id": row[0],
            "nama": row[1],
            "prodi": row[2]
        })

    cur.close()
    conn.close()

    return jsonify(data)


@app.route("/mata_kuliah")
def mata_kuliah():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM mata_kuliah")
    rows = cur.fetchall()

    data = []

    for row in rows:
        data.append({
            "id": row[0],
            "nama_mk": row[1],
            "sks": row[2]
        })

    cur.close()
    conn.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)