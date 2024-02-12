from config import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String) 
    description = db.Column(db.String)
    reward = db.Column(db.Integer)
    difficulty = db.Column(db.Integer)
    
    resource_id = db.Column(db.Integer, db.ForeignKey('resources.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', back_populates="tasks")
    resource = db.relationship('Resource', back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task: {self.name}"


class Resource(db.Model):
    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String) 
    quantity = db.Column(db.Integer)

    tasks = db.relationship('Task', back_populates="resource")

    def __repr__(self) -> str:
        return f"Resource: {self.name}"
        

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    experience = db.Column(db.Integer)

    tasks = db.relationship('Task', back_populates="user")

    def __repr__(self) -> str:
        return f"User: {self.name}"