"""Conflict-free Replicated Data Type tools."""

from __future__ import annotations

import time


class LWWDict(dict):
    """
    A subclass of dict that implements a Last-Writer-Wins (LWW) CRDT.

    This implementation of LWWDict uses the timestamps attribute to track the
    last time a key-value pair was added or updated in the dictionary. When
    merge() is called, the timestamps of the pairs in the other dictionary are
    compared with the corresponding timestamps in the current dictionary, and
    the pairs from the other dictionary are only added or updated in the
    current dictionary if they have a more recent timestamp. This ensures
    that the last writer wins in case of conflicts.

    """

    def __init__(self, **kwargs) -> None:
        """Initialize a LWWDict."""
        super().__init__()
        self.timestamps = {}
        for key, value in kwargs.items():
            self[key] = value

    def __setitem__(self, key, value):
        """Set an item."""
        self.timestamps[key] = time.time()
        super().__setitem__(key, value)

    def merge(self, other):
        """Merge with another LWWDict via timestamp comparison."""
        for key, value in other.items():
            if key not in self or self.timestamps[key] < other.timestamps[key]:
                self[key] = value
