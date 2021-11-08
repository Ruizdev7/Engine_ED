from Engine_ED import db
from datetime import datetime


class Transferencia(db.Model):
    
    __tablename__ = 'tblTransferencias'
    ccnTransferencia = db.Column(db.Integer, primary_key=True)
    fechaTransferencia = db.Column(db.DateTime, nullable=False)
    depositoElectronicoOrigen = db.Column(db.BigInteger, nullable=False)
    depositoElectronicoDestino = db.Column(db.BigInteger, nullable=False)
    montoTransferencia = db.Column(db.Float, nullable=False)
    

    def __init__(self, depositoElectronicoOrigen, depositoElectronicoDestino, montoTransferencia):
        
        self.fechaTransferencia = datetime.now()
        self.depositoElectronicoOrigen = depositoElectronicoOrigen
        self.depositoElectronicoDestino = depositoElectronicoDestino
        self.montoTransferencia = montoTransferencia
        
        
    def __repr__(self):
        return f'Transferencia: {self.ccnTransferencia}'