from Engine_ED import db


class DepositosInscritos(db.Model):
    
    __tablename__ = 'tblDepositosInscritos'
    ccnDepositosInscritos = db.Column(db.Integer, primary_key=True)
    filtroLista = db.Column(db.String(60), nullable=False)
    tipoDeposito = db.Column(db.String(5), nullable=False)
    depositoElectronico = db.Column(db.BigInteger, nullable=False)
    nombrePersonalizado = db.Column(db.String(100), nullable=False)
    tipoId = db.Column(db.String(2), nullable=False)
    numeroIdCliente = db.Column(db.Integer, nullable=False)
    

    def __init__(self, filtroLista, tipoDeposito, depositoElectronico, nombrePersonalizado, tipoId, numeroIdCliente):
        
        self.filtroLista = filtroLista
        self.tipoDeposito = tipoDeposito
        self.depositoElectronico = depositoElectronico
        self.nombrePersonalizado = nombrePersonalizado
        self.tipoId = tipoId
        self.numeroIdCliente = numeroIdCliente
        
        
    def ActualizarDepositosInscritos(filtroLista,
                                   tipoDeposito,
                                   depositoElectronico,
                                   nombrePersonalizado,
                                   tipoId,
                                   numeroIdCliente,
                                   ccnDepositosInscritos):
                
        q = DepositosInscritos.query.filter(DepositosInscritos.ccnDepositosInscritos == ccnDepositosInscritos).first()
        
        q.filtroLista = filtroLista
        q.tipoDeposito = tipoDeposito
        q.depositoElectronico = depositoElectronico
        q.nombrePersonalizado = nombrePersonalizado
        q.tipoId = tipoId
        q.ccnDepositosInscritos = ccnDepositosInscritos
        
        db.session.commit()
        
        return print(q)
        
    
    def EliminarDepositosInscritos(ccnDepositosInscritos):
        
        q = DepositosInscritos.query.filter(DepositosInscritos.ccnDepositosInscritos == ccnDepositosInscritos).first()
        
        db.session.delete(q)
        db.session.commit()
        
        return print(q)
    
    
    def __repr__(self):
        return f'DepositosInscritos: {self.ccnDepositosInscritos}'