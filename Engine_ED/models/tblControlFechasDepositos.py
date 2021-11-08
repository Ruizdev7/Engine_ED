from Engine_ED import db


class ControlFechasDepositos(db.Model):
    
    __tablename__ = 'tblControlFechasDepositos'
    ccnControlFechas = db.Column(db.Integer, primary_key=True)
    depositoElectronico = db.Column(db.BigInteger, nullable=True, unique=True)
    fechaInicial = db.Column(db.Date, nullable=True)
    fechaUltimoMovimientoCredito = db.Column(db.Date, nullable=True)
    fechaUltimaCausacion = db.Column(db.Date, nullable=True)
    fechaProximaCausacion = db.Column(db.Date, nullable=True)
    fechaLiquidacion = db.Column(db.Date, nullable=True)
    fechaTerminacion = db.Column(db.Date, nullable=True)
    

    def __init__(self, depositoElectronico, fechaInicial, fechaUltimoMovimientoCredito, fechaUltimaCausacion, fechaProximaCausacion, fechaLiquidacion, fechaTerminacion):
        
        self.depositoElectronico = depositoElectronico
        self.fechaInicial = fechaInicial
        self.fechaUltimoMovimientoCredito = fechaUltimoMovimientoCredito
        self.fechaUltimaCausacion = fechaUltimaCausacion
        self.fechaProximaCausacion = fechaProximaCausacion
        self.fechaLiquidacion = fechaLiquidacion
        self.fechaTerminacion = fechaTerminacion
        
        
    def __repr__(self):
        return f'ControlFechasDepositos: {self.depositoElectronico}'