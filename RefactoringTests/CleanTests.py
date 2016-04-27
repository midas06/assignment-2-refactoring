from Validator import *
import unittest


class CleanCoverageTests(unittest.TestCase):
    # A558,F,08,885,Normal,517

    def setUp(self):
        self.v = Validator()

    def test_clean_id(self):
        input = "a558,F,08,885,Normal,517"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","885","Normal","517"])

    def test_clean_gender(self):
        input = "A558,f,08,885,Normal,517"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","885","Normal","517"])

    def test_clean_age(self):
        input = "A558,F,8,885,Normal,517"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","885","Normal","517"])

    def test_clean_sales_1(self):
        input = "A558,F,08,85,Normal,517"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","085","Normal","517"])

    def test_clean_sales_2(self):
        input = "A558,F,08,5,Normal,517"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","005","Normal","517"])

    def test_clean_bmi(self):
        input = "A558,F,08,885,normal,517"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","885","Normal","517"])

    def test_clean_income(self):
        input = "A558,F,08,85,Normal,7"
        output = self.v.clean_input(input)
        self.assertEqual(output, ["A558","F","08","085","Normal","07"])


if __name__ == "__main__":
    unittest.main(verbosity=2)

