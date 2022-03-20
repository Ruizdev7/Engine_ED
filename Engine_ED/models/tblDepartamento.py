from Engine_ED import db


class Departamento(db.Model):
    
    __tablename__ = 'tblDepartamentos'
    ccnDepartamento = db.Column(db.Integer, primary_key=True)
    idDepartamento = db.Column(db.Integer, nullable=False)
    descripcionDepartamento = db.Column(db.String(60), nullable=False)
    ccnPais = db.Column(db.Integer, db.ForeignKey('tblPaises.ccnPais'), nullable=False)
    
    #Relationships
    municipios = db.relationship('Municipio', backref='departamento', lazy=True)
    clientes = db.relationship('Cliente', backref='departamento', lazy=True)
    
    def __init__(self, idDepartamento, descripcionDepartamento, ccnPais):
        
        self.idDepartamento = idDepartamento
        self.descripcionDepartamento = descripcionDepartamento
        self.ccnPais = ccnPais
        
        
    def __repr__(self):
        return f'Departamento: {self.descripcionDepartamento}'