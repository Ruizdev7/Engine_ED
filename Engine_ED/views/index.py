from flask import render_template, Blueprint, redirect, request, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import CSRFProtect
from Engine_ED import forms, db
from Engine_ED.models.tblCliente import Cliente
from Engine_ED.models.tblDepositoElectronico import DepositoElectronico

landingPage = Blueprint('landingPage', __name__, url_prefix='')


@landingPage.route('/', methods=['GET'])
def index():
    return render_template('index/index.html')


@landingPage.route('/registroCliente', methods=['GET','POST'])
def registroCliente():
    form = forms.registroCliente(request.form)
    if request.method == 'GET':
        return render_template('index/registroCliente.html', form=form)
    else:
        numeroIdCliente = request.form['numeroIdCliente']
        tipoId = request.form["tipoId"]
        fechaExpIdCliente = request.form['fechaExpIdCliente']
        lugarExpIdCliente = request.form['lugarExpIdCliente']
        primerNombreCliente = request.form['primerNombreCliente']
        segundoNombreCliente = request.form['segundoNombreCliente']
        primerApellidoCliente = request.form['primerApellidoCliente']
        segundoApellidoCliente = request.form['segundoApellidoCliente']
        fechaNacimientoCliente = request.form['fechaNacimientoCliente']
        direccionCliente = request.form['direccionCliente']
        barrioCliente = request.form['barrioCliente']
        idPais = request.form['idPais']
        idDepartamento = request.form['idDepartamento']
        idMunicipio = request.form['idMunicipio']
        celularCliente = request.form['celularCliente']
        correoElectronicoCliente = request.form['correoElectronicoCliente']
        contraseñaCliente = generate_password_hash(request.form['contraseñaCliente'])

        nuevo_cliente = Cliente(numeroIdCliente, tipoId, fechaExpIdCliente, lugarExpIdCliente, 
                          primerNombreCliente, segundoNombreCliente, primerApellidoCliente, segundoApellidoCliente, 
                          fechaNacimientoCliente, direccionCliente, barrioCliente, idPais, idDepartamento, 
                          idMunicipio, celularCliente, correoElectronicoCliente, contraseñaCliente)

        db.session.add(nuevo_cliente)
        db.session.commit()
        
        return redirect(url_for('landingPage.ingresoCliente'))


@landingPage.route('/ingresoCliente', methods=['GET','POST'])
def ingresoCliente():
    form = forms.ingresoCliente(request.form)
    if request.method == 'GET':
        return render_template('index/ingresoCliente.html', form=form)
    else:
        correoElectronico = request.form['correoElectronicoCliente']
        contraseña = request.form['contraseñaCliente']

        consulta = Cliente.query.filter(Cliente.correoElectronicoCliente == correoElectronico).first()
    
        if correoElectronico == consulta.correoElectronicoCliente and check_password_hash(consulta.contraseñaCliente, contraseña):
            session['username'] = correoElectronico
            session['idCliente'] = contraseña
            mensajeExito = 'Bienvenido {}'.format(
                consulta.primerNombreCliente + ' ' + consulta.primerApellidoCliente)
            flash(mensajeExito)

            return redirect(url_for('zonaTransaccional.portalTransaccional'))
        else:
            mensajeError = 'Email o Contraseña incorrecta porfavor intente de nuevo'
            flash(mensajeError)

            return redirect(url_for('landingPage.ingresoCliente'))