from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')

@app.route('/usuario/<nome>')
def saudacao(nome):
    return render_template('personalizado.html', nome=nome)

@app.route('/postar', methods=['POST'])
def postar():
    data = request.json #Eu vou receber uma informação no formato de JSON (Objeto JavaScript, basicamente dicionário)
    if data:
        return jsonify({'mensagem': 'Dados recebidos com sucesso', 'dados':data}), 200
    else:
        return jsonify({'mensagem': 'Nenhum dado foi recebido'}), 400

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True, port=3200)