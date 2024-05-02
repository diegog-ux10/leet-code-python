from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    res = defaultdict(list) # mapping charCount to list of anagrams

    for s in strs:
        count = [0] * 26 # a ... z

        for c in s:
            test = ord('a')
            test2 = ord('b')
            count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)

    return res.values()

def main():
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    
if __name__ == "__main__":
   main()