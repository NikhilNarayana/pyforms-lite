# !/usr/bin/python3
# -*- coding: utf-8 -*-


import logging, os, sys


PYFORMS_LOG_FILENAME = 'pyforms.log'
PYFORMS_LOG_HANDLER_FILE_LEVEL = logging.INFO
PYFORMS_LOG_HANDLER_CONSOLE_LEVEL = logging.INFO

PYFORMS_CONTROL_CODE_EDITOR_DEFAULT_FONT_SIZE = '12'
PYFORMS_CONTROL_EVENTS_GRAPH_DEFAULT_SCALE = 1

PYFORMS_QUALITY_TESTS_PATH = None

PYFORMS_STYLESHEET = None
PYFORMS_STYLESHEET_DARWIN = None
PYFORMS_STYLESHEET_LINUX = None
PYFORMS_STYLESHEET_WINDOWS = None

PYFORMS_CONTROLPLAYER_FONT = 9

# In a normal loading, there may be errors that show up which are not important.
# This happens because plugins_finder will search for classes on plugins which are not present because they are not needed.
# However, if plugin is not loaded at all, this will show all related errors.
# See pyforms.utils.plugins_finder.find_class()
PYFORMS_SILENT_PLUGINS_FINDER = True
