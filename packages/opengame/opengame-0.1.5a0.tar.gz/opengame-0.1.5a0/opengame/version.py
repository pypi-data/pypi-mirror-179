from collections import namedtuple

__all__ = ['version']

_Version = namedtuple('Version', ['major', 'minor', 'micro'])
version = _Version(0, 1, 5)
