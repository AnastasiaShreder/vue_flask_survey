from app import db
from app.models import Questions, Answers

def get_list_questions():
  list = []
  questions = Questions.query.all()
  for q in questions:
    list.append(q.question)
    # list[q.id] = q.question
  print(list)
  return list
get_list_questions()

def get_list_answers(q_id):
  list = {}
  answers = Answers.query.filter_by(question_id=q_id)
  for a in answers:
    print(a)
    list[a.answer] = a.mthd
  print(list)
  return list
get_list_answers(1)


# a = Answers(question_id="5",
# answer="Да",
# mthd="A")
# db.session.add(a)
# db.session.commit()

# a = Answers(question_id="5",
# answer="Нет",
# mthd="W")
# db.session.add(a)
# db.session.commit()

# a = Answers(question_id="5",
# answer="Скорее да, чем нет",
# mthd="A")
# db.session.add(a)
# db.session.commit()

# a = Answers(question_id="5",
# answer="Скорее нет, чем да",
# mthd="W")
# db.session.add(a)
# db.session.commit()