from Engine_ED import db


class PUC(db.Model):
    
    __tablename__ = 'tblPUC'
    ccnPUC = db.Column(db.Integer, primary_key=True)
    codigoCuenta = db.Column(db.Integer, nullable=False)
    nombreCuenta = db.Column(db.String(100), nullable=False)
    naturalezaCuenta = db.Column(db.String(1), nullable=False)
    tipoCuenta = db.Column(db.String(3), nullable=False)
    nivelCuenta = db.Column(db.String(60), nullable=False)
    lineaCuenta = db.Column(db.Integer, nullable=False)
    
    
    def __init__(self, codigoCuenta, nombreCuenta, naturalezaCuenta, tipoCuenta, nivelCuenta, lineaCuenta):
        
        self.codigoCuenta = codigoCuenta
        self.nombreCuenta = nombreCuenta
        self.naturalezaCuenta = naturalezaCuenta
        self.tipoCuenta = tipoCuenta
        self.nivelCuenta = nivelCuenta
        self.lineaCuenta = lineaCuenta
        
        
    def __repr__(self):
        return f'PUC: {self.codigoCuenta}'