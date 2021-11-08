from Engine_ED import db


class ClaseTasaInteres(db.Model):
    
    __tablename__ = 'tblClaseTasaInteres'
    ccnClaseTasaInteres = db.Column(db.Integer, primary_key=True)
    claseTasaInteres = db.Column(db.String(1), nullable=False)
    descripcionClaseTasa = db.Column(db.String(25), nullable=False)
    
    
    def __init__(self, claseTasaInteres, descripcionClaseTasa):
        
        self.claseTasaInteres = claseTasaInteres
        self.descripcionClaseTasa = descripcionClaseTasa
    

    def __repr__(self):
        return f'ClaeTasaInteres: {self.descripcionClaseTasa}'