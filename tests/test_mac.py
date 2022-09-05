import unittest
import isvalid

valid_text = [
    "FF:FF:FF:FF:FF:FF",
    "00:11:22:33:44:55",
]

invalid_text = [
    "FF:FF:FF",
    "FF:FF:FF:FF:FF:GG",
]

class TestMacAddr(unittest.TestCase):
    def test_valid(self):
        """checking valid syntax"""
        for v in valid_text:
            self.assertTrue(isvalid.mac_address(v))
            
    def test_invalid(self):
        """checking invalid syntax"""
        for b in invalid_text:
            self.assertFalse(isvalid.mac_address(b))