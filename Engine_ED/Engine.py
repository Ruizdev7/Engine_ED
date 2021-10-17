from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import session
from flask import Response
from flask import flash
from flask import jsonify
from flask import json
from datetime import datetime
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


@app.route('/registroCliente', methods=['GET','POST'])
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

        mydb.connect()
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

        datos = (
            numeroidentificacion,
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
        print(mycursor.rowcount, "record(s) affected")
        mydb.commit()
        mydb.close()

        return redirect(url_for('ingresoCliente'))


@app.route('/ingresoCliente', methods=['GET','POST'])
def ingresoCliente():
    form = forms.ingresoCliente(request.form)
    if request.method == 'GET':
        return render_template('ingresoCliente.html', form=form)
    else:
        email = request.form['correoElectronicoCliente']
        contraseña = request.form['contraseñaCliente']
        mydb.connect()
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


@app.route('/portalTransaccional', methods=['GET','POST'])
def portalTransaccional():
    titulo = "Zona Transaccional"
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            try:
                mydb.connect()
                mycursor = mydb.cursor()
                sql = "select * from tblDepositoElectronico where ccnCliente = %s"
                ccnCliente = session['idCliente']
                mycursor.execute(sql, (ccnCliente,))
                depositoCliente = mycursor.fetchone()
                print(depositoCliente)
            except Exception as e:
                print(e)
            finally:
                mycursor.close()
                mydb.close()
                return render_template('portalTransaccional/homePortalTransaccional.html', titulo=titulo, usuario=usuario, depositoCliente=depositoCliente)
        else:
            return render_template('portalTransaccional/homePortalTransaccional.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/cerrarSesion', methods=['GET','POST'])
def cerrarSesion():
    session.pop('username')
    session.pop('idCliente')
    return redirect(url_for('index'))


@app.route('/portalTransaccional/productos', methods=['GET','POST'])
def productos():
    titulo = "Productos"
    mydb.connect()
    mycursor = mydb.cursor()
    sql = "select ccnCliente, celularCliente from `Engine_DB`.`tblCliente` where ccnCliente = %s"
    val = (session['idCliente'],)
    mycursor.execute(sql, val)
    cliente = mycursor.fetchone()
    print(cliente)
    mydb.close()
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        return render_template('portalTransaccional/productos.html', titulo=titulo, cliente=cliente, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/eleccionProducto', methods=['GET','POST'])
def eleccionProducto():
    if 'username' and 'idCliente' in session:
        print(request.method)
        if request.method == 'POST':
            depositoElectronico = request.form['depositoElectronico']
            codigoCuenta = request.form['codigoCuenta']
            ccnCliente = request.form['ccnCliente']
            cuantiaMaxDeposito = request.form['cuantiaMaxDeposito']
            claseTasaInteres = request.form['claseTasaInteres']
            tasaInteres = request.form['tasaInteres']
            frecLiqIntereses = request.form['frecLiqIntereses']
            tipoDeposito = request.form['tipoDeposito']
            saldoDeposito = 0

            print(depositoElectronico, codigoCuenta, ccnCliente, cuantiaMaxDeposito, claseTasaInteres, tasaInteres, frecLiqIntereses, tipoDeposito)
            mydb.connect()
            mycursor = mydb.cursor()
            sql = """insert into `Engine_DB`.`tblDepositoElectronico`(
                `depositoElectronico`,
                `codigoCuenta`,
                `ccnCliente`,
                `cuantiaMaxDeposito`,
                `claseTasaInteres`,
                `tasaInteres`,
                `frecLiqIntereses`,
                `tipoDeposito`,
                `saldoDeposito`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) on duplicate key update
                `depositoElectronico` = %s,
                `codigoCuenta` = %s,
                `ccnCliente` = %s,
                `cuantiaMaxDeposito` = %s,
                `claseTasaInteres` = %s,
                `tasaInteres` = %s,
                `frecLiqIntereses` = %s,
                `tipoDeposito` = %s;"""

            datos = (
                depositoElectronico,
                codigoCuenta,
                ccnCliente,
                cuantiaMaxDeposito,
                claseTasaInteres,
                tasaInteres,
                frecLiqIntereses,
                tipoDeposito,
                saldoDeposito,
                depositoElectronico,
                codigoCuenta,
                ccnCliente,
                cuantiaMaxDeposito,
                claseTasaInteres,
                tasaInteres,
                frecLiqIntereses,
                tipoDeposito)
                
            mycursor.execute(sql, datos)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")

            return redirect(url_for('portalTransaccional'))


@app.route('/portalTransaccional/listaDepositosInscritos', methods=['GET','POST'])
def listaDepositosInscritos():
    titulo = "Lista Depositos Inscritos"
    form = forms.inscribirDepositos(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            try:
                mydb.connect()
                mycursor = mydb.cursor()
                sql = "select * from tblDepositosInscritos where filtroLista = %s"
                filtro = (session['username'],)
                mycursor.execute(sql, filtro)
                data = tuple(mycursor.fetchall())
                print(data)
            except Exception as e:
                print(e)
            finally:
                mycursor.close()
                mydb.close()
                return render_template('portalTransaccional/listaDepositosInscritos.html', titulo=titulo, usuario=usuario, data=data, form=form)
        else:
            return render_template('portalTransaccional/listaDepositosInscritos.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/inscribirDepositosElectronicos', methods=['GET','POST'])
def inscribirDepositosElectronicos():
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            return render_template('portalTransaccional/inscribirDepositosElectronicos.html', usuario=usuario)
        else:
            filtroLista = session['username']
            tipoDeposito = request.form['tipoDeposito']
            depositoElectronico = request.form['depositoElectronico']
            nombrePersonalizado = request.form['nombrePersonalizado']
            tipoId = request.form['tipoId']
            numeroIdCliente = request.form['numeroIdCliente']

            print(filtroLista, tipoDeposito, depositoElectronico, nombrePersonalizado, tipoId, numeroIdCliente)

            mydb.connect()
            mycursor = mydb.cursor()
            sql = """insert into `Engine_DB`.`tblDepositosInscritos`(
                `ccnDepositosInscritos`,
                `filtroLista`,
                `tipoDeposito`,
                `depositoElectronico`,
                `nombrePersonalizado`,
                `tipoId`,
                `numeroIdCliente`) VALUES (null, %s, %s, %s, %s, %s, %s);"""

            datos = (
                filtroLista,
                tipoDeposito,
                depositoElectronico,
                nombrePersonalizado,
                tipoId,
                numeroIdCliente)
                
            mycursor.execute(sql, datos)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")

            return redirect(url_for('listaDepositosInscritos'))
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/editarDepositoInscrito/<int:ccnDepositosInscritos>')
def editarDepositoInscrito(ccnDepositosInscritos):
    titulo = "Editar Deposito Inscrito"
    form = forms.inscribirDepositos(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            try:
                mydb.connect()
                mycursor = mydb.cursor()
                sql = "select * from tblDepositosInscritos where ccnDepositosInscritos = %s"
                ccnDepositosInscritos = (ccnDepositosInscritos,)
                mycursor.execute(sql, ccnDepositosInscritos)
                data2 = mycursor.fetchone()
                print(data)
            except Exception as e:
                print(e)
            finally:
                mycursor.close()
                mydb.close()
                return render_template('portalTransaccional/editarDepositosInscritos.html', titulo=titulo, usuario=usuario, data2=data2, form=form)
        else:
            return render_template('portalTransaccional/listaDepositosInscritos.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/procesoEdicionDepositoElectronico', methods=['GET','POST'])
def procesoEdicionDepositoElectronico():
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'POST':
            ccnDepositoInscrito = request.form['ccnDepositoInscrito']
            filtroLista = session['username']
            tipoDeposito = request.form['tipoDeposito']
            depositoElectronico = request.form['depositoElectronico']
            nombrePersonalizado = request.form['nombrePersonalizado']
            tipoId = request.form['tipoId']
            numeroIdCliente = request.form['numeroIdCliente']

            print(ccnDepositoInscrito, filtroLista, tipoDeposito, depositoElectronico, nombrePersonalizado, tipoId, numeroIdCliente)

            mydb.connect()
            mycursor = mydb.cursor()
            sql = """update tblDepositosInscritos set 
                filtroLista = %s,
                tipoDeposito = %s,
                depositoElectronico = %s,
                nombrePersonalizado = %s,
                tipoId = %s,
                numeroIdCliente = %s where ccnDepositosInscritos = %s;"""

            datos = (
                filtroLista,
                tipoDeposito,
                depositoElectronico,
                nombrePersonalizado,
                tipoId,
                numeroIdCliente,
                ccnDepositoInscrito)
                
            mycursor.execute(sql, datos)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")

            return redirect(url_for('listaDepositosInscritos'))
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/eliminarDepositoInscrito/<int:ccnDepositosInscritos>')
def eliminarDepositoInscrito(ccnDepositosInscritos):
    try:
        mydb.connect()
        mycursor = mydb.cursor()
        mycursor.execute("delete from tblDepositosInscritos where ccnDepositosInscritos = %s", (ccnDepositosInscritos,))
    except Exception as e:
        print(e)
    finally:
        mydb.commit()
        mycursor.close()
        mydb.close()
        return redirect(url_for('listaDepositosInscritos'))


@app.route('/portalTransaccional/transferir', methods=['GET','POST'])
def transferir():
    titulo = "Realizar Transferencia"
    form = forms.transferir(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            mydb.connect()
            mycursor = mydb.cursor()
            sql = "select celularCliente from `Engine_DB`.`tblCliente` where ccnCliente = %s"
            val = (session['idCliente'],)
            mycursor.execute(sql, val)
            deposito = mycursor.fetchone()
            print(deposito)
            mydb.close()
            return render_template('portalTransaccional/transferir.html', titulo=titulo, form=form, deposito=deposito, usuario=usuario)
        else:
            fechaTransferencia = datetime.now()
            depositoElectronicoOrigen = request.form['productoOrigen']
            depositoElectronicoDestino = request.form['productoDestino']
            montoTransferencia = request.form['valorATransferir']
            
            print(depositoElectronicoOrigen, depositoElectronicoDestino, montoTransferencia)

            mydb.connect()
            mycursor = mydb.cursor()
            sql1 = """insert into `Engine_DB`.`tblTransferencias`(
                `ccnTransferencias`,
                `fechaTransferencia`,
                `depositoElectronicoOrigen`,
                `depositoElectronicoDestino`,
                `montoTransferencia`) VALUES (null, %s, %s, %s, %s);"""

            datos1 = (
                fechaTransferencia,
                depositoElectronicoOrigen,
                depositoElectronicoDestino,
                montoTransferencia)
                
            mycursor.execute(sql1, datos1)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")

            mydb.connect()
            mycursor = mydb.cursor()
            sql2 = "CALL `Engine_DB`.`spTransferencia`(%s, %s, %s);"

            datos2 = (
                depositoElectronicoOrigen,
                depositoElectronicoDestino,
                montoTransferencia)

            mycursor.execute(sql2, datos2)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")

            return redirect(url_for('portalTransaccional'))
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/portalTransaccional/listaConveniosInscritos', methods=['GET','POST'])
def listaConveniosInscritos():
    titulo = "Lista Convenios Inscritos"
    #form = forms.inscribirDepositos(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            try:
                mydb.connect()
                mycursor = mydb.cursor()
                sql = "select * from listaConvenios"
                mycursor.execute(sql)
                data = mycursor.fetchall()
                print(data)
            except Exception as e:
                print(e)
            finally:
                mycursor.close()
                mydb.close()
                return render_template('portalTransaccional/listaConveniosInscritos.html', titulo=titulo, usuario=usuario, data=data)
        else:
            return render_template('portalTransaccional/listaConveniosInscritos.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('ingresoCliente'))


@app.route('/ingresoEmpleado', methods=['GET','POST'])
def ingresoEmpleado():
    form = forms.ingresoEmpleado(request.form)
    if request.method == 'GET':
        return render_template('ingresoEmpleado.html', form=form)
    else:
        email = request.form['correoElectronicoEmpleado']
        contraseña = request.form['contraseñaEmpleado']
        mydb.connect()
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
            # pendiente establecer metodos para asignacion de dashboard
            return redirect(url_for('portalTransaccional'))
        else:
            mensajeError = 'Email o Contraseña incorrecta porfavor intente de nuevo'
            flash(mensajeError)
            return redirect(url_for('ingresoEmpleado'))


@app.route('/dbEmpleados')
def dbEmpleados():
    mydb.connect()
    mycursor = mydb.cursor()
    mycursor.execute("select * from `Engine_DB`.`tblEmpleado`;")
    listaEmpleados = mycursor.fetchall()
    return render_template('moduloAdminSistema/dbEmpleados.html', listaEmpleados=listaEmpleados)


@app.route('/registrarEmpleado', methods=['GET','POST'])
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

        mydb.connect()
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


@app.route('/eliminarEmpleado/<int:ccnEmpleado>')
def eliminarEmpleado(ccnEmpleado):
    mydb.connect()
    mycursor = mydb.cursor()
    mycursor.execute("delete from `Engine_DB`.`tblEmpleado` where ccnEmpleado = %s", (ccnEmpleado,))
    mydb.commit()
    return redirect(url_for('dbEmpleados'))


@app.route('/basePortalAdminSistema')
def base():
    return render_template('moduloAdminSistema/basePortalAdminSistema.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)
