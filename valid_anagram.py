from collections import Counter


def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """    
    if len(s) != len(t):
        return False

    count_s, count_t= {}, {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
    
    return True

def is_anagram_counter(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """    
    return Counter(s) == Counter(t)

def is_anagram_sorted(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """    
    return sorted(s) == sorted(t)