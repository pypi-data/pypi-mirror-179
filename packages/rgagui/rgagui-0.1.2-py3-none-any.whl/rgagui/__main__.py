#!/usr/bin/env python3

import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication
from .ui.taskmain import TaskMain


def main():
    TaskMain.DefaultConfigFile = str(Path(__file__).parent / "examples/rga100/myrga.taskconfig")
    app = QApplication(sys.argv)
    main_window = TaskMain()
    main_window.show()
    app.exec()


if __name__ == '__main__':
    main()


