from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    
    # Check if data is a list
    if not isinstance(data, list):
        return jsonify({
            "is_success": False,
            "user_id": "",
        }), 400

    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",
        "numbers": numbers,
        "alphabets": alphabets,
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
