from Editor import *
import unittest
from unittest import mock as mock


class EditorCoverageTests(unittest.TestCase):
    # A558,F,08,885,Normal,517
    def setUp(self):
        self.e = Editor()

    def test(self):
        bad_input = {"A58,F,08,885,Normal,517"}
        self.e.set_raw(bad_input)
        expected = Person('A58','F','08','885','Normal','517')
        with mock.patch(self.e.set_new_value()) as mp:
            mp.return_value = 'A558'
            self.e.validate()
            self.assertEqual(self.e._good_data[0], expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)

