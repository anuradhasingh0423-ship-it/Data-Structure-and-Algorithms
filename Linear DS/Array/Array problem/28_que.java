class Solution {
    public int strStr(String haystack, String needle) {
        int hLen = haystack.length();
        int nLen = needle.length();

        if (nLen == 0) return 0;
        if (nLen > hLen) return -1;

        for (int start = 0; start <= hLen - nLen; start++) {
            int curr = 0;
            while (curr < nLen && haystack.charAt(start + curr) == needle.charAt(curr)) {
                curr++;
            }
            if (curr == nLen) {
                return start;
            }
        }
        return -1;
    }

    // 🛠️ ADD THIS: The main method to run your local test case
    public static void main(String[] args) {
        String haystack = "hello";
        String needle = "ll";
        
        Solution solution = new Solution();
        int result = solution.strStr(haystack, needle);
        
        System.out.println(result); // This will now compile cleanly!
    }
}