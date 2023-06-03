from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongodb://admin:admin@example-mongodb-0.example-mongodb-svc.default.svc.cluster.local:27017,example-mongodb-1.example-mongodb-svc.default.svc.cluster.local:27017,example-mongodb-2.example-mongodb-svc.default.svc.cluster.local:27017/test?replicaSet=example-mongodb&ssl=false&authSource=admin")

db = client.test
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))

    all_todos = todos.find()
    if not all_todos:
        all_todos = [{"content":2, "degree":4}]
    return render_template('index.html', todos=all_todos)


@app.route('/watch', methods=['GET'])
def watch():
    app.logger.info("An info message")
    with db.todos.watch() as stream:
        for change in stream:
            app.logger.info(change)
    return "watching ended"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
