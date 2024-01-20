 # Registro de datos ambientales

from flask import Flask, request, jsonify

app = Flask(__name__)
registros_ambientales = []

@app.route('/registro', methods=['POST'])
def registrar_datos_ambientales():
    nuevo_registro = request.json
    registros_ambientales.append(nuevo_registro)
    return jsonify({'mensaje': 'Registro exitoso'}), 201

@app.route('/registro', methods=['GET'])
def obtener_registros_ambientales():
    fecha = request.args.get('fecha')
    contaminante = request.args.get('contaminante')
    
    if fecha and contaminante:
        resultados = [registro for registro in registros_ambientales if registro['fecha'] == fecha and registro['contaminante'] == contaminante]
    else:
        resultados = registros_ambientales

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(port=5000)
