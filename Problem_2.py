#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
'''
Time Complexity - O(ML) M- number of words, L-length on each word


'''
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None: #insertion in the Trie
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] == None: #check if node is present for character
                curr.children[idx] = TrieNode() #create a node if not present
            curr = curr.children[idx] #else move to next character 
        curr.isEnd = True #once all characters of the word are covered mark the last node as end

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word) #insert all words of dictionary in the Trie.
        result = ""
        sentenceArr =sentence.split() #split all the words of the sentence in to an array
        
        for i in range(len(sentenceArr)):
            sb = ""
            if i!=0:
                result=result+" " #add a space before every word in result except the first word
            word = sentenceArr[i]
            curr = self.root
            for c in word: #for every character in the word
                idx = ord(c) - ord('a')  #get the index in the children array
                if curr.children[idx] == None or curr.isEnd: #check if the trie node exists for character
                    break #break away from loop if the node is end node or the prefix of word does not match that in dictionary
                curr = curr.children[idx] #continue to next character if it matches
                sb+=c #add the character to a temporary string
            
            if curr.isEnd:
                result+=sb #append temporary string(word from dictionary) if prefix matches
            else:
                result+=word #append the entire word if the word does not matches
        return result #return the result


        
# @lc code=end

