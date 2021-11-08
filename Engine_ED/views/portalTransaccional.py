from Engine_ED import db, forms
from Engine_ED.models.tblCliente import Cliente
from Engine_ED.models.tblDepositosInscritos import DepositosInscritos
from Engine_ED.models.tblDepositoElectronico import DepositoElectronico
from Engine_ED.models.tblConvenio import Convenio
from flask import (Blueprint, flash, redirect, render_template, request,
                   session, url_for)
from flask_wtf import CSRFProtect

zonaTransaccional = Blueprint('zonaTransaccional', __name__, url_prefix='')

@zonaTransaccional.route('/portalTransaccional', methods=['GET','POST'])
def portalTransaccional():
    titulo = "Zona Transaccional"
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        ccnCliente = session['idCliente']
        cliente = Cliente.query.filter(Cliente.correoElectronicoCliente==usuario).first()
        depositoActivo = DepositoElectronico.query.filter(DepositoElectronico.ccnCliente == cliente.ccnCliente).first()
        if request.method == 'GET':
            return render_template('portalTransaccional/homePortalTransaccional.html', titulo=titulo, usuario=usuario, depositoActivo=depositoActivo)
        else:
            return render_template('portalTransaccional/homePortalTransaccional.html', titulo=titulo, usuario=usuario, depositoActivo=depositoActivo)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('landingPage.ingresoCliente'))
    

@zonaTransaccional.route('/cerrarSesion', methods=['GET','POST'])
def cerrarSesion():
    session.pop('username')
    session.pop('idCliente')
    return redirect(url_for('landingPage.index'))


@zonaTransaccional.route('/portalTransaccional/productos', methods=['GET','POST'])
def productos():
    titulo = "Productos"
    correoElectronico = session['username']
    cliente = Cliente.query.filter(Cliente.correoElectronicoCliente==correoElectronico).first()
    print(cliente)
    
    '''
    Verificacion de la base de datos y condiciona si el cliente no tiene un deposito electronico se asigna por defecto,
    si el cliente tiene un deposito electronico omite la asignacion por primera vez
    ''' 
    
    q1 = DepositoElectronico.query.filter(DepositoElectronico.depositoElectronico==cliente.celularCliente).first()
    
    if q1 != None:
        if 'username' and 'idCliente' in session:
            usuario = session['username']
            return render_template('portalTransaccional/productos.html', titulo=titulo, cliente=cliente, usuario=usuario)
        else:
            mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
            flash(mensajeErrorSesion)
            return redirect(url_for('landingPage.ingresoCliente'))
    else:
        #Ocurre la asignacion de un deposito electronico por defecto DETS

        depositoElectronico = cliente.celularCliente
        codigoCuenta = 21300501
        ccnCliente = cliente.ccnCliente
        cuantiaMaxDeposito = 2725578
        claseTasaInteres = "V"
        tasaInteres = 0.01
        frecLiqIntereses = "M"
        tipoDeposito = "DETS"
        saldoDeposito = 1000000


        depElecPorDefecto = DepositoElectronico(depositoElectronico,
                                                codigoCuenta,
                                                ccnCliente, 
                                                cuantiaMaxDeposito, 
                                                claseTasaInteres, 
                                                tasaInteres, 
                                                frecLiqIntereses, 
                                                tipoDeposito, 
                                                saldoDeposito)
        
        db.session.add(depElecPorDefecto)
        db.session.commit()

        if 'username' and 'idCliente' in session:
            usuario = session['username']
            return render_template('portalTransaccional/productos.html', titulo=titulo, cliente=cliente, usuario=usuario)
        else:
            mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
            flash(mensajeErrorSesion)
            return redirect(url_for('landingPage.ingresoCliente'))


@zonaTransaccional.route('/portalTransaccional/actualizarProducto', methods=['GET','POST'])
def actualizarProducto():
    titulo = "Productos"
    correoElectronico = session['username']
    cliente = Cliente.query.filter(Cliente.correoElectronicoCliente==correoElectronico).first()
    print(cliente)
    
    
    if 'username' and 'idCliente' in session:
        if request.method == 'POST':
            depositoElectronico = request.form['depositoElectronico']
            codigoCuenta = request.form['codigoCuenta']
            ccnCliente = request.form['ccnCliente']
            cuantiaMaxDeposito = request.form['cuantiaMaxDeposito']
            claseTasaInteres = request.form['claseTasaInteres']
            tasaInteres = request.form['tasaInteres']
            frecLiqIntereses = request.form['frecLiqIntereses']
            tipoDeposito = request.form['tipoDeposito']
            
            q = DepositoElectronico.query.filter(DepositoElectronico.depositoElectronico == depositoElectronico).first()
            
            if q != None:
                
                print(q)
                
                updateDep = DepositoElectronico.ActualizarDepElectronico(depositoElectronico, 
                                                                         codigoCuenta, 
                                                                         cuantiaMaxDeposito, 
                                                                         tasaInteres, 
                                                                         frecLiqIntereses, 
                                                                         tipoDeposito)
                
                return redirect(url_for('zonaTransaccional.portalTransaccional'))
            else:
                return redirect(url_for('zonaTransaccional.portalTransaccional'))    
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        
        return redirect(url_for('landingPage.ingresoCliente'))


@zonaTransaccional.route('/portalTransaccional/listaDepositosInscritos', methods=['GET','POST'])
def listaDepositosInscritos():
    titulo = "Lista Depositos Inscritos"
    form = forms.inscribirDepositos(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            depInscrito = DepositosInscritos.query.filter(DepositosInscritos.filtroLista == usuario).all()
            print(depInscrito)
            return render_template('portalTransaccional/listaDepositosInscritos.html', depInscrito=depInscrito, titulo=titulo, usuario=usuario, form=form)
        else:
            return render_template('portalTransaccional/listaDepositosInscritos.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('landingPage.ingresoCliente'))

@zonaTransaccional.route('/portalTransaccional/inscribirDepositosElectronicos', methods=['GET','POST'])
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

            nuevoDepositoInscrito = DepositosInscritos(filtroLista, 
                                                      tipoDeposito,
                                                      depositoElectronico, 
                                                      nombrePersonalizado, 
                                                      tipoId, 
                                                      numeroIdCliente)
            
            db.session.add(nuevoDepositoInscrito)
            db.session.commit()

            return redirect(url_for('zonaTransaccional.listaDepositosInscritos'))
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('landingPage.ingresoCliente'))


@zonaTransaccional.route('/portalTransaccional/editarDepositoInscrito/<int:ccnDepositosInscritos>')
def editarDepositoInscrito(ccnDepositosInscritos):
    titulo = "Editar Deposito Inscrito"
    form = forms.inscribirDepositos(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session['username']
        if request.method == 'GET':
            editarDeposito = DepositosInscritos.query.filter(DepositosInscritos.ccnDepositosInscritos == ccnDepositosInscritos).first()
            print(editarDeposito)
            return render_template('portalTransaccional/editarDepositosInscritos.html', titulo=titulo, usuario=usuario, editarDeposito=editarDeposito, form=form)
        else:
            return render_template('portalTransaccional/listaDepositosInscritos.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('landingPage.ingresoCliente'))


@zonaTransaccional.route('/portalTransaccional/procesoEdicionDepositoElectronico', methods=['GET','POST'])
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

            updateDepositoInscrito = DepositosInscritos.ActualizarDepositosInscritos(filtroLista, 
                                                                                   tipoDeposito, 
                                                                                   depositoElectronico, 
                                                                                   nombrePersonalizado, 
                                                                                   tipoId, 
                                                                                   numeroIdCliente, 
                                                                                   ccnDepositoInscrito)
            
            return redirect(url_for('zonaTransaccional.listaDepositosInscritos'))
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('landingPage.ingresoCliente'))


@zonaTransaccional.route('/portalTransaccional/eliminarDepositoInscrito/<int:ccnDepositosInscritos>')
def eliminarDepositoInscrito(ccnDepositosInscritos):
    
    deleteDepositoInscrito = DepositosInscritos.EliminarDepositosInscritos(ccnDepositosInscritos)
    
    return redirect(url_for('zonaTransaccional.listaDepositosInscritos'))
    

@zonaTransaccional.route('/portalTransaccional/listaConveniosInscritos', methods=['GET','POST'])
def listaConvenios():
    titulo = "Lista Convenios"
    #form = forms.inscribirDepositos(request.form)
    if 'username' and 'idCliente' in session:
        usuario = session   ['username']
        if request.method == 'GET':
            
            convenios = Convenio.ListarConvenios()
            
            return render_template('portalTransaccional/listaConvenios.html', titulo=titulo, usuario=usuario, convenios=convenios)
        else:
            return render_template('portalTransaccional/listaConvenios.html', titulo=titulo, usuario=usuario)
    else:
        mensajeErrorSesion = 'No existe una sesion activa porfavor ingrese a la plataforma'
        flash(mensajeErrorSesion)
        return redirect(url_for('zonaTransaccional.ingresoCliente'))
    
'''
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

'''
