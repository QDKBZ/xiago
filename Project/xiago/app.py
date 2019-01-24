import os

from flask_script import Manager
from app import create_app
from flask_migrate import MigrateCommand

app = create_app()
manager = Manager(app)
manager.add_command('kaka', MigrateCommand)

if __name__ == '__main__':
    manager.run()

