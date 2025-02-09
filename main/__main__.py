import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import heebow

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        
print("Successfully deployed!")
print("@wahiebtalal ")

if __name__ == "__main__":
    heebow.run_until_disconnected()
