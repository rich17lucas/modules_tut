#README.md
This is a trivial project to solve how to update the path when running 
a Python script that referenced modules, from the command line.

This first started to cause me a problem when I used first Poetry to create a
new project for me (_though it was the first time I had decided to create
a project with modules so I doubt it's problem with Poetry but more my own
naivety_)

So as an experiment, I created a project with this directory structure 
```
modules_tut:.
├─── __init.py__
├─── foobah
│   ├─── __init.py__
│   ├─── bah.py
│   ├─── foo.py
├─── harrytom
│   └─── __init.py__
│   ├─── harry.py
│   ├─── tom.py
├─── main
│   ├─── __init.py__
│   ├─── main.py
```

When I executed the `main.py` the result was a ModuleNotFoundError

```
(venv) E:\work\pythonprojects\modules_tut>python main/main.py
Traceback (most recent call last):
  File "main/main.py", line 9, in <module>
    from foobah import foo, bah
ModuleNotFoundError: No module named 'foobah'

```

After Googl-ing & Stackoverflow-ing, I found these articles:

[Python Modules and Packages – An Introduction](https://realpython.com/python-modules-packages/) by John Sturtz
which was the inspiration for this self learning experiment, and:

[Python 3's pathlib Module: Taming the File System](https://realpython.com/python-pathlib/) by Gier Arne Hjelle
which introduced the use of `pathlib` library

Basically to avoid the `module not found` error, add these lines to the main program
and then its possible to run main.py successfully from the command line.

```python
import os, sys
from pathlib import Path
sys.path.append(os.fspath(Path(__file__).resolve().parent.parent))
```  

Now when its executed, it works as expected.
```
(venv) E:\work\pythonprojects\modules_tut>python main/main.py
arg = a
foo.foo('a'): None
bah.bah(2): 4
harry
tom

```
