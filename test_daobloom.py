# test_daobloom.py
"""
Tests for DaoBloom module.
"""

import unittest
from daobloom import DaoBloom

class TestDaoBloom(unittest.TestCase):
    """Test cases for DaoBloom class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DaoBloom()
        self.assertIsInstance(instance, DaoBloom)

    def test_run_method(self):
        """Test the run method."""
        instance = DaoBloom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
