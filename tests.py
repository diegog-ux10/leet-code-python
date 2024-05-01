import unittest

from merge_words import merge_alternately
from contains_duplicate import contains_duplicate
from valid_anagram import is_anagram

class Test(unittest.TestCase):
    
    def test_merge_words(self):
        self.assertEqual(merge_alternately("abc", "pqr"), "apbqcr")
        self.assertEqual(merge_alternately("abcd", "pq"), "apbqcd")
        self.assertEqual(merge_alternately("ab", "pqrs"), "apbqrs")
        
    def test_contains_duplicate(self):
        self.assertTrue(contains_duplicate([1,2,3,1]))
        self.assertFalse(contains_duplicate([1,2,3,4]))
        self.assertTrue(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
        
    def test_valid_anagram(self):
        self.assertTrue(is_anagram("anagram", "nagaram"))
        self.assertFalse(is_anagram("rat", "car"))
        
        
if __name__ == "__main__":
    unittest.main()