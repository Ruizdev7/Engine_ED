from Engine_ED import db
from datetime import datetime


class Pagos(db.Model):
    
    __tablename__ = 'tblPagos'
    ccnPagos = db.Column(db.Integer, primary_key=True)
    fechaPagoConvenio = db.Column(db.DateTime, nullable=False)
    depositoElectronicoOrigen = db.Column(db.BigInteger, nullable=False)
    codigoConvenio = db.Column(db.Integer, nullable=False)
    montoPago = db.Column(db.Float, nullable=False)
    

    def __init__(self, depositoElectronicoOrigen, codigoConvenio, montoPago):
        
        self.fechaPagoConvenio = datetime.now()
        self.depositoElectronicoOrigen = depositoElectronicoOrigen
        self.codigoConvenio = codigoConvenio
        self.montoPago = montoPago
        
        
    def __repr__(self):
        return f'Pagos: {self.ccnPagos}'