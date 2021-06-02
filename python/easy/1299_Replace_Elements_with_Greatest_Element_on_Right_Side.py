from typing import *
class Solution:
    # 176 ms, faster than 42.43% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    # 15.2 MB, less than 85.67% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    def replaceElements(self, arr: List[int]) -> List[int]:
        local_max = arr[-1]
        for idx in range(2, len(arr)):
            temp = arr[-idx]
            arr[-idx] = local_max
            if local_max < temp:
                local_max = temp
        arr[0] = local_max
        arr[-1]= -1
        return arr

    # 116 ms, faster than 90.27% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    # 15.6 MB, less than 21.93% of Python3 online submissions for Replace Elements with Greatest Element on Right Side.
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-2, -1, -1):
            arr[i] = max(arr[i], arr[i+1])
        return arr[1:]+[-1]



if __name__ == "__main__":
    so = Solution()
    print(so.replaceElements(arr = [400]))