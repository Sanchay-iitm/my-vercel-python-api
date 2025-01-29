from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # This will allow CORS for all origins

# Load the student data from the JSON file
with open('students.json', 'r') as f:
    students_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_student_marks():
    # Extract the names from the query parameters
    names = request.args.getlist('name')
    
    # Find the marks for the given names
    result = {"marks": []}
    for name in names:
        student = next((s for s in students_data if s['name'] == name), None)
        if student:
            result["marks"].append(student["marks"])
        else:
            result["marks"].append(None)  # In case the name isn't found
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
