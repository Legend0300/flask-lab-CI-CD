from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Home route - render the home HTML template."""
    return render_template('home.html'), 200


@app.route('/health')
def health():
    """Health route - returns service status as JSON."""
    print("route working")
    return jsonify(status='ok'), 200


@app.route('/data')
def data():
    """Data route - returns dummy JSON data."""
    dummy = {
        'items': [
            {'id': 1, 'name': 'Alice'},
            {'id': 2, 'name': 'Bob'},
            {'id': 3, 'name': 'Carol'},
            {'id': 4, 'name': 'David'},
        ],
        'count': 3
    }
    # If the client accepts HTML, render the template. Otherwise return JSON.
    return render_template('data.html', data=dummy), 200


if __name__ == '__main__':
    # When run directly, start the dev server on all interfaces.
    app.run(host='0.0.0.0', port=5000)