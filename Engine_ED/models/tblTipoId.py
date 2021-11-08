from Engine_ED import db


class TipoId(db.Model):
    
    __tablename__ = 'tblTipoId'
    ccn = db.Column(db.Integer, primary_key=True)
    tipoId = db.Column(db.Integer, nullable=False)
    descripcionTipoId = db.Column(db.String(40), nullable=False)
    
    tipo_id = db.relationship('Cliente', backref='tipo_Id', lazy=True)
    

    def __init__(self, tipoId, descripcionTipoId):
        
        self.tipoId = tipoId
        self.descripcionTipoId = descripcionTipoId
        
        
    def __repr__(self):
        return f'TipoId: {self.descripcionTipoId}'