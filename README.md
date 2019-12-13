# python_tutorial

Going through various learning resources.

# Youtube Links

[Dan Taylor - Get Productive with Python in Visual Studio Code](https://www.youtube.com/watch?v=6YLMWU-5H9o)

https://github.com/qubitron/pydemo

# Virtual environment

```
// create virtual environment in "env" subfolder
python -m venv env

// activate - PATH variable will be altered
env/Scripts/activate.bat

// show all python executables
where python

// start VSC
code .
```

```

pip install -r requirements.txt

pip freeze > requirements.txt

```

In VSC on the bottom left corner it should show "Python xxx ('env': venv)".

# VSC commands

Ctrl+Shift O - browse functions, etc (open symbols)

Ctrl+K U - Close Window

Ctrl+Shift P - and type discover Python unit tests

# Building a repository of code fragments

Needs to be:

- searchable
- runable in place (in vscode)
- ability to add pictures
- version control

folder structure

- algorithms
- data
- integration
  - nginx, wsgi
- python
  - basic
  - pythonic
  - generators
  - async
  - modules
    - collections
    - itertools
    - os
    - unittest
  - external modules
    - numpy
    - pandas
    - matplotlib
    - requests
    - sqlalchemy
    - zipfile
