import unittest

class DummyTest (unittest.TestCase): 
    def test_upper(self):
        assert "Hello".upper() == "HELLO"

if __name__ == '__main__':
    unittest.main()