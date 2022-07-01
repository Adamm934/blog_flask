
from flask import Flask, render_template

app = Flask(__name__)



# 
@app.route('/')
def display_things():
    return render_template('home.html')


# traces topics by theyre id
# based on topic id relevant tasks will be shown
# topic id on the left comes from from template and value comes from parameter
@app.route('/topic/<topic_id>')
def display_tasks(topic_id):
    return render_template('topic-tasks.html', topic_id = topic_id)
    
    
# handles addition of the new tasks
# forms gets passed aka / / topic
@app.route('/add/topic', methods=["POST"])
def add_topics():
    
    
    
    return 'topic added'


# view functions to add additions of the task

@app.route("/add/task/<topic_id>", methods=['POST'])
def add_task(topic_id):
    
    
    return 'Task added succesfully'






if __name__ == "__main__":
    app.run(debug=True)