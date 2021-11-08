from Engine_ED import db


class Prueba(db.Model):
    
    __tablename__ = 'tblPrueba'
    ccn = db.Column(db.Integer, primary_key=True)


    def __init__(self):
        pass
        

    def __repr__(self):
        return f'ClaeTasaInteres: {self.ccn}'