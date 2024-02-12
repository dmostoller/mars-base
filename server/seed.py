from config import app

from models import *

if __name__ == "__main__":
  with app.app_context():
      resources = []

      resources.append(Resource(name = "Air", quantity = 10))
      resources.append(Resource(name = "Food", quantity = 10))
      resources.append(Resource(name = "Fuel", quantity = 10))        
      resources.append(Resource(name = "Water", quantity = 10))

      db.session.add_all(resources)
      db.session.commit()
    # remove pass and write your seed data