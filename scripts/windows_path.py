import sys

cfg = 'venv-windows/pyvenv.cfg'
replace = f"home = {sys.path[-2]}"

with open(cfg, 'r') as file:
    lines = file.readlines()

with open(cfg, 'w') as file:
    for line in lines:
        if 'home' not in line.strip("\n"):
            file.write(line)
        else:
            file.write(replace + "\n")
