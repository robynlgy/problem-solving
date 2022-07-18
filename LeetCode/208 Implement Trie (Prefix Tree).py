# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

# Example:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True

class TrieNode:

    def __init__(self):
        self.children = [0]*26
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            c = ord(char)-ord('a')
            if not curr.children[c]:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            c = ord(char)-ord('a')
            if not curr.children[c]:
                return False
            curr = curr.children[c]

        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for char in prefix:
            c = ord(char)-ord('a')
            if not curr.children[c]:
                return False
            curr = curr.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# class TrieNode:

#     def __init__(self):
#         self.children = {}   #instead of mult nodes we can also have a place for each letter node
#         self.end = False

#     # def __repr__(self):
#     #     print("val:",self.val,"\nchildren:",self.children,"\nend:",self.end)
# class Trie:

#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word: str) -> None:
#         curr = self.root

#         for char in word:
#             if char not in curr.children:
#                 curr.children[char]=TrieNode()
#             curr = curr.children[char]
#         curr.end = True

#     def search(self, word: str) -> bool:
#         curr = self.root

#         for char in word:
#             if char not in curr.children:
#                 return False
#             curr = curr.children[char]

#         return curr.end

#     def startsWith(self, prefix: str) -> bool:
#         curr = self.root
#         for char in prefix:
#             if char not in curr.children:
#                 return False
#             curr = curr.children[char]
#         return True


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)