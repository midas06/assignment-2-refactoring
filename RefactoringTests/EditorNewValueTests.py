from Editor import *
from NewValueHandler import *
import unittest
from unittest import mock as mock


class EditorNewValueCoverageTests(unittest.TestCase):
    # A558,F,08,885,Normal,517
    def setUp(self):
        self.e = Editor()

    def test(self):
        with mock.patch('NewValueHandler.IDValueHandler.input') as mp:
            mp.return_value = "a123"
            self.assertEqual(IDValueHandler.set_new_value('kj'), 'A123')

if __name__ == "__main__":
    unittest.main(verbosity=2)

