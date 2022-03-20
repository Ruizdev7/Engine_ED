from Engine_ED import db


class TipoDeposito(db.Model):
    
    __tablename__ = 'tblTipoDepositos'
    ccnTipoDepositos = db.Column(db.Integer, primary_key=True)
    idTipoDepositos = db.Column(db.String(5), nullable=False)
    descripcionTipoDepositos = db.Column(db.String(100), nullable=False)
    
    
    def __init__(self, idTipoDepositos, descripcionTipoDepositos):
        
        self.idTipoDepositos = tipoDepositos
        self.descripcionTipoDepositos = descripcionTipoDepositos
        
        
    def __repr__(self):
        return f'TipoDeposito: {self.descripcionTipoDepositos}'