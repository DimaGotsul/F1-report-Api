import unittest
from api import app


class FlaskTesting(unittest.TestCase):

    def test_report(self):
        tester = app.test_client(self)
        response = tester.get('/report')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_report_id(self):
        tester = app.test_client(self)
        response = tester.get('/report/DRR')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_drivers(self):
        tester = app.test_client(self)
        response = tester.get('/drivers')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_drivers_id(self):
        tester = app.test_client(self)
        response = tester.get('/drivers/DRR')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
