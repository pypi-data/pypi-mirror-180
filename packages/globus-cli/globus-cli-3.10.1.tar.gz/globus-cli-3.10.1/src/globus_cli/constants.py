"""
This module is used to define constants used throughout the code.
It should not depend on any other part of the globus-cli codebase.

(If you need to import something else, maybe it's not simple enough to be a constant...)
"""

__all__ = ("EXPLICIT_NULL",)


class _ExplicitNullClass:
    """
    Magic sentinel value used to disambiguate values which are being
    intentionally nulled from values which are `None` because no argument was
    provided
    """

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "null"


EXPLICIT_NULL = _ExplicitNullClass()
