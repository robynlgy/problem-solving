# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# O(m * n * 26) -> O(m * n)
# note default dict -> if key doesnt exist yet, default to a list
# lists cant be keys -> tuple
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:               # O(m)
            count = [0]*26              # 26 -> O(1)
            for char in word:           # O(n)
                count[ord(char)-ord('a')] += 1
            res[tuple(count)].append(word)

        return res.values()




# O( m * nlog(n)) where m = # of words, n = len of each word
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = {}

#         for word in strs:                           #m
#             sorted_str = ''.join(sorted(word))      #nlogn
#             if res.get(sorted_str):
#                 res[sorted_str].append(word)
#             else:
#                 res[sorted_str]=[word]

#         return list(res.values())