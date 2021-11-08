from Engine_ED import db


class Cliente(db.Model):
    
    __tablename__ = 'tblClientes'
    ccnCliente = db.Column(db.Integer, primary_key=True)
    numeroIdCliente = db.Column(db.Integer, primary_key=True, unique=True)
    tipoId = db.Column(db.Integer, db.ForeignKey('tblTipoId.ccn'), nullable=False)
    fechaExpIdCliente = db.Column(db.Date, nullable=False)
    lugarExpIdCliente = db.Column(db.Integer, nullable=False)
    primerNombreCliente = db.Column(db.String(20), nullable=False)
    segundoNombreCliente = db.Column(db.String(20), nullable=True)
    primerApellidoCliente = db.Column(db.String(20), nullable=False)
    segundoApellidoCliente = db.Column(db.String(20), nullable=True)
    fechaNacimientoCliente = db.Column(db.Date, nullable=False)
    idEstado = db.Column(db.String(1), nullable=False)
    idRoles = db.Column(db.String(10), nullable=True,)
    direccionCliente = db.Column(db.String(60), nullable=False)
    barrioCliente = db.Column(db.String(60), nullable=False)
    idPais = db.Column(db.String(2), nullable=False)
    idDepartamento = db.Column(db.Integer, nullable=False)
    idMunicipio = db.Column(db.Integer, nullable=False)
    celularCliente = db.Column(db.BigInteger, nullable=False)
    correoElectronicoCliente = db.Column(db.String(100), nullable=False)
    contraseñaCliente = db.Column(db.String(300), nullable=False)
    
    

    def __init__(self, numeroIdCliente, tipoId, fechaExpIdCliente, lugarExpIdCliente, primerNombreCliente,
                segundoNombreCliente, primerApellidoCliente, segundoApellidoCliente, fechaNacimientoCliente,
                direccionCliente, barrioCliente, idPais, idDepartamento, idMunicipio,
                celularCliente, correoElectronicoCliente, contraseñaCliente):
        
        self.numeroIdCliente = numeroIdCliente
        self.tipoId = tipoId
        self.fechaExpIdCliente = fechaExpIdCliente
        self.lugarExpIdCliente = lugarExpIdCliente
        self.primerNombreCliente = primerNombreCliente
        self.segundoNombreCliente = segundoNombreCliente
        self.primerApellidoCliente = primerApellidoCliente
        self.segundoApellidoCliente = segundoApellidoCliente
        self.fechaNacimientoCliente = fechaNacimientoCliente
        self.idEstado = "A"
        self.idRoles = "SHE-005"
        self.direccionCliente = direccionCliente
        self.barrioCliente = direccionCliente
        self.idPais = idPais
        self.idDepartamento = idMunicipio
        self.idMunicipio = idMunicipio
        self.celularCliente = celularCliente
        self.correoElectronicoCliente = correoElectronicoCliente
        self.contraseñaCliente = contraseñaCliente

    def __repr__(self):
        return f'Cliente: {self.numeroIdCliente}'