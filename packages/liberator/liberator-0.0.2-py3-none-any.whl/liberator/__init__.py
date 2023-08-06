"""
mkinit -m liberator
mkinit -m liberator --diff
mkinit -m liberator --diff --help
"""

__version__ = '0.0.2'

from liberator import core as closer
from liberator.core import (Closer,)

__explicit__ = ['Closer', 'closer']  # fixme, mkinit is not respecting this

# ^^^ Backwards compatibility ^^^


from liberator import core
from liberator.core import (Liberator,)

__all__ = ['Closer', 'Liberator', 'closer', 'core']
