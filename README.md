## Setup

Create a virtual environvent.

```bash
$ python -m venv <venv-name>
```

Change include-system-site-package to true.

```conf
home = ...
include-system-site-packages = true
version = 3.8.6
```

Activate virtual environment.

```bash
$ source <venv>/bin/activate
```

Install ursina

```bash
$ pip install -r requirements.txt
```
