# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
 

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            for other_word in strs[1:]:
                if i == len(other_word) or other_word[i] != char:
                    return first_word[:i]
        return first_word        
    
strs = ["flower","flow","flight"]
solution = Solution()
result = solution.longestCommonPrefix(strs)
print(result)  # Output: "fl"    