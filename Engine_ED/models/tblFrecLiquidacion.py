from Engine_ED import db


class FrecuenciaLiquidacion(db.Model):
    
    __tablename__ = 'tblFrecLiquidacion'
    ccnFrec = db.Column(db.Integer, primary_key=True)
    idFrecuencia = db.Column(db.String(1), nullable=False)
    descripcionFrecuencia = db.Column(db.String(50), nullable=False)
    

    def __init__(self, idFrecuencia, descripcionFrecuencia):
        
        self.idFrecuencia = idFrecuencia
        self.descripcionFrecuencia = descripcionFrecuencia
        
    
    def __repr__(self):
        return f'FrecLiquidacion: {self.descripcionFrecuencia}'