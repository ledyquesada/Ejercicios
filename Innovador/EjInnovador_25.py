#Monitoreo de calidad del aire en tiempo real

from flask import Flask, request, jsonify

app = Flask(__name__)
calidad_aire = {}

@app.route('/calidad-aire', methods=['POST'])
def registrar_calidad_aire():
    datos_calidad_aire = request.json
    ubicacion = datos_calidad_aire.get('ubicacion')
    calidad = datos_calidad_aire.get('calidad')

    calidad_aire[ubicacion] = calidad
    return jsonify({'mensaje': 'Registro de calidad del aire exitoso'}), 201

@app.route('/calidad-aire', methods=['GET'])
def obtener_calidad_aire():
    ubicacion = request.args.get('ubicacion')
    if ubicacion:
        return jsonify({ubicacion: calidad_aire.get(ubicacion, 'Ubicación no encontrada')})
    else:
        return jsonify(calidad_aire)

@app.route('/recomendaciones', methods=['GET'])
def obtener_recomendaciones():
    ubicacion = request.args.get('ubicacion')
    calidad = calidad_aire.get(ubicacion)

    # Lógica para generar recomendaciones basadas en la calidad del aire
    recomendaciones = generar_recomendaciones(calidad)
    
    return jsonify({'recomendaciones': recomendaciones})

def generar_recomendaciones(calidad):
    # Lógica para generar recomendaciones
    # ...

if __name__ == '__main__':
    app.run(port=5001)
