
import unittest
from Search import *


class TestSearchBar(unittest.TestCase):

    #tests whether empty string fails in search
    def test_empty_string_in_search(self):
        self.assertEqual(search(""),False)

    #tests whether an incorrect name fails or not
    def test_incorrect_name(self):
        self.assertEqual(search("randomNameThatisnt a StoKASDLP)(@WIOPQJoi1o1i9u3712893oijsan"), False)
    
    #tests whether a correct name fails or not
    def test_correct_name(self):
        self.assertEqual(search("csco"), True)
    
    #tests whether an correct name with different capitalizations fails or not
    def test_correct_name_alternate(self):
        self.assertEqual(search("CsCo"),True)
    
    #tests whether an incorrect name close to an actual name fails or not
    def test_incorrect_name_alternate(self):
        self.assertEqual(search("Cisco"),False)

if __name__ == '__main__':
    unittest.main()