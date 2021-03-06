# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words):
        words = sorted(words, key=lambda word:len(word))
        word_dict = {}
        
        for word in words:
            word_dict[word] = 1
        
        longest = 1
        for word in words:
        
            for i in range(len(word)):
                z=word[:i] + word[i + 1:] 
                
                if z in word_dict:
        
                
                    word_dict[word] = word_dict[word[:i] + word[i + 1:]]+ 1
                    
                    longest = max(longest, word_dict[word])
        
        
        return longest

obj = Solution()
print(obj.longestStrChain(["a","b","ba","bca","bda","bdca"]))