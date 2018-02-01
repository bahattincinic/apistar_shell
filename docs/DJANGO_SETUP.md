# Django Setup

```python
from apistar_shell.commands import django_commands
from apistar_shell.components import components


app = App(
    commands=django_commands
    components=components
)
```

## Usage

```bash
$ apistar shell

> session.Model.objects.all()
```
