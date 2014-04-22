# -*- coding: utf-8 -*-
"""
    Flask-Collect
    =============

    Flack-Collect is simply application for collect static files in Flask_
    project.
    Serve static files with Flask_ -- bad idea for production, with this you
    will can collect them in one command.

    This extension checks application blueprints for static files and copy it
    to specific folder (saves related paths).

"""

from .collect import Collect
from .version import __version__, __license__

assert Collect

__project__ = __name__
__author__ = "Kirill Klenov <horneds@gmail.com>"
