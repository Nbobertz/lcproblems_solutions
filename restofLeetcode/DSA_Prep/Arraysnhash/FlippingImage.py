"""
Here we are just trying to flip an image
"""
def solution(image):
    if not image:
        return image

    step1 = []
    for i in range(len(image)):
        row = image.pop(0)
        row = row[::-1]
        step1.append(row)

    step2 = []
    for i in range(len(step1)):
        row = step1.pop(0)
        for i2 in range(len(row)):
            if row[i2] == 1:
                row[i2] = 0
            elif row[i2] == 0:
                row[i2] = 1
        step2.append(row)
    return step2