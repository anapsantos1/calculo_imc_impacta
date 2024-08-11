from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = 'Magreza'
    elif 18.5 <= imc < 24.9:
        categoria = 'Normal'
    elif 24.9 <= imc < 30:
        categoria = 'Sobrepeso'
    else:
        categoria = 'Obesidade'
    return imc, categoria

@app.route('/calcular_imc', methods=['POST'])
def imc():
    data = request.json
    peso = float(data.get('peso'))
    altura = float(data.get('altura'))
    if peso and altura:
        imc, categoria = calcular_imc(peso, altura)
        return jsonify({'imc': imc, 'categoria': categoria})
    else:
        return jsonify({'error': 'Peso e altura são necessários!'}), 400

if __name__ == '__main__':
    app.run(debug=True)
