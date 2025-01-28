import unittest # import unittest module
from app import app # import app object from flask file


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # creating test case for /sum endpoint
    def test_sum(self):
        payload = {'num1': 2, 'num2': 3}
        response = self.app.post('/sum', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 5)

    # creating test case for /subtract endpoint
    def test_subtract(self):
        payload = {'num1': 10, 'num2': 2}
        response = self.app.post('/subtract', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 8)

    # creating test case for /multiply endpoint
    def test_multiply(self):
        payload = {'num1': 2, 'num2': 3}
        response = self.app.post('/multiply', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 6)

    # creating test case for /divide endpoint
    def test_divide(self):
        payload = {'num1': 10, 'num2': 2}
        response = self.app.post('/divide', json=payload)
        data = response.get_json()
        self.assertEqual(data['result'], 5)

if __name__ == '__main__':
    unittest.main()