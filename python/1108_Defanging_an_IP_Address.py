class Solution:
    # 28ms, faster than 76.51% of Python3 online submissions for Defanging an IP Address.
    # 14.3 MB, less than 32.32% of Python3 online submissions for Defanging an IP Address.
    def defangIPaddr(self, address: str) -> str:
        ans = address.split(".")
        return "[.]".join(ans)

    # 32 ms, faster than 43.45% of Python3 online submissions for Defanging an IP Address
    # 14.2 MB, less than 63.49% of Python3 online submissions for Defanging an IP Address
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for char in address:
            if char != ".":
                ans += char
            else:
                ans += "[.]"
        return ans

    # 32 ms, faster than 43.45% of Python3 online submissions for Defanging an IP Address.
    # 14.2 MB, less than 32.32% of Python3 online submissions for Defanging an IP Address
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == "__main__":
    so = Solution()
    print(so.defangIPaddr( "255.100.50.0"))