
from logging import debug
from turtle import title
from flask import Flask, render_template, request, flash , redirect , url_for

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypass@localhost:5432/blog_app'

app.config['SECRET_KEY'] = '\xff\x98Tq\x80\xf3\xb6\xac=\x10\xbfG\x9a\x98\x1e\xab098fi\xed\x1d@'

db = SQLAlchemy(app)


# imolementation of dynamic tasks first step to create class

     

class Topic(db.Model):
    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255))


class Task(db.Model):
     __tablename__ = 'tasks'
     
     task_id = db.Column(db.Integer, primary_key=True)
     topic_id = db.Column(db.Integer, db.ForeignKey('topics.topic_id'))
     description = db.Column(db.String(length=255))
     
     topic = db.relationship('Topic')

@app.route('/')
def display_topics():
    return render_template('home.html', topics=Topic.query.all())


@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template("topic-tasks.html", topic=Topic.query.filter_by(topic_id=topic_id).first(),
                           tasks= Task.query.filter_by(topic_id=topic_id))


@app.route('/add/topic', methods=["POST"])
def add_topic():
    # add topic functionality
    if not request.form["topic-title"]:
        flash('Enter title for your new topic', 'orange')
    else:
        # storing topick user entered
        topic = Topic(title=request.form['topic-title'])
        # adding to db
        db.session.add(topic)
        db.session.commit()
        flash('Topic Added succesfully', 'tomato')
        
    return redirect(url_for('display_topics'))


@app.route("/add/task/<topic_id>", methods=["POST"])
def add_task(topic_id):
    # add task functionality
    if not request.form['task-description']:
        flash('Enter a description for new task', 'yellow')
    else:
        task = Task(description=request.form["task-description"], topic_id = topic_id)
        db.session.add(task)
        db.session.commit()
        flash('Task Added succesfully', 'lawngreen')
        
    return redirect(url_for('display_tasks', topic_id=topic_id))







if __name__ == "__main__":
    app.run(debug=True)