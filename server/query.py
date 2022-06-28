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
# get_list_questions()

def get_list_answers():
  list_all = []
  questions = Questions.query.all()
  for q in questions:
    list = {}
    answers = Answers.query.filter_by(question_id=q.id)
    for a in answers:
      # print(a)
      list[a.answer] = a.mthd
    list_all.append(list)
  print(list_all)
  return list_all
# get_list_answers()

def get_answers(q_id):
  list = {}
  answers = Answers.query.filter_by(question_id=q_id)
  for a in answers:
    print(a)
    list[a.answer] = a.mthd
  print(list)
  return list

# q = Questions(id = "2", question = "У всех участников высокий уровень квалификации?")
# db.session.query(Questions).delete()
# a = Answers(question_id="5",
# answer="Да",
# mthd="A")

# a = Answers(question_id="10",
# answer="Задачи, связанные с документацией, будут выполняться в последнюю очередь",
# mthd="F")
# db.session.add(a)
# db.session.commit()
# a = Answers(question_id="10",
# answer="Полноценная документация не предусмотрена",
# mthd="S")
# db.session.add(a)
# db.session.commit()
# a = Answers(question_id="10",
# answer="Необходимо наличие документации одного из видов",
# mthd="D")
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