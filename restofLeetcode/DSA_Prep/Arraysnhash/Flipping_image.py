"""
This is from an assesment
"""


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        if not image:
            return image

        for i in range(len(image)):
            row = image[i]
            row = row[::-1]
            image[i] = row

        for row in image:
            for i in range(len(row)):
                x = row[i]
                if x == 0:
                    row[i] = 1
                elif x == 1:
                    row[i] = 0

        return image