"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from questions.blueprint import questions
from flask_admin import Admin 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

question_tag = db.Table('question_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True)
)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(500), nullable=False)
    tags = db.relationship('Tag', secondary=question_tag, backref=db.backref('questions', lazy="dynamic"))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Question %r>' % self.question

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.tag

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/questionUpload', methods=['POST', 'GET'])
def questionUpload():
    if request.method == 'POST':

        Question_question = request.form['question']
        Question_answer = request.form['answer']
        Question_tags = request.form['tag']
        Question_tags_list = Question_tags.replace(" ", "").split(",")

        for u_tag in Question_tags_list:
            if not bool(Tag.query.filter_by(tag=u_tag).first()):
                try:
                    db.session.add(Tag(tag=u_tag))
                    db.session.commit()
                except:
                    return 'There was an issue adding your tag'

        new_question = Question(question=Question_question, answer=Question_answer)
        try:
            for tag_name in Question_tags_list:
                tag = Tag.query.filter_by(tag=tag_name).first()
                new_question.tags.append(tag)

            db.session.add(new_question)
            
            db.session.commit()
            return redirect('/')

        except:
            return 'There was an issue adding your question'

    else:
        tasks = Question.query.order_by(Question.date_created).all()
        return render_template('questionUpload.html', questions=tasks)


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.secret_key = "123"
    app.run(host='0.0.0.0')