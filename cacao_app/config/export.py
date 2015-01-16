'''
Django Perseus Config
'''
# -*- coding: utf-8 -*-
import os
from os.path import join, dirname

from .common import Common

BASE_DIR = dirname(dirname(__file__))

class Local(Common):
    USE_PERSEUS = True
    DEBUG = True
    RENDER_STATIC = True
    PERSEUS_SOURCE_DIR = os.path.join(
        BASE_DIR, '..', "_output"
    )
    PERSEUS_STATIC_DIR = os.path.join(
        PERSEUS_SOURCE_DIR, "static"
    )
    PERSEUS_BUILD_DIR = os.path.join(
        BASE_DIR, '..', "temp"
    )
    PERSEUS_IMPORTERS = [
        'cacao.importers.MediaImporter',
        'cacao.importers.StaticImporter',
    ]