import unittest
from person import Person


class TestPerson(unittest.TestCase):
    def test_main(self):
        guy = TestPerson("John", "Doe")
        assert(guy.firstname(), "John")
        assert(guy.lastname(), "Doe")
        assert(guy.full_name(), "John Doe")
        assert(guy.formal_name("Mr."), "Mr. John Doe")