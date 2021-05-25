from typing import *
class Solution:
    # 28 ms, faster than 94.77% of Python3 online submissions for Unique Morse Code Words.
    # 14.4 MB, less than 28.22% of Python3 online submissions for Unique Morse Code Words.
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup_table = {letter:code for letter, code in zip(
            "abcdefghijklmnopqrstuvwxyz", [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        )}
        ans = set()
        for word in words:
            key = ""
            for letter in word:
                key += lookup_table[letter]
            ans.add(key)
        return len(ans)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lookup_table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            key = ""
            for letter in word:
                key += lookup_table[ord(letter) - ord('a')]
            ans.add(key)
        return len(ans)



if __name__ == "__main__":
    so = Solution()
    print(so.uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]))