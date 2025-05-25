"""
Salary Calculation Module

According your hourly salary, daily working hour and workdays,
this module can tell you how much you earned each second. It can track total work duration.
"""

from datetime import datetime
import time


class SalaryTracker:
    def __init__(self, monthly_salary, daily_hours, work_days):
        self.monthly_salary = monthly_salary
        self.daily_hours = daily_hours
        self.work_days = work_days
        self.start_time = None
        self.running = False

        total_seconds = daily_hours * work_days * 3600
        self.earnings_per_second = monthly_salary / total_seconds if total_seconds != 0 else 0
        self.total_seconds = total_seconds

    def start_tracking(self):
        self.start_time = time.time()
        self.running = True

    def calculate_earnings(self):
        if not self.start_time:
            return "Tracking not started!"

        elapsed_seconds = time.time() - self.start_time
        current_time = datetime.now().strftime('%H:%M:%S')

        # calculate earned
        earned = elapsed_seconds * self.earnings_per_second

        return f"Current earnings: ${earned:.2f} | Last update: {current_time}"
