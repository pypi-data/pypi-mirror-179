"""
This module is part of the 'sitzungsdienst' package,
which is released under GPL-3.0-only license.
"""

from .regex import ASSIGNMENT, EXPRESS, PERSON
from .sta import Sitzungsdienst
from .utils import data2hash, dedupe, flatten, sort_din5007

__all__ = [
    # Main class
    "Sitzungsdienst",
    # RegExes
    "ASSIGNMENT",
    "EXPRESS",
    "PERSON",
    # Helpers
    "data2hash",
    "dedupe",
    "flatten",
    "sort_din5007",
]
