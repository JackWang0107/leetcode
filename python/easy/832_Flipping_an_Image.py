from typing import *
class Solution:
    # a simple solution, change each row of image in-place by comprehension.
    # 36 ms, faster than 99.84% of Python3 online submissions for Flipping an Image.
    # 14.2 MB, less than 53.32% of Python3 online submissions for Flipping an Image.
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image[0])):
            image[row] = [1-bit for bit in image[row][::-1]]
        return image

    # 52 ms, faster than 50.26% of Python3 online submissions for Flipping an Image.
    # 14.1 MB, less than 78.57% of Python3 online submissions for Flipping an Image.
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image[0])):
            image[row] = list(map(lambda pixel: 1-pixel, image[row][::-1]))
        return image
    
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        length = ( len(image[0])+1 ) // 2
        for row in range(len(image[0])):
            for pixel in range(length):
                temp = image[row][pixel]
                image[row][pixel] = 1- image[row][length - pixel]
                image[row][length - pixel] = 1 - temp
        return image


if __name__ == "__main__":
    so = Solution()
    print(so.flipAndInvertImage( image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))