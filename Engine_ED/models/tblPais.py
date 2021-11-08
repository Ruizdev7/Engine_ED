from Engine_ED import db


class Pais(db.Model):
    
    __tablename__ = 'tblPaises'
    ccnPais = db.Column(db.Integer, primary_key=True)
    idPais = db.Column(db.String(2), nullable=False)
    descripcionPais = db.Column(db.String(60), nullable=False)
    
    
    def __init__(self, idPais, descripcionPais):
        
        self.idPais = idPais
        self.descripcionPais = descripcionPais
        
        
    def __repr__(self):
        return f'Pais: {self.descripcionPais}'