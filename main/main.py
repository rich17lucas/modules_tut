from pathlib import Path
import os, sys
"""
 Add the root module to the system path to allow this to be
 run from the command line / terminal to prevent module not found
"""
sys.path.append(os.fspath(Path(__file__).resolve().parent.parent))

from foobah import foo, bah
from harrytom import harry, tom

print(f"foo.foo('a'): {foo.foo('a')}")
print(f"bah.bah(2): {bah.bah(2)}")
print(harry.harry())
print(tom.tom())
