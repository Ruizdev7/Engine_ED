from Engine_ED import db


class Empleado(db.Model):
    __tablename__ = 'tblEmpleados'
    ccnEmpleado = db.Column(db.Integer, primary_key=True)
    numeroIdEmpleado = db.Column(db.Integer, nullable=False, unique=True)
    tipoId = db.Column(db.String(2), nullable=False)
    fechaExpIdEmpleado = db.Column(db.Date, nullable=False)
    lugarExpIdEmpleado = db.Column(db.Integer, nullable=False)
    primerNombreEmpleado = db.Column(db.String(20), nullable=False)
    segundoNombreEmpleado = db.Column(db.String(20), nullable=True)
    primerApellidoEmpleado = db.Column(db.String(20), nullable=False)
    segundoApellidoEmpleado = db.Column(db.String(20), nullable=True)
    fechaNacimientoEmpleado = db.Column(db.Date, nullable=False)
    idEstado = db.Column(db.String(1), nullable=False)
    idRoles = db.Column(db.String(10), nullable=True,)
    direccionEmpleado = db.Column(db.String(60), nullable=False)
    barrioEmpleado = db.Column(db.String(60), nullable=False)
    idPais = db.Column(db.String(2), nullable=False)
    idDepartamento = db.Column(db.Integer, nullable=False)
    idMunicipio = db.Column(db.Integer, nullable=False)
    celularEmpleado = db.Column(db.BigInteger, nullable=False)
    correoElectronicoEmpleado = db.Column(db.String(100), nullable=False)
    contraseñaEmpleado = db.Column(db.String(300), nullable=False)

    def __init__(self, numeroIdEmpleado, tipoId, fechaExpIdEmpleado, lugarExpIdEmpleado, primerNombreEmpleado,
                segundoNombreEmpleado, primerApellidoEmpleado, segundoApellidoEmpleado, fechaNacimientoEmpleado,
                direccionEmpleado, barrioEmpleado, idPais, idDepartamento, idMunicipio,
                celularEmpleado, correoElectronicoEmpleado, contraseñaEmpleado):
        
        self.numeroIdEmpleado = numeroIdEmpleado
        self.tipoId = tipoId
        self.fechaExpIdEmpleado = fechaExpIdEmpleado
        self.lugarExpIdEmpleado = lugarExpIdEmpleado
        self.primerNombreEmpleado = primerNombreEmpleado
        self.segundoNombreEmpleado = segundoNombreEmpleado
        self.primerApellidoEmpleado = primerApellidoEmpleado
        self.segundoApellidoEmpleado = segundoApellidoEmpleado
        self.fechaNacimientoEmpleado = fechaNacimientoEmpleado
        self.idEstado = "A"
        self.idRoles = ""
        self.direccionEmpleado = direccionEmpleado
        self.barrioEmpleado = direccionEmpleado
        self.idPais = idPais
        self.idDepartamento = idMunicipio
        self.idMunicipio = idMunicipio
        self.celularEmpleado = celularEmpleado
        self.correoElectronicoEmpleado = correoElectronicoEmpleado
        self.contraseñaEmpleado = contraseñaEmpleado

    def __repr__(self):
        return f'Empleado: {self.numeroIdEmpleado}'