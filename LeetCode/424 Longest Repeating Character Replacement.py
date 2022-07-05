# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        maxf = 0
# maxf: keeps track of the highest frequency seen, doesn't have to be reduced when you shift your left pointer bcz the only way for you to get a higher res is if maxf got larger than before
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            maxf = max(maxf, count[s[r]])
            while (r - l + 1 - maxf) > k :
                count[s[l]] -= 1
                l+=1
            res = max(res, r - l + 1)

        return res


# slightly slower, getting max freq count is O(26) so overall time complexity is O(26n) => O(n)
#         count = {}
#         res = 0
#         l = 0

#         for r in range(len(s)):
#             count[s[r]] = count.get(s[r],0) + 1
#             while (r - l + 1 - max(count.values())) > k :
#                 count[s[l]] -= 1
#                 l+=1
#             res = max(res, r - l + 1)

#         return res




#         l, r, longest = 0, 0, 0
#         count = defaultdict()

#         while r < len(s):
#             count[s[r]] = count.get(s[r],0) + 1
#             mostFrequent = max(count.values())
#             while (r-l+1) - mostFrequent > k:
#                 count[s[l]] -= 1
#                 mostFrequent = max(count.values())
#                 l += 1
#             longest = max(longest,r-l+1)
#             r+=1

#         return longest