import unittest
import isvalid

valid_text = [
    "ip6-localnet",
    "localhost",
    "john-doe",
    "ip6-loopback",
]

invalid_text = [
    "john@doe",
]

class TestEmail(unittest.TestCase):
    def test_valid(self):
        """checking valid syntax"""
        for v in valid_text:
            self.assertTrue(isvalid.hostname(v))
            
    def test_invalid(self):
        """checking invalid syntax"""
        for b in invalid_text:
            self.assertFalse(isvalid.hostname(b))