from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
from tracer import configure_tracer
import time
import random

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Configure OpenTelemetry Tracer
configure_tracer(app)

# A simple flag to enable/disable chaos engineering practices
chaos_mode_enabled = False

# Custom metric to track chaos mode status
chaos_mode_status_metric = metrics.info('chaos_mode_status', 'Indicates if chaos mode is enabled')

@app.route('/process-payment', methods=['POST'])
def process_payment():
    global chaos_mode_enabled

    if chaos_mode_enabled:
        # 1. Inject Latency
        time.sleep(3)

        # 2. Inject Errors (50% chance of failure)
        if random.choice([True, False]):
            return jsonify({"error": "Internal Server Error: Chaos mode is active"}), 500

    data = request.get_json()
    print(f"Processing payment for: {data}")
    return jsonify({"status": "approved"}), 200

@app.route('/chaos/toggle', methods=['POST'])
def toggle_chaos():
    global chaos_mode_enabled
    chaos_mode_enabled = not chaos_mode_enabled
    status = "enabled" if chaos_mode_enabled else "disabled"

    # Update custom metric
    chaos_mode_status_metric.info({'status': status})

    return jsonify({"status": f"Chaos mode is now {status}"}), 200

@app.route('/chaos/status', methods=['GET'])
def chaos_status():
    status = "enabled" if chaos_mode_enabled else "disabled"
    return jsonify({"chaos_mode": status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
