from Editor import *
import unittest
from unittest import mock as mock


class EditorNewValueCoverageTests(unittest.TestCase):
    # A558,F,08,885,Normal,517
    def setUp(self):
        self.e = Editor()

    def test(self):
        with mock.patch(self.e.set_new_value) as mp:
            mp.return_value = ""

if __name__ == "__main__":
    unittest.main(verbosity=2)

