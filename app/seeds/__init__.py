from flask.cli import AppGroup
from .seed import seed_all, undo_seed

seed_commands = AppGroup('seed')


@seed_commands.command('all')
def seed():
    undo_seed()
    seed_all()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_seed()
