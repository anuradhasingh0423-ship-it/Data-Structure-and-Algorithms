# 28. Find the Index of the First Occurrence in a String

#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example 1:
#Input: haystack = "sadbutsad", needle = "sad"
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.

#Example 2:
#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution(object):
    def strStr(self, haystack, needle):
        h_len = len(haystack)
        n_len = len(needle)

        if n_len == 0:
            return 0
        if n_len > h_len:
            return -1
        
        for i in range(h_len - n_len + 1):
            curr = 0
            while curr < n_len and haystack[i + curr] == needle[curr]:
                curr += 1
            if curr == n_len:
                return i
        return -1    

haystack = "Sadbutsad"
needle = "sad"
print(Solution().strStr(haystack, needle))

