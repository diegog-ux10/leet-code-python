import unittest
from merge_words import merge_alternately

class Test(unittest.TestCase):
    
    def test_merge_words(self):
        self.assertEqual(merge_alternately("abc", "pqr"), "apbqcr")
        self.assertEqual(merge_alternately("abcd", "pq"), "apbqcd")
        self.assertEqual(merge_alternately("ab", "pqrs"), "apbqrs")
        
if __name__ == "__main__":
    unittest.main()