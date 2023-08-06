class EdgeError(Exception):
    """Exception raised when a node process fails to run."""

class DuplicatedError(Exception):
    """Raised when a duplicated item is found."""
    pass

class EmptyStorageError(Exception):
    """Raised when a storage is empty."""
    pass