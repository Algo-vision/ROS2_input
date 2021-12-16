import sys, importlib
from pathlib import Path

def smart_import(file = None, level=1):
    # global __package__
    file = Path(__file__).resolve() if file is None else file
    parent, top = file.parent, file.parents[level]
    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError:  # already removed
        pass

    __package__ = '.'.join(parent.parts[len(top.parts):])
    importlib.import_module(__package__)  # won't be needed after that
    return __package__

if __name__ == '__main__':
    smart_import(1)