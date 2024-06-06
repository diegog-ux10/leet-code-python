def longest_consecutive_sequence(nums):
    """find the length of the longest consecutive elements sequence."""
    num_set = set(nums)
    longest = 0
    
    for n in nums:
        # check is its the start of a sequence.
        if(n - 1) not in num_set:
            length = 0
            while (n + length) in num_set:
                length += 1
            longest = max(length, longest)
    
    return longest
    
