# Copyright 2020-2021 Laszlo Attila Toth
# Distributed under the terms of the GNU Lesser General Public License v3

import sys

from dewi_core.application import Application
from . import FindCommand


def main():
    app = Application('dewi-find', FindCommand)
    app.run(sys.argv[1:])


if __name__ == '__main__':
    main()
