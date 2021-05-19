from typing import *
class Solution:
    # 32 ms, faster than 49.48% of Python3 online submissions for Goal Parser Interpretation
    # 14.3 MB, less than 39.22% of Python3 online submissions for Goal Parser Interpretation
    def interpret(self, command: str) -> str:
        ans = ""
        idx = 0
        total_go_through = 0
        while total_go_through < len(command):
            if command[idx] == "G":
                ans += "G"
                total_go_through += 1
                idx +=1
            elif command[idx:idx+2] == "(a":
                ans += "al"
                total_go_through += 4
                idx += 4
            else:
                ans += "o"
                total_go_through += 2
                idx +=2
        return  ans

    # 24 ms, faster than 93.73% of Python3 online submissions for Goal Parser Interpretation
    # 14.2 MB, less than 69.19% of Python3 online submissions for Goal Parser Interpretation.
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")

if __name__ == "__main__":
    so = Solution()
    print(so.interpret(command = "G()()()()(al)"))
