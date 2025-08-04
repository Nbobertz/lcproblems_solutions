class Solution(object):
    def phonePrefix(self, numbers):
        # Sort numbers so any prefix would appear just before the number it prefixes
        numbers.sort()

        for i in range(len(numbers) - 1):
            # If current number is a prefix of the next one
            if numbers[i + 1].startswith(numbers[i]):
                return False
        return True