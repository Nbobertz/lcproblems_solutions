#here we are given a string and asked to reverse all vowels in the string. The upper capped vowels will have to be replaced as uppercap.

s = "IceCreAm"

def solution():
    l, r = 0, len(s) - 1

    # edge constraint? If we ecounter an uppe cap can we only transfer with upper cap?
    # 'Iaddae'
    # 'eaddaI'
    # loop through s, if l lands on vowel then we simply need to wait for r to land on vowel or vice versa.

    slist = list(s)
    # const array
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    if len(s) == 1 or len(s) == 0:
        return s

    while l < r:
        char1 = slist[l]
        char2 = slist[r]

        # handles if they are normal letters
        if char1 not in vowels:
            l += 1
        if char2 not in vowels:
            r -= 1

        # what if we encounter left is vowel?
        if char1 in vowels and char2 in vowels:
            tmp_1 = char1
            tmp_2 = char2

            # replace
            slist[l] = tmp_2
            slist[r] = tmp_1

            l += 1
            r -= 1

        answer = ''.join(slist)
    return answer

def optimal():
    vowels = [i for i in s if i in "aeiouAEIOU"]
    result = [i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
    return "".join(result)