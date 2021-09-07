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


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/registroCliente', methods=['GET', 'POST'])
def registroCliente():
    form = forms.registroCliente(request.form)
    if request.method == 'GET':
        return render_template('registroCliente.html', form=form)
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


@app.route('/ingresoCliente', methods=['GET', 'POST'])
def ingresoCliente():
    form = forms.ingresoCliente(request.form)
    if request.method == 'GET':
        return render_template('ingresoCliente.html', form=form)
    else:
        email = request.form['correoElectronicoCliente']
        contraseña = request.form['contraseñaCliente']
        mycursor = mydb.cursor()
        sql = "select ccnCliente, primerNombreCliente, PrimerApellidoCliente, correoElectronicoCliente, contraseñaCliente from `Engine_DB`.`tblCliente` where correoElectronicoCliente = %s"
        val = (request.form['correoElectronicoCliente'],)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()
        if email == resultado[3] and check_password_hash(resultado[4], contraseña):
            session['username'] = request.form['correoElectronicoCliente']
            session['idCliente'] = resultado[0]
            mensajeExito = 'Bienvenido {}'.format(
                resultado[1] + ' ' + resultado[2])
            flash(mensajeExito)
            return redirect(url_for('portalTransaccional'))
        else:
            mensajeError = 'Email o Contraseña incorrecta porfavor intente de nuevo'
            flash(mensajeError)
            return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional', methods=['GET', 'POST'])
def portalTransaccional():
    titulo = "Zona Transaccional"
    if 'username' and 'idCliente' in session:
        return render_template('portalTransaccional/homePortalTransaccional.html', titulo=titulo)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/cerrarSesion', methods=['GET', 'POST'])
def cerrarSesion():
    session.pop('username')
    session.pop('idCliente')
    return redirect(url_for('index'))


@app.route('/portalTransaccional/productos', methods=['GET', 'POST'])
def productos():
    titulo = "Productos"
    if 'username' and 'idCliente' in session:
        return render_template('portalTransaccional/productos.html', titulo=titulo)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/productos/dets', methods=['GET', 'POST'])
def productosDets():
    titulo = "Productos DETS"
    if 'username' and 'idCliente' in session:
        
        """cuentaContable = 21300501
        claseTasa = "V"
        tasaInt = 0.01
        tDeposito = "Dets"
        
        mycursor = mydb.cursor()
        sql = """"""insert into `Engine_DB`.`tblDepositoElectronico` (
        `depositoElectronico`,
        `codigoCuenta`,
        `ccnCliente`,
        `cuantiaMaxDeposito`,
        `claseTasaInteres`,
        `tasaInteres`,
        `frecLiqIntereses`,
        `fechaTerminacion`,
        `tipoDeposito`,
        `retencionGmf`,
        `fechaExencGmf`,
        `saldoDeposito`) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        """val = (,cuentaContable,val,claseTasa,tasaInt,tDeposito)

        mycursor.execute(sql2, val2)
        mydb.commit()
        mydb.close()"""
        return redirect(url_for('portalTransaccional'))
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))

@app.route('/ingresoEmpleado', methods=['GET', 'POST'])
def ingresoEmpleado():
    form = forms.ingresoEmpleado(request.form)
    if request.method == 'GET':
        return render_template('ingresoEmpleado.html', form=form)
    else:
        email = request.form['correoElectronicoEmpleado']
        contraseña = request.form['contraseñaEmpleado']
        mycursor = mydb.cursor()
        sql = "select ccnEmpleado, primerNombreEmpleado, PrimerApellidoEmpleado, correoElectronicoEmpleado, contraseñaEmpleado from `Engine_DB`.`tblEmpleado` where correoElectronicoEmpleado = %s"
        val = (request.form['correoElectronicoEmpleado'],)
        mycursor.execute(sql, val)
        resultado = mycursor.fetchone()
        if email == resultado[3] and check_password_hash(resultado[4], contraseña):
            session['username'] = request.form['correoElectronicoEmpleado']
            mensajeExito = 'Bienvenido {}'.format(
                resultado[1] + ' ' + resultado[2])
            flash(mensajeExito)
            return redirect(url_for('portalTransaccional'))#pendiente establecer metodos para asignacion de dashboard
        else:
            mensajeError = 'Email o Contraseña incorrecta porfavor intente de nuevo'
            flash(mensajeError)
            return redirect(url_for('ingresoEmpleado'))


@app.route('/dbEmpleados')
def dbEmpleados():
    mycursor = mydb.cursor()
    mycursor.execute("select * from `Engine_DB`.`tblEmpleado`;")
    listaEmpleados = mycursor.fetchall()
    return render_template('moduloAdminSistema/dbEmpleados.html', listaEmpleados=listaEmpleados)


@app.route('/registrarEmpleado', methods=['GET', 'POST'])
def registrarEmpleado():
    form = forms.registrarEmpleado(request.form)
    if request.method == 'GET':
        return render_template('moduloAdminSistema/registrarEmpleado.html', form=form)

    else:
        numeroidentificacion = request.form['numeroIdEmpleado']
        tipoIdentificacion = request.form['tipoId']
        fechaExpedicionIdentificacion = request.form['fechaExpIdEmpleado']
        lugarExpedicionIdentificacion = request.form['lugarExpIdEmpleado']
        primerNombre = request.form['primerNombreEmpleado']
        segundoNombre = request.form['segundoNombreEmpleado']
        primerApellido = request.form['primerApellidoEmpleado']
        segundoApellido = request.form['segundoApellidoEmpleado']
        fechaNacimiento = request.form['fechaNacimientoEmpleado']
        direccionResidencia = request.form['direccionEmpleado']
        barrioResidencia = request.form['barrioEmpleado']
        paisResidencia = request.form['idPais']
        departamentoResidencia = request.form['idDepartamento']
        municipioResidencia = request.form['idMunicipio']
        celular = request.form['celularEmpleado']
        email = request.form['correoElectronicoEmpleado']

        mycursor = mydb.cursor()
        sql = """insert into `Engine_DB`.`tblEmpleado` (
        `ccnEmpleado`,
        `numeroIdEmpleado`,
        `tipoId`,
        `fechaExpIdEmpleado`,
        `lugarExpIdEmpleado`,
        `primerNombreEmpleado`,
        `segundoNombreEmpleado`,
        `primerApellidoEmpleado`,
        `segundoApellidoEmpleado`,
        `fechaNacimientoEmpleado`,
        `direccionEmpleado`,
        `barrioEmpleado`,
        `idPais`,
        `idDepartamento`,
        `idMunicipio`,
        `celularEmpleado`,
        `correoElectronicoEmpleado`) values (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

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
                 email)

        mycursor.execute(sql, datos)
        mydb.commit()
        mydb.close()
        return render_template('index.html')


@app.route('/editarEmpleado/<int:ccnEmpleado>')
def editarEmpleado(ccnEmpleado):
    form = forms.editarEmpleado(request.form)
    mycursor = mydb.cursor()
    mycursor.execute(
        "select * from `Engine_DB`.`tblEmpleado` where ccnEmpleado = %s", (ccnEmpleado,))
    empleado = mycursor.fetchall()
    print(empleado)
    return render_template('moduloAdminSistema/editarEmpleado.html', empleado=empleado, form=form)


@app.route('/eliminarEmpleado/<int:ccnEmpleado>')
def eliminarEmpleado(ccnEmpleado):
    mycursor = mydb.cursor()
    mycursor.execute(
        "delete from `Engine_DB`.`tblEmpleado` where ccnEmpleado = %s", (ccnEmpleado,))
    mydb.commit()
    return redirect(url_for('dbEmpleados'))


@app.route('/basePortalAdminSistema')
def base():
    return render_template('moduloAdminSistema/basePortalAdminSistema.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
