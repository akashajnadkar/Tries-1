#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
'''
Time Complexity - O(L) for inserting, searching, startsWith. L being length of the word


'''
class TrieNode:
    def __init__(self):
        self.children = [None] * 26 #26 alphabets
        self.isEnd = False #marks end of a word
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root 
        for c in word:
            idx = ord(c) - ord('a') #calculate position in the array
            if curr.children[idx] == None: #check if object present
                curr.children[idx] = TrieNode() #create an object if not created for that position 
            curr = curr.children[idx] #else move to the next child (deeper in the Trie)
        curr.isEnd = True #set the current child as the end to mark end of word
        

    def search(self, word: str) -> bool: #search a string in the Trie
        curr = self.root
        for c in word: #for every character in the string
            idx = ord(c) - ord('a') #get the index in the array
            if curr.children[idx] == None: #check if Node is present at that index
                return False #if not present the word is not present, search results to false
            curr = curr.children[idx] #if present move to next character and check
        return curr.isEnd #return True if the we reach the end of the Trie
        

    def startsWith(self, prefix: str) -> bool: #check for string starts with prefix
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True #follow similar approach as search. We return True when we reach end of Trie

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

