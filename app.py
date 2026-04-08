from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db=SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer , primary_key=True)
    title = db.Column(db.String(200),nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}" 

with app.app_context():
    db.create_all()    



@app.route('/')
def hello_world():
    todo = Todo(title="First Todo" , desc="Start investing in stock market")
    # db.session.add(todo)
    # db.session.commit()
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('index.html', allTodo=allTodo)
    # return 'Hello,Tannu!'

@app.route('/show')
def products():
    allTodo = Todo.query.all()
    return 'This is product page'

if __name__ == "__main__":
    app.run(debug=True)

