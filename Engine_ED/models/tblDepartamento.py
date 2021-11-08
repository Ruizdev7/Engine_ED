from Engine_ED import db


class Departamento(db.Model):
    
    __tablename__ = 'tblDepartamentos'
    ccnDepartamento = db.Column(db.Integer, primary_key=True)
    idDepartamento = db.Column(db.Integer, nullable=False)
    descripcionDepartamento = db.Column(db.String(60), nullable=False)
    idPais = db.Column(db.String(2), nullable=False)
    
    def __init__(self, idDepartamento, descripcionDepartamento, idPais):
        
        self.idDepartamento = idDepartamento
        self.descripcionDepartamento = descripcionDepartamento
        self.idPais = idPais
        
        
    def __repr__(self):
        return f'Departamento: {self.descripcionDepartamento}'