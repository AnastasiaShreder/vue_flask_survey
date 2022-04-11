from flask import jsonify
from flask_cors import CORS
from flask import request as flask_request
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

def get_responces(num, flask_request_local: flask_request):
    answers = query.get_answers(num)
    return answers

# @app.route('/answers', methods=['POST'])
# def get_answers():
#     print(dict(flask_request.form.items()))
#     num = flask_request.form.get('number')
#     print(num)
#     answers = get_responces(num, flask_request_local=flask_request)
#     return jsonify(answers)

@app.route('/list_answers', methods=['GET'])
def get_list():
    answers = query.get_list_answers()
    # print(answers)
    return jsonify(answers)

if __name__ == '__main__':
    app.run()