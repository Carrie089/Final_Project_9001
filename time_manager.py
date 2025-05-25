"""
Holiday Calculation Module

Provides time-related functions for the main system. Calculates days until
weekends, custom holidays, and paydays.
"""

from datetime import datetime, date, timedelta

class TimeManager:
    def days_until_weekend():
        today = datetime.now().weekday()  # Monday=0 ... Sunday=6
        return 4 - today if today < 5 else 0  # Days until Friday


    def days_until_holiday(holiday_str):
        try:
            holiday = datetime.strptime(holiday_str, "%Y-%m-%d").date()
            today = datetime.now().date()
            delta = holiday - today
            return max(delta.days, 0)
        except ValueError:
            return "Invalid date format (YYYY-MM-DD required)"

    def days_until_payday(day):
        today = datetime.now()
        try:
            next_payday = today.replace(day=day)
            if next_payday < today:
                next_payday += timedelta(days=30)
            return (next_payday - today).days
        except ValueError:
            return "Invalid payday day (1-31)"