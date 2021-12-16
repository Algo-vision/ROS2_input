![Screenshot](index.png)
# PyCharm/ROS2 import wrapper.
The repository provides us with an ability to run the same way of importing files both in PyCharm and ROS2 packages.

Install:
```
git clone https://github.com/NanovelRobot/ROS2_input.git
cd ROS2_input
python3 setup.py install
```

Usage:
You need to add these rows to the very beginning of your main function.
```
from import_parents import smart_import
from pathlib import Path
__package__ = smart_import(file=Path(__file__).resolve(), level=1)
```
