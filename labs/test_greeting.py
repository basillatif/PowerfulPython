import unittest
from greeting import greet

class TestGreeting(unittest.TestCase):
    def test_greet(self):
        greet("John")
        #assert "Hi, John" == greet("John")
        self.assertEqual("Hi, John", greet("John"))

        """
        * Where is the test module ("test_greeting") specified?
        * Where is the test class ("TestGreeting") specified?
        * Where is the test method ("test_greet") specified?
        * What is the line number of the failing test?
        """

