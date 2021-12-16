# PyCharm/ROS2 import wrapper.
The repository provides us with an ability to run the same way of importing files both in PyCharm and ROS2 packages.

Usage:
```
from import_parents import smart_import
from pathlib import Path
__package__ = smart_import(file=Path(__file__).resolve(), level=1)
```
![Screenshot](index.png)
