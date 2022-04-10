from flask import jsonify
from flask_cors import CORS
from app import app
import query

# enable CORS
CORS(app)

# sanity check route
@app.route('/ping')
def ping():
    return jsonify(success=True)

@app.route('/quiz', methods=['GET'])
def get_quiz():
    questions = query.get_list_questions()
    return jsonify(questions)

if __name__ == '__main__':
    app.run()