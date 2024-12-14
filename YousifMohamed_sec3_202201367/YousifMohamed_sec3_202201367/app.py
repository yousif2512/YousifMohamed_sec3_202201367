from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

tasks = []
def add_task(task):
    tasks.append(task)
def get_tasks():
    return tasks
@app.route('/')
def index():
    return render_template('index.html', tasks=get_tasks())
@app.route('/add-task', methods=['POST'])
def add_task_route():
    task = request.form.get('task')
    if task:
        add_task(task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
