
from logging import debug
from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypass@localhost:5432/blog_app'

app.config['SECRET_KEY'] = '\xff\x98Tq\x80\xf3\xb6\xac=\x10\xbfG\x9a\x98\x1e\xab098fi\xed\x1d@'

db = SQLAlchemy(app)


class Topic(db.Model):
    __tablename__ = 'topics'

    topic_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=255))


@app.route('/')
def display_topics():
    return render_template('home.html', topics=Topic.query.all())


@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template("topic-tasks.html", topic_id=topic_id)


@app.route('/add/topic', methods=["POST"])
def add_topic():
    # add topic functionality

    return "Topic Added Successfully"


@app.route("/add/task/<topic_id>", methods=["POST"])
def add_task(topic_id):
    # add task functionality

    return "Task Added Successfully"







if __name__ == "__main__":
    app.run(debug=True)