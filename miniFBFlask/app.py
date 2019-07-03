from flask import Flask, render_template, request
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def mini_fb():
    get_user_data()
    return render_template("index.html")

def get_user_data():
    name = request.args.get('name')
    
    id = request.args.get('ID')
    age = request.args.get('age')
    income = request.args.get('income')
    print(name, id, age, income)

if __name__ == '__main__':
    app.run()
