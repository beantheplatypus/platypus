print("Hello, World!")
import os
from pathlib import Path

path = "/"
os.chdir(path)
f = open("list.txt", "r")
amountofwords = (f.read())
