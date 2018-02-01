# API Star Shell
API Star Shell inspired from Django


## Installation

```
$ pip install apistar_shell
```

## Setup

For Sqlalchemy:

```python
from apistar_shell.commands import sqlalchemy_shell
from apistar_shell.components import components


app = App(
    commands=sqlalchemy_shell
    components=components
)
```

For Django:

```python
from apistar_shell.commands import django_shell
from apistar_shell.components import components


app = App(
    commands=django_shell
    components=components
)
```

For Common:

```python
from apistar_shell.commands import common_shell
from apistar_shell.components import components


app = App(
    commands=common_shell
    components=components
)
```


## Usage:

```
$ apistar shell
```


## Configuration

**Auto import models, modules:**

```python
settings = {
  'APISTAR_SHELL': {
      'PRE_IMPORTS': [
            {
                'module': 'module.submodule1',
                'imports': [class1', 'function2']
            },
            {
                'module': 'module.submodule2'',
                'imports': ['function3']
            },
            {
                'module': 'module'
            },
        ]
}
```

The above example would directly translate to the following python code which would be executed before the automatic imports:

```python
from module.submodule1 import class1, function2
from module.submodule2 import function3
import module
```

**Change Shell Header:**

```python
settings = {
    'APISTAR_SHELL': {
        'HEADER': 'Example Shell'
    }
}
```

**Customize imports & Namespace:**

foo.py
```python
from datetime import datetime

def bar():
    return {'datetime': datetime }
```

settings.py

```python
settings = {
    'APISTAR_SHELL': {
        'CUSTOM_FUNCTION': {
            'module': 'foo',
            'function': 'bar'
        },
    }
}
```
