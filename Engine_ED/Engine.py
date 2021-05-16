from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registroCliente')
def registroCliente():
    return render_template('registroCliente.html')

@app.route('/loginCliente')
def loginCliente():
    return render_template('loginCliente.html')

@app.route('/baseModulos')
def baseModulos():
    return render_template('baseModulos.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
