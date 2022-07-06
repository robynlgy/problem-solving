from collections import Counter

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1 :
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Example 3:
# Input: s1 = 'abc', s2 = 'bbabbc'
# Output: false


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # worst case is O(26n) -- loop + checking s1_count == s2_count with 26 keys max -- this is if every single char in s2 is a dupe from s1: eg. s1 = 'abc' s2 = 'bbabbc'
        # probs between O(26n) and O(n)

        l,r = 0,0
        set1 = set(s1)
        s1_count = Counter(s1)
        s2_count = {}

        while r < len(s2):
            while r - l < len(s1) and r < len(s2):
            # while window is less than length of s1
                if s2[r] in set1:
                # if char at r is in s1, add to counter and move to next char
                    s2_count[s2[r]] = s2_count.get(s2[r],0) + 1
                    r += 1
                else:
                # if window doesnt reach len(s1) = theres no permutations from 0 up until r, clear out s2 counter and set both pointers to next char
                    s2_count = {}
                    r += 1
                    l = r

            # if reached here, window size = len(s1) and all chars in window are in s1, however count may be diff
            if s1_count == s2_count:
                return True

            # if reached here, window size = len(s1) but freq count is diff
            if l >= len(s2) or r >= len(s2): return False

            # moving l up, so decrement the count at l.
            s2_count[s2[l]] -= 1
            l += 1








        # doesnt work
#         s1_count = collections.Counter(s1)
#         s2_count = {}

#         print(s1_count)

#         for i in range(len(s2)):
#             if s2[i] in s1:
#                 s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1
#                 if s1_count == s2_count: return True
#             else :
#                 s2_count = {}
#         return False


#         for i in range(len(s2)):
#             if s2[i] == s1[0]:
#                 if (self.checkString(i,s1,s2)): return True

#         return False


#     def checkString(self,i,s1,s2):
#         if len(s1) == 1: return True
#         #check forward, i cant be the last one
#         for j in range(1,len(s1)):
#             if (i+j) >= len(s2): break
#             if s2[i+j] != s1[j]:
#                 break
#             if j == len(s1)-1:
#                 return True
#         #check backward
#         for k in range(1,len(s1)):
#             if (i-k) < 0: break
#             if s2[i-k] != s1[k]:
#                 break
#             if k == len(s1)-1:
#                 return True
#         return False
