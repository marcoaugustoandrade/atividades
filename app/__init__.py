from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    a = ['Semana ADS', 'Semana de Tecnologia', 'EIIFRO']
    return render_template("index.html", atividades=a)
