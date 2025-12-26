"""
Minimum penality for submissions
"""

penalty = customers.count('Y')  # close at hour 0
        min_penalty = penalty
        best_hour = 0

        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1
            else:  # c == 'N'
                penalty += 1

            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = i + 1

        return best_hour