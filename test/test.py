
import unittest
import method as methods

class RmitStoreAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_database_connection():
        methods.setUp()
        methods.checkDatabaseErrorAppear()
        methods.tearDown()