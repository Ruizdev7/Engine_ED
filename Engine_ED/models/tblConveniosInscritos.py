from Engine_ED import db


class ConveniosInscritos(db.Model):
    
    __tablename__ = 'tblConveniosInscritos'
    ccnConveniosInscritos = db.Column(db.Integer, primary_key=True)
    filtroLista = db.Column(db.String(50), nullable=False)
    codigoConvenio = db.Column(db.Integer, nullable=False)
    

    def __init__(self, filtroLista, codigoConvenio):
        
        self.filtroLista = filtroLista
        self.codigoConvenio = codigoConvenio
        
        
    def __repr__(self):
        return f'ConveniosInscritos: {self.ccnConveniosInscritos}'