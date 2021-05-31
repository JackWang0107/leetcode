from typing import *
class Solution:
    # 32 ms, faster than 40.00% of Python3 online submissions for Check if Word Equals Summation of Two Words.
    # 14.1 MB, less than 100.00% of Python3 online submissions for Check if Word Equals Summation of Two Words.
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def word2value(word):
            ans = 0
            for letter in word:
                ans = ans*10 + (ord(letter) - ord("a")) 
            return ans
        word_value_dict = {i:word2value(word) for i, word in enumerate([firstWord, secondWord, targetWord])}
        return word_value_dict[0] + word_value_dict[1] == word_value_dict[2]

    #  28 ms, faster than 100.00% of Python3 online submissions for Check if Word Equals Summation of Two Words.
    # 28 ms, faster than 100.00% of Python3 online submissions for Check if Word Equals Summation of Two Words.
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        mapping = {
            'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9'
        }
        def decoding(s):
            nonlocal mapping
            return int(''.join(list(map((lambda i:mapping[i]),list(s)))))
        
        return decoding(firstWord) + decoding(secondWord) == decoding(targetWord)


if __name__ == "__main__":
    so = Solution()
    print(so.isSumEqual(firstWord = "aaa", secondWord = "a", targetWord = "aab"))
