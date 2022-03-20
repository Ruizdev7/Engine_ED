from Engine_ED import db


class Cliente(db.Model):
    
    __tablename__ = 'tblClientes'
    ccnCliente = db.Column(db.Integer, primary_key=True)
    numeroIdCliente = db.Column(db.Integer, primary_key=True, unique=True)
    ccnTipoId = db.Column(db.Integer, db.ForeignKey('tblTipoId.ccnTipoId'))
    fechaExpIdCliente = db.Column(db.Date, nullable=False)
    lugarExpIdCliente = db.Column(db.Integer, db.ForeignKey('tblMunicipios.ccnMunicipios'))
    primerNombreCliente = db.Column(db.String(20), nullable=False)
    segundoNombreCliente = db.Column(db.String(20), nullable=True)
    primerApellidoCliente = db.Column(db.String(20), nullable=False)
    segundoApellidoCliente = db.Column(db.String(20), nullable=True)
    fechaNacimientoCliente = db.Column(db.Date, nullable=False)
    ccnEstado = db.Column(db.Integer, db.ForeignKey('tblEstados.ccnEstado'))
    ccnRoles = db.Column(db.Integer, db.ForeignKey('tblRoles.ccnRoles'))
    direccionCliente = db.Column(db.String(60), nullable=False)
    barrioCliente = db.Column(db.String(60), nullable=False)
    ccnPais = db.Column(db.Integer, db.ForeignKey('tblPaises.ccnPais'))
    ccnDepartamento = db.Column(db.Integer, db.ForeignKey('tblDepartamentos.ccnDepartamento'))
    ccnMunicipio = db.Column(db.Integer, db.ForeignKey('tblMunicipios.ccnMunicipios'))
    celularCliente = db.Column(db.BigInteger, nullable=False)
    correoElectronicoCliente = db.Column(db.String(100), nullable=False)
    contraseñaCliente = db.Column(db.String(300), nullable=False)
    

    def __init__(self, numeroIdCliente, ccnTipoId, fechaExpIdCliente, lugarExpIdCliente, primerNombreCliente,
                segundoNombreCliente, primerApellidoCliente, segundoApellidoCliente, fechaNacimientoCliente,
                direccionCliente, barrioCliente, ccnPais, ccnDepartamento, ccnMunicipio,
                celularCliente, correoElectronicoCliente, contraseñaCliente):
        
        self.numeroIdCliente = numeroIdCliente
        self.ccnTipoId = ccnTipoId
        self.fechaExpIdCliente = fechaExpIdCliente
        self.lugarExpIdCliente = lugarExpIdCliente
        self.primerNombreCliente = primerNombreCliente
        self.segundoNombreCliente = segundoNombreCliente
        self.primerApellidoCliente = primerApellidoCliente
        self.segundoApellidoCliente = segundoApellidoCliente
        self.fechaNacimientoCliente = fechaNacimientoCliente
        self.Estado = 1
        self.ccnRoles = "SHE-005"
        self.direccionCliente = direccionCliente
        self.barrioCliente = direccionCliente
        self.ccnPais = ccnPais
        self.ccnDepartamento = ccnDepartamento
        self.ccnMunicipio = ccnMunicipio
        self.celularCliente = celularCliente
        self.correoElectronicoCliente = correoElectronicoCliente
        self.contraseñaCliente = contraseñaCliente

    def __repr__(self):
        return f'Cliente: {self.numeroIdCliente}'