class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            if current_char in char_map and char_map[current_char] >= left:
                left = char_map[current_char] + 1
            
            char_map[current_char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length


if __name__ == "__main__":
    solution = Solution()
    
    string1 = "abcabcbb"
    result1 = solution.lengthOfLongestSubstring(string1)
    

    string2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(string2)
    
 
    string3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(string3)

    print("-" * 45)
    print(f"🎬 Test Case 1: '{string1}' -> Output Length: {result1}")
    print(f"🎬 Test Case 2: '{string2}'     -> Output Length: {result2}")
    print(f"🎬 Test Case 3: '{string3}'    -> Output Length: {result3}")
    print("-" * 45)