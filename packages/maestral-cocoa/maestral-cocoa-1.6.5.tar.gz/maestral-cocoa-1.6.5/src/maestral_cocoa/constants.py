# -*- coding: utf-8 -*-

# system imports
import sys

try:
    from importlib.metadata import metadata  # type: ignore
except ImportError:
    # Backwards compatibility Python 3.7 and lower
    from importlib_metadata import metadata  # type: ignore


_app_module = sys.modules["__main__"].__package__
_md = metadata(_app_module)  # type: ignore

# detect if we have been built with briefcase or frozen with PyInstaller
FROZEN = "Briefcase-Version" in _md or getattr(sys, "frozen", False)
