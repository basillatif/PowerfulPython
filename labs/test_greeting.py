import unittest
from greeting import greet
"""
    * Where is the test module ("test_greeting") specified?
        in the test_greeting file
    * Where is the test class ("TestGreeting") specified?
        in the test_greeting file
    * Where is the test method ("test_greet") specified?
            in the test_greeting file

    * What is the line number of the failing test?
    18
"""

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        greet("John")
        #assert "Hi, John" == greet("John")
        self.assertEqual("Hi, John", greet("Hi, John"))

