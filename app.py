from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Path to the data file
DATA_FILE = 'data.json'

def read_data():
    """Read data from JSON file"""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading data file: {e}")
        return []

@app.route('/api', methods=['GET'])
def get_data():
    """API endpoint that returns JSON data"""
    data = read_data()
    return jsonify(data)

if __name__ == '__main__':
    # Create data.json if it doesn't exist
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
