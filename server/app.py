from config import app, migrate

from models import db

if __name__ == "__main__":
  with app.app_context():
    migrate.init_app(app, db)
    pass
    # remove pass and write your cli logic
