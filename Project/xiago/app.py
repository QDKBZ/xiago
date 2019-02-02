import os
from app import create_app, db
from app.models import User
from flask_migrate import Migrate, Manager, MigrateCommand

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()