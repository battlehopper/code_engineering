import os
from flask import Flask, jsonify, request
import requests
from prometheus_flask_exporter import PrometheusMetrics

from tracer import configure_tracer

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Configure OpenTelemetry Tracer
configure_tracer(app)

# The service URLs will be managed by Docker Compose or Kubernetes later.
# For now, we assume they are running on these addresses.
PRODUCT_SERVICE_URL = os.environ.get("PRODUCT_SERVICE_URL", "http://localhost:5001")
PAYMENT_SERVICE_URL = os.environ.get("PAYMENT_SERVICE_URL", "http://localhost:5002")

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json()

    # Simple validation
    if not data or 'items' not in data or 'payment_details' not in data:
        return jsonify({"error": "Invalid request payload"}), 400

    # In a real app, we would first check product availability.
    # We will add this logic later. For now, let's focus on the payment flow.

    # 1. Call Payment Service
    try:
        payment_response = requests.post(
            f"{PAYMENT_SERVICE_URL}/process-payment",
            json=data['payment_details']
        )
        payment_response.raise_for_status()  # Raises an exception for 4xx/5xx errors
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Payment service is unavailable", "details": str(e)}), 503

    payment_data = payment_response.json()

    if payment_data.get("status") == "approved":
        return jsonify({"status": "Checkout successful", "payment_status": "approved"})
    else:
        return jsonify({"status": "Checkout failed", "payment_status": "denied"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
