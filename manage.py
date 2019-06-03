from app import create_app
from flask_script import Manager, Server
from app import db
from app.models import User, BlogPost, Image, Comment
from flask_migrate import Migrate, MigrateCommand

app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict( app = app, db = db, User = User, BlogPost = BlogPost, Image = Image, Comment = Comment )

if __name__ == '__main__':
    manager.run()