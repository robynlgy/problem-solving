# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1 :
# Input: s = "egg", t = "add"
# Output: true

# Example 2 :
# Input: s = "foo", t = "bar"
# Output: false

# Example 3 :
# Input: s = "paper", t = "title"
# Output: true

# Example 4:
# Input: s = "bada", t = "baba"
# Output: false

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = defaultdict()
        seen = set()

        for i in range(len(s)):
            # if s has been mapped, is it the same t mapped before
            if s[i] in mapper:
                if mapper[s[i]] != t[i]: return False
            # if s not mapped yet, but someone already mapped to t
            elif t[i] in seen: return False
            else:
                mapper[s[i]]=t[i]
                seen.add(t[i])

        # print(seen)
        return True


    # space: O(n) * 2 ?
    # time: O(n)