from Engine_ED import db


class Municipio(db.Model):
    
    __tablename__ = 'tblMunicipios'
    ccnMunicipios = db.Column(db.Integer, primary_key=True)
    idMunicipio = db.Column(db.Integer, nullable=False)
    descripcionMunicipio = db.Column(db.String(60), nullable=False)
    ccnDepartamento = db.Column(db.Integer, db.ForeignKey('tblDepartamentos.ccnDepartamento'), nullable=False)
    
    #Relationships
    clientes = db.relationship('Cliente', backref='municipio', lazy=True)
    
    def __init__(self, idMunicipio, descripcionMunicipio, idDepartamento):
        
        self.idMunicipio = idMunicipio
        self.descripcionMunicipio = descripcionMunicipio
        self.ccnDepartamento = ccnDepartamento
        
        
    def __repr__(self):
        return f'Municipio: {self.descripcionMunicipio}'