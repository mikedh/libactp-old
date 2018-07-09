import unittest

class ACTPTest(unittest.TestCase):
    """
    Test to make sure plumbing is hooked up
    """
    def test_import(self):
        import pyactp
        # make sure it actually has methods
        assert hasattr(pyactp, 'makerough')

if __name__ == '__main__':
    unittest.main()
