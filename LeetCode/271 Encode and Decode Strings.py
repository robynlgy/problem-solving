# Design an algorithm to encode a list of strings to a string. The encoded string
#  is then sent over the network and is decoded back to the original list of strings.

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """

        # instead of passing secret key like this, could make a delimiter like:
        # length of str + # + word
        # 'hello','world' -> '5#hello5#world'

        def rot13(char):
            return chr(ord(char)+13)

        for i in range(len(strs)):
            newstr=''
            for char in strs[i]:
                newstr += rot13(char)
            strs[i]=newstr

        SECRET_KEY="ao#134sdf$%"
        res = SECRET_KEY.join(strs)

        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        SECRET_KEY="ao#134sdf$%"
        res = s.split(SECRET_KEY)

        def rot13(char):
            return chr(ord(char)-13)

        for i in range(len(res)):
            newstr=''
            for char in res[i]:
                newstr += rot13(char)
            res[i]=newstr


        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))