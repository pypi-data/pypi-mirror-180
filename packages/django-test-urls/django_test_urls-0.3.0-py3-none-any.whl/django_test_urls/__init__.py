#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" A package used to test the mapping of URLs to views and parameters.

:copyright: (c) 2022 by Alan Verresen
:license: MIT, see LICENSE for more details.
"""

from .resolves_to import resolves_to
from .resolves_to import resolves_to_404


__all__ = (
    'resolves_to',
    'resolves_to_404',
)

VERSION = "0.3.0"
