from mockito import mock, verify
import unittest

from read_root import read_root

class HelloWorldTest(unittest.TestCase):

    def test_correct_message(self):
        out = mock()
        read_root()
        //verify(out).write("Hello World!\n")