from config import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    reward = db.Column(db.Integer)
    resource_id = db.Column(db.Integer, db.ForeignKey("resources.id"))

    resource = db.relationship("Resource", back_populates="tasks")

    def __repr__(self) -> str:
        return f"Task: {self.name}"


class Resource(db.Model):
    __tablename__ = "resources"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)

    tasks = db.relationship("Task", back_populates="resource")

    def __repr__(self) -> str:
        return f"Resource: {self.name}"


class Score(db.Model):
    __tablename__ = "scores"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    num_turns = db.Column(db.Integer)
    game_won = db.Column(db.Boolean)

    def __repr__(self) -> str:
        return f"Score: {self.num_turns}"
