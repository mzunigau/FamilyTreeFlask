from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# parent = db.Table("parent",
#     db.Column("parent_id", db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"), primary_key=True),
#     db.Column("child_id", db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
# )

# child = db.Table("child",
#     db.Column("parent_id", db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"), primary_key=True),
#     db.Column("child_id", db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"), primary_key=True)
# )

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    age = db.Column(db.Integer)  
    padres = db.relationship("Person", secondary="padres", primaryjoin="Person.id==padres.c.parent_id", secondaryjoin="Person.id==padres.c.child_id",lazy="joined")
    hijos = db.relationship("Person", secondary="hijos", primaryjoin="Person.id==hijos.c.child_id", secondaryjoin="Person.id==hijos.c.parent_id",lazy="joined")
    
    #parents = db.relationship("Person", secondary="progeny", primaryjoin="Person.id==progeny.c.parent_id", secondaryjoin="Person.id==progeny.c.child_id", lazy="joined")
    #children = db.relationship("Person", secondary="progeny", primaryjoin="Person.id==progeny.c.child_id", secondaryjoin="Person.id==progeny.c.parent_id", lazy="joined")

    def __repr__(self):
        return '<Person %r>' % self.first_name

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "padres": list(map(lambda x: x.serialize(), self.padres)),
            #"childrens": list(map(lambda x: x.serialize(), self.childrens))
            # do not serialize the password, its a security breach
        }
    def getAllbyAge():
        persons = Person.query.order_by(Person.age.desc()).all()
        return list(map(lambda x: x.serialize(), persons))

class Padres(db.Model):
    __tablename__ = 'padres'
    parent_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"),primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"),primary_key=True)

    def __repr__(self):
        return '<Padres %r>' % self.parent_id
        
    def serialize(self):
        return {
            "parent_id": self.parent_id,
            "child_id": self.child_id,
            # do not serialize the password, its a security breach
        }

class Hijos(db.Model):
    __tablename__ = 'hijos'
    parent_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"),primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey("person.id", ondelete="CASCADE"),primary_key=True)

    def __repr__(self):
        return '<Hijos %r>' % self.parent_id
        
    def serialize(self):
        return {
            "parent_id": self.parent_id,
            "child_id": self.child_id,
            # do not serialize the password, its a security breach
        }