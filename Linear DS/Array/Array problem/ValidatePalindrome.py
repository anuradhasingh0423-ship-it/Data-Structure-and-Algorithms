class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move the left pointer forward if it points to a symbol/space
            while left < right and not s[left].isalnum():
                left += 1
                
            # Move the right pointer backward if it points to a symbol/space
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare the characters (case-insensitive conversion)
            if s[left].lower() != s[right].lower():
                return False
                
            # Move both pointers inward for the next round
            left += 1
            right -= 1
            
        return True

s = "Makam"
print(Solution().isPalindrome(s))  # Output: True
