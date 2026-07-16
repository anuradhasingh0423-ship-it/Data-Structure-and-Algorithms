from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
            
        dict_t = Counter(t)
        need = len(dict_t)
        have = 0
        window_counts = {}
        

        ans = float("inf"), None, None
        
        left = 0
        for right in range(len(s)):
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            if character in dict_t and window_counts[character] == dict_t[character]:
                have += 1
                
            while have == need:
                current_window_len = right - left + 1
                
                if current_window_len < ans[0]:
                    ans = (current_window_len, left, right)
                    
                left_char = s[left]
                window_counts[left_char] -= 1
                
                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    have -= 1
                    
                left += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]


if __name__ == "__main__":
    solution = Solution()
    
    s1, t1 = "ADOBECODEBANC", "ABC"
    result1 = solution.minWindow(s1, t1)
    
    s2, t2 = "a", "a"
    result2 = solution.minWindow(s2, t2)
    

    s3, t3 = "a", "aa"
    result3 = solution.minWindow(s3, t3)


    print("-" * 50)
    print(f" Test 1: s='{s1}', t='{t1}' -> Output: '{result1}'")
    print(f" Test 2: s='{s2}', t='{t2}'             -> Output: '{result2}'")
    print(f" Test 3: s='{s3}', t='{t3}'            -> Output: '{result3}'")
    print("-" * 50)