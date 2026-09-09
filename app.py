import json
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ── Helper ──────────────────────────────────────────────────────────────────
def load_data(filename):
    filepath = os.path.join(os.path.dirname(__file__), 'data', filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

# ── Page Routes (5 halaman) ─────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eksplorasi')
def explore():
    return render_template('explore.html')

@app.route('/matematika')
def mathematics():
    math_data = load_data('mathematics.json')
    return render_template('mathematics.html', math_data=math_data)

@app.route('/budaya')
def culture():
    culture_data = load_data('culture.json')
    return render_template('culture.html', culture_data=culture_data)

@app.route('/tentang')
def about():
    return render_template('about.html')

# ── API Routes ───────────────────────────────────────────────────────────────
@app.route('/api/house_parts')
def get_house_parts():
    """Full house parts data for 3D hotspot system."""
    return jsonify(load_data('house_parts.json'))

@app.route('/api/house_parts/<part_id>')
def get_house_part(part_id):
    """Single part data."""
    data = load_data('house_parts.json')
    part = data.get('parts', {}).get(part_id)
    if not part:
        return jsonify({'error': 'Bagian tidak ditemukan'}), 404
    return jsonify(part)

@app.route('/api/mathematics')
def get_all_mathematics():
    return jsonify(load_data('mathematics.json'))

@app.route('/api/culture')
def get_all_culture():
    return jsonify(load_data('culture.json'))

# Legacy hotspot endpoint (dipakai hotspot.js)
@app.route('/api/hotspot/<part_id>')
def get_hotspot_data(part_id):
    data = load_data('house_parts.json')
    part = data.get('parts', {}).get(part_id)
    if not part:
        return jsonify({'error': 'Bagian tidak ditemukan'}), 404
    return jsonify(part)

# ── Run ──────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
