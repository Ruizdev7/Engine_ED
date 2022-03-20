from Engine_ED import db


class TipoId(db.Model):
    
    __tablename__ = 'tblTipoId'
    ccnTipoId = db.Column(db.Integer, primary_key=True)
    tipoId = db.Column(db.String(2), nullable=False)
    descripcionTipoId = db.Column(db.String(40), nullable=False)
    
    #Relationships
    clientes = db.relationship('Cliente', backref='tipoId', lazy=True)
    
    
    def __init__(self, tipoId, descripcionTipoId):
        
        self.tipoId = tipoId
        self.descripcionTipoId = descripcionTipoId
        
        
    def __repr__(self):
        return f'TipoId: {self.descripcionTipoId}'