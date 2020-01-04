from pathlib import Path
import sys
# Add the root module to the system path to allow this to be
# run from the command line / terminal
sys.path.append(str(Path(__file__).resolve().parent.parent))

from moduletutorial import mod
from harrytom import harry, tom

print(f"mod.foo(a) {mod.foo('a')}")

print(harry.harry())
print(tom.tom())