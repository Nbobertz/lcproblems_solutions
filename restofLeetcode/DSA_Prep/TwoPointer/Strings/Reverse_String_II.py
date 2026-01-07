"""
This is for reversing a secition of each string
"""

s = list(s)

for i in range(0, len(s), 2 * k):
    s[i:i+k] = reversed(s[i:i+k])

return ''.join(s)