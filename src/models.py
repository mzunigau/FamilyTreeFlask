from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Persona(db.Model):
    __tablename__= 'persona'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<Persona %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
            # do not serialize the password, its a security breach
        }
    def getAllbyAge():
        personas = Persona.query.order_by(Persona.age.desc()).all()
        return list(map(lambda x: x.serialize(), personas))


class Padres(db.Model):
    __tablename__= 'padres'
    id_hijo = db.Column(db.Integer, db.ForeignKey("persona.id"), primary_key=True)
    id_padre = db.Column(db.Integer, db.ForeignKey("persona.id"), primary_key=True) 
    def __repr__(self):
        return '<Padres %r>' % self.id_hijo

    def serialize(self):
        return {
            "id_hijo": self.id_hijo,
            "id_padre": self.id_padre,
            # do not serialize the password, its a security breach
        }
