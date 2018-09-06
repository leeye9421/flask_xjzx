from info import create_app, db
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import models


app = create_app("development")


# 数据库迁移
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()