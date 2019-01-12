import unittest
import coverage
import os

def test():
    COV = None
    COV = coverage.Coverage(branch=False, include='./*', omit=['venv/*', 'tests/*'])
    COV.start()
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    COV.stop()
    COV.save()
    print('Coverage Summary:')
    COV.report()
    COV.erase()