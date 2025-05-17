#did this a second time. Here it is

def solution():
    # three/two steps
    # first, run len check. Return False if len != len
    # Second, hashmap loop add first word, then check second word. fw_hm = {char:number of times}
    # pop off it as we go through/remove and if hm is null at end return True

    # not possible, one word has more char then the other
    if len(s) != len(t):
        return False

    hm = {}

    for char in s:
        if char not in hm:
            hm[char] = 1
        elif char in hm:
            hm[char] += 1

    # no loop through second word and 'pop'/remove from hm. If none left in hm return True

    for char in t:
        if char not in hm:
            return False
        elif char in hm:
            hm[char] -= 1
            if hm[char] == 0:
                hm.pop(char)

    return True

