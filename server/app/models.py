from app import db

class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(164), index=True, unique=True)

    def __repr__(self):
        return '<Questions {}>'.format(self.question)

class Responces(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    responce = db.Column(db.String(645))
    type = db.Column(db.String(1), index=True)

    def __repr__(self):
        return '<Responces {}>'.format(self.type)

class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    answer= db.Column(db.String(640))
    mthd = db.Column(db.String(1), index=True)

    def __repr__(self):
        return '<Answers {}>'.format(self.answer)