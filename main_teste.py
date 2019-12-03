import unittest
import os
import main
import re

class MyTestCase(unittest.TestCase):
    def test_something(self):
        for _, _, arquivo in os.walk('input'):
            for dir in arquivo:
                input_file = open('input/' + dir, 'r')
                output_file = open('output/' + dir, 'r')
                response = []
                controller = 0
                for line in output_file.readlines():
                    response.append(int(line))
                output_file.close()
                n = int(input_file.readline())
                while n != 0:
                    amostras = list(map(int, input_file.readline().split()))
                    self.assertEqual(response[controller], main.scanner(n, amostras))
                    n = int(input_file.readline())
                    controller += 1

                input_file.close()


if __name__ == '__main__':
    unittest.main()
