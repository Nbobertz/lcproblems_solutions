"""
This is a two pointer approach on boats to save people
"""

people.sort()
i, j = 0, len(people) - 1
boats = 0

while i <= j:
    if people[i] + people[j] <= limit:
        i += 1  # lightest person goes with heaviest
    j -= 1  # heaviest person always goes
    boats += 1  # count the boat

return boats