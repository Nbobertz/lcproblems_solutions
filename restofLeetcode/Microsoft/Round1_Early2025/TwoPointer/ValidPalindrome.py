#here we are given a s string and we have to return if it's a palindrome or not.

s = "A man, a plan, a canal: Panama"

def solution(s):
    l, r = 0, len(s) - 1

    # Convert string to lowercase and check for palindrome
    s = s.lower()

    while l < r:
        # Skip non-alphanumeric characters
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue

        # Compare characters at l and r
        if s[l] != s[r]:
            return False

        # Move towards the center
        l += 1
        r -= 1

    return True


print(solution(s))