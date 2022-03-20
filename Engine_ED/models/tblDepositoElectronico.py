from Engine_ED import db


class DepositoElectronico(db.Model):
    
    __tablename__ = 'tblDepositosElectronicos'
    ccnDepositoElectronico = db.Column(db.Integer, primary_key=True)
    depositoElectronico = db.Column(db.BigInteger, nullable=False, unique=True)
    codigoCuenta = db.Column(db.BigInteger, nullable=False)
    ccnCliente = db.Column(db.Integer, nullable=False)
    cuantiaMaxDeposito = db.Column(db.Float, nullable=False)
    claseTasaInteres = db.Column(db.String(1), nullable=False)
    tasaInteres = db.Column(db.Float, nullable=False)
    frecLiqIntereses = db.Column(db.String(1), nullable=False)
    tipoDeposito = db.Column(db.String(5), nullable=False)
    saldoDeposito = db.Column(db.Float, nullable=True)
    
    
    def __init__(self, depositoElectronico, codigoCuenta, ccnCliente, cuantiaMaxDeposito, claseTasaInteres,
                 tasaInteres, frecLiqIntereses, tipoDeposito, saldoDeposito):
        
        self.depositoElectronico = depositoElectronico
        self.codigoCuenta = codigoCuenta
        self.ccnCliente = ccnCliente
        self.cuantiaMaxDeposito = cuantiaMaxDeposito
        self.claseTasaInteres = claseTasaInteres
        self.tasaInteres = tasaInteres
        self.frecLiqIntereses = frecLiqIntereses
        self.tipoDeposito = tipoDeposito
        self.saldoDeposito = 1000000
        
    
    def ActualizarDepElectronico(depositoElectronico, 
                                 codigoCuenta, 
                                 cuantiaMaxDeposito, 
                                 tasaInteres, 
                                 frecLiqIntereses, 
                                 tipoDeposito):
        
        q = DepositoElectronico.query.filter(DepositoElectronico.depositoElectronico == depositoElectronico).first()
        
        q.depositoElectronico = depositoElectronico
        q.codigoCuenta = codigoCuenta
        q.cuantiaMaxDeposito = cuantiaMaxDeposito
        q.tasaInteres = tasaInteres
        q.frecLiqIntereses = frecLiqIntereses
        q.tipoDeposito = tipoDeposito
        
        db.session.commit()
        
        return print(q)
        
    
    def __repr__(self):
        return f'DepositoElectronico: {self.depositoElectronico}' 