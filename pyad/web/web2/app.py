from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuario/<nome>')
def usuario(nome):
    return render_template('usuario.html', nome=nome)

@app.route('/post-example', methods=['POST'])
def post_example():
    data = request.json  # Assuming the data is sent in JSON format
    # Process the received data
    if data:
        return jsonify({'message': 'Data received successfully', 'data': data}), 200
    else:
        return jsonify({'message': 'No data received'}), 400

if __name__ == '__main__':
    app.run(debug=True)
