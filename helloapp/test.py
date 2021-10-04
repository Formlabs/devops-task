from helloapp.app import hello_world
import unittest

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertIn("Hello", hello_world(), "Endpoint is not polite enough.")
