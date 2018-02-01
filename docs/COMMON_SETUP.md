# Common Setup

This setup doesn't related to db session.

```python
from apistar_shell.commands import common_commands
from apistar_shell.components import components


app = App(
    commands=common_commands
    components=components
)
```

## Usage

```bash
$ apistar shell
```
