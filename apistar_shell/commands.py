from IPython import embed

from apistar import Command

from .components import ShellBackend
from .compat import DjangoSession, SqlalchemySession


def shell_sqlalchemy(session: SqlalchemySession, backend: ShellBackend):
    """
    This command includes SQLAlchemy DB Session
    """
    namespace = {
        'session': session
    }
    namespace.update(backend.get_namespace())
    embed(user_ns=namespace, header=backend.header)


def shell_django(session: DjangoSession, backend: ShellBackend):
    """
    This command includes Django DB Session
    """
    namespace = {
        'session': session
    }
    namespace.update(backend.get_namespace())
    embed(user_ns=namespace, header=backend.header)


def shell(backend: ShellBackend):
    namespace = backend.get_namespace()
    embed(user_ns=namespace, header=backend.header)


sqlalchemy_commands = [
    Command('shell', shell_sqlalchemy)
]

django_commands = [
    Command('shell', shell_django)
]

common_commands = [
    Command('shell', shell)
]
