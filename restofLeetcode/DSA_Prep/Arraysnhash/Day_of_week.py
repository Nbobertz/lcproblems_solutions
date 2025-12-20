"""
Here we want to return the day of the week from three integers
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        import calendar

        day, month, year = day, month, year
        my_date = datetime.date(year, month, day)
        day_name = my_date.strftime("%A")

        return day_name
