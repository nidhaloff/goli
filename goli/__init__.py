# type: ignore[attr-defined]
"""The last boilerplate generator you will need (seriously)"""

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # pragma: no cover
    from importlib_metadata import PackageNotFoundError, version


__version__ = version(__name__)
