from Engine_ED import db


class Convenio(db.Model):
    
    __tablename__ = 'tblConvenios'
    ccnConvenios = db.Column(db.Integer, primary_key=True)
    codigoConvenio = db.Column(db.Integer, nullable=False)
    nombreEmpresa = db.Column(db.String(100), nullable=False)
    convenio = db.Column(db.String(100), nullable=False)
    datoCaptura = db.Column(db.String(100), nullable=False)
    modalidadConvenio = db.Column(db.String(100), nullable=False)
    idMunicipio = db.Column(db.Integer, nullable=False)
    idDepartamento = db.Column(db.Integer, nullable=False)
    

    def __init__(self, codigoConvenio, nombreEmpresa, convenio, datoCaptura, 
                 modalidadConvenio, idMunicipio, idDepartamento):
        
        self.codigoConvenio = codigoConvenio
        self.nombreEmpresa = nombreEmpresa
        self.convenio = convenio
        self.datoCaptura = datoCaptura
        self.modalidadConvenio = modalidadConvenio
        self.idMunicipio = idMunicipio
        self.idDepartamento = idDepartamento
        
        
    def ListarConvenios():
        
        q = Convenio.query.all()
        
        return q
        
        
    def __repr__(self):
        return f'Convenio: {self.codigoConvenio}'