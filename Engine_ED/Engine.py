from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='123qweAs*'
app.config['MYSQL_DATABASE_DB']='DB_ENGINE_ED'
mysql.init_app(app)

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

@app.route('/moduloAdminSistema/registrarEmpleado')
def registrarEmpleado():

    #sql = "select * from tblEmpleado;"
    #conn= mysql.connect()
    #cursor=conn.cursor()
    #cursor.execute(sql)
    #con.commit()

    return render_template('moduloAdminSistema/registrarEmpleado.html')
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)
