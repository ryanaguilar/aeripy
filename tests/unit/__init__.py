"""aeripy Unit Test Suite."""
from aeripy import Aeripy


class UnitTest:
    """Base class for aeripy unit tests."""

    def setup(self):
        """Setup runs before all test cases."""
        self.aeries = Aeripy(
            endpoint="dummy",
            api_key="dummy"
        )
        # Unit tests should never issue requests
