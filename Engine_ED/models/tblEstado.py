from Engine_ED import db


class Estado(db.Model):
    
    __tablename__ = 'tblEstados'
    ccnEstado = db.Column(db.Integer, primary_key=True)
    idEstado = db.Column(db.String(1), nullable=False)
    descripcionEstado = db.Column(db.String(20), nullable=False)
    

    def __init__(self, idEstado, descripcionEstado):
        
        self.idEstado = idEstado
        self.descripcionEstado = descripcionEstado
    

    def __repr__(self):
        return f'Estado: {self.descripcionEstado}'