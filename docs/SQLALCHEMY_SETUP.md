# Sqlalchemy Setup

```python
from apistar_shell.commands import sqlalchemy_commands
from apistar_shell.components import components


app = App(
    commands=sqlalchemy_commands
    components=components
)
```

## Usage

```bash
$ apistar shell

> session.query(Model).all()
```
