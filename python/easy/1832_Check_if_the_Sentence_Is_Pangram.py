from typing import *
class Solution:
    # 24 ms, faster than 96.35% of Python3 online submissions for Check if the Sentence Is Pangram.
    # 14.2 MB, less than 48.07% of Python3 online submissions for Check if the Sentence Is Pangram.
    def checkIfPangram(self, sentence: str) -> bool: 
        if set("abcdefghijklmnopqrstuvwxyz") - set(sentence) == set():
            return True
        return False

    def checkIfPangram(self, sentence: str) -> bool: 
        if len(set("abcdefghijklmnopqrstuvwxyz")) - len(set(sentence)) == 0:
            return True
        return False

if __name__ == "__main__":
    so = Solution()
    print(so.checkIfPangram(sentence = "thequickbrownfoxjumpsoverthelazydog"))