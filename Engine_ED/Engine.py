from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import session
from flask import flash
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_wtf import CSRFProtect
from db import *
import forms


app = Flask(__name__)
app.config["SECRET_KEY"] = 'hardsecretkey'
csfr = CSRFProtect(app)


@app.errorhandler(404)
def paginaNoEncontrada(e):
    pass


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ingresoCliente', methods = ['GET','POST'])
def ingresoCliente():
    form = forms.ingresoCliente(request.form)
    if request.method == 'POST':
        email = request.form['correoElectronicoCliente']
        contraseña = request.form['contraseñaCliente']
        mycursor = mydb.cursor()
        sql = "select ccnCliente, primerNombreCliente, PrimerApellidoCliente, correoElectronicoCliente, contraseñaCliente from `Engine_DB`.`tblCliente` where correoElectronicoCliente = %s"
        val = (request.form['correoElectronicoCliente'],)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()
        print(resultado)
#asynawait in javascrip para python
        if email == resultado[3] and check_password_hash(resultado[4], contraseña):
            session['username'] = request.form['correoElectronicoCliente']
            mensajeExito = 'Bienvenido {}'.format(resultado[1] + ' ' + resultado[2])
            flash(mensajeExito)
            return redirect(url_for('portalTransaccional'))
        else:
            mensajeError = 'Email o Contraseña incorrecta porfavor intente de nuevo'
            flash(mensajeError)
            return redirect(url_for('ingresoCliente'))
    else:
        return render_template('ingresoCliente.html', form = form)

@app.route('/portalTransaccional', methods = ['GET','POST'])
def portalTransaccional():
    #Identificar si el usuario esta conectado atravez de sesiones
    if 'username' in session:
        return render_template('portalTransaccional/homePortalTransaccional.html')


@app.route('/cerrarSesion', methods = ['GET','POST'])
def cerrarSesion():
    session.pop('username')
    return redirect(url_for('index'))
    

@app.route('/registroCliente', methods = ['GET','POST'])
def registroCliente():
    form = forms.registroCliente(request.form)
    if request.method == 'GET':
        return render_template('registroCliente.html', form = form)
    else:
        numeroidentificacion = request.form['numeroIdCliente']
        tipoIdentificacion = request.form['tipoId']
        fechaExpedicionIdentificacion = request.form['fechaExpIdCliente']
        lugarExpedicionIdentificacion = request.form['lugarExpIdCliente']
        primerNombre = request.form['primerNombreCliente']
        segundoNombre = request.form['segundoNombreCliente']
        primerApellido = request.form['primerApellidoCliente']
        segundoApellido = request.form['segundoApellidoCliente']
        fechaNacimiento = request.form['fechaNacimientoCliente']
        direccionResidencia = request.form['direccionCliente']
        barrioResidencia = request.form['barrioCliente']
        paisResidencia = request.form['idPais']
        departamentoResidencia = request.form['idDepartamento']
        municipioResidencia = request.form['idMunicipio']
        celular = request.form['celularCliente']
        email = request.form['correoElectronicoCliente']
        contraseña = generate_password_hash(request.form['contraseñaCliente'])

        mycursor = mydb.cursor()
        sql = """insert into `Engine_DB`.`tblCliente` (
        `ccnCliente`,
        `numeroIdCliente`,
        `tipoId`,
        `fechaExpIdCliente`,
        `lugarExpIdCliente`,
        `primerNombreCliente`,
        `segundoNombreCliente`,
        `primerApellidoCliente`,
        `segundoApellidoCliente`,
        `fechaNacimientoCliente`,
        `direccionCliente`,
        `barrioCliente`,
        `idPais`,
        `idDepartamento`,
        `idMunicipio`,
        `celularCliente`,
        `correoElectronicoCliente`,
        `contraseñaCliente`) values (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        datos = (numeroidentificacion,
        tipoIdentificacion,
        fechaExpedicionIdentificacion,
        lugarExpedicionIdentificacion,
        primerNombre,
        segundoNombre,
        primerApellido,
        segundoApellido,
        fechaNacimiento,
        direccionResidencia,
        barrioResidencia,
        paisResidencia,
        departamentoResidencia,
        municipioResidencia,
        celular,
        email,
        contraseña)

        mycursor.execute(sql, datos)
        mydb.commit()
        mydb.close()

        return redirect(url_for('ingresoCliente'))


if __name__ == '__main__':
    app.run(debug=True, port=8080)
