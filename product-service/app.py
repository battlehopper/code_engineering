from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

from tracer import configure_tracer

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Configure OpenTelemetry Tracer
configure_tracer(app)

products = [
    {"id": 1, "name": "Laptop Gamer", "price": 8500, "stock": 15},
    {"id": 2, "name": "Mouse Sem Fio", "price": 250, "stock": 50},
    {"id": 3, "name": "Teclado Mecânico", "price": 450, "stock": 30},
    {"id": 4, "name": "Monitor Ultrawide", "price": 3200, "stock": 10},
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
