from Engine_ED import app


if __name__ == '__main__':
    app.run()


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

'''