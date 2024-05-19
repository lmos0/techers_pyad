from flask import Flask,  render_template, request, redirect, url_for

app = Flask(__name__)

todos = [{'tarefa': 'levar carro pra revisão', "concluido":False}]

afazeres = {
    'tarefa':'comprar coca'
}

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods =["POST"])
def add():
    todo = request.form['todo']
    todos.append({'tarefa':todo, "concluido":False})
    return redirect(url_for("index"))

    

if __name__ == '__main__':
    app.run(debug=True)