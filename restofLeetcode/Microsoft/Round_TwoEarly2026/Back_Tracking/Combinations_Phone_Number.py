"""
This is combinations for a phone number
"""

if not digits:
    return []

hm = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

answer = []


def dfs(index: int, path: List[str]):
    # base case: processed all digits
    if index == len(digits):
        answer.append("".join(path))
        return

    # choose one letter for current digit
    for ch in hm[digits[index]]:
        path.append(ch)
        dfs(index + 1, path)
        path.pop()


dfs(0, [])
return answer