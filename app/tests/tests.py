import unittest
from app.views import hello

class TestGuestApp(unittest.TestCase):

    def test_hello(self):
        name = 'Manuel'
        expected_output = 'Hello ' + name + '!!'
        real_output = hello.hello(name)
        self.assertEqual(real_output, expected_output)

if __name__ == '__main__':
    unittest.main()
