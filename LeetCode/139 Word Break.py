# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                # print(i, s[i])
                if len(s)-i >= len(word) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)]
                    if dp[i]: break
        # print(dp)
        return dp[0]
