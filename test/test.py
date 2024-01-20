
import unittest
import method as methods


class RmitStoreAppPositiveTestCases(unittest.TestCase):
    def test_database_connection(self):
        methods.setUp()
        methods.checkDatabaseErrorAppear()
        methods.tearDown()
