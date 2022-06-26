class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            '(':')',
            '{':'}',
            '[':']'
        }

        seen = []

        for char in s:
            if char in hmap:
                seen.append(hmap[char])
            elif seen and seen[-1] == char:
                seen.pop()
            else:
                return False

        return len(seen) == 0