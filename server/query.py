from app import db
from app.models import Questions, Responces

def get_list_questions():
  list = {}
  list_a = {}
  list_q = {}
  questions = Questions.query.all()
  answers = Responces.query.all()
  print(answers)
  for q in questions:
    a = Responces.query.filter_by(question_id=q.id)
    list_a[a.responce] = a.type
    list[q.question] = list_a
    list_q[q.id] = q.question
  # print(list.items())
  return list
get_list_questions()