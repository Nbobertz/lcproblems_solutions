#here we are going to be ggiven a palindrom and our goal is to figure out if we can remmove just one character to make it a palindrom.

s = "abca"

def solution():
    def check_palindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    i = 0
    j = len(s) - 1
    while i < j:
        # Found a mismatched pair - try both deletions
        if s[i] != s[j]:
            return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
        i += 1
        j -= 1

    return True

print(solution())