# test_hello_world.py

import unittest
import subprocess

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        result = subprocess.run(['python', 'hello_world.py'], capture_output=True, text=True)
        self.assertEqual(result.stdout.strip(), "Hello, World!")  # Check that the output matches the expected result

if __name__ == '__main__':
    unittest.main()

