from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_miles_to_km():
    data = request.get_json()
    miles = data.get('miles')
    km = miles * 1.60934
    return jsonify({'kilometers': km})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
