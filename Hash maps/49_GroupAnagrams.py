from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list)
        
        for word in strs:
            # 26-element frequency count for lowercase 'a'-'z'
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Tuples are hashable; use as dict key
            anagram_map[tuple(count)].append(word)
            
        return list(anagram_map.values())

if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]])
    ]
    
    for i, (input_strs, expected) in enumerate(test_cases):
        result = sol.groupAnagrams(input_strs)
        print(f"Test {i + 1}: Input: {input_strs} -> Output: {result} | Expected: {expected}")