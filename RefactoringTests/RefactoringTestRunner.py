from RefactoringTests.CleanTests import *


def refactoring_suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(CleanCoverageTests))

    return the_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = refactoring_suite()
    runner.run(test_suite)

