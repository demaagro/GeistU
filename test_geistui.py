# test_geistui.py
"""
Tests for GeistUI module.
"""

import unittest
from geistui import GeistUI

class TestGeistUI(unittest.TestCase):
    """Test cases for GeistUI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GeistUI()
        self.assertIsInstance(instance, GeistUI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GeistUI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
