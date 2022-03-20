from Engine_ED import db


class Roles(db.Model):
    
    __tablename__ = 'tblRoles'
    ccnRoles = db.Column(db.Integer, primary_key=True)
    idRoles = db.Column(db.String(7), nullable=False)
    descripcionRoles = db.Column(db.String(60), nullable=False)
    
    #Relationships
    clientes = db.relationship('Cliente', backref='roles', lazy=True)
    
    
    def __init__(self, idRoles, descripcionRoles):
        
        self.idRoles = idRoles
        self.descripcionRoles = descripcionRoles
        
        
    def __repr__(self):
        return f'Roles: {self.descripcionRoles}'