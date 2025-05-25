"""
main.py

Coordinates all modules through a unified menu interface. Handles user input
routing and result display. Maintains system operation and error handling.
"""

from salary_calculator import SalaryTracker
from time_manager import TimeManager
from food_chooser import FoodChooser
from todo_list import TodoList
import time


def display_header():
    print("\n" + "=" * 40)
    print("=== Salary Calculator System ===".center(40))
    print("=" * 40)


def main():
    wage = float(input("Enter monthly salary ($): "))
    hours = float(input("Daily working hours: "))
    days = int(input("Working days per month: "))

    salary_tracker = SalaryTracker(wage, hours, days)
    salary_tracker.start_tracking()


    fc = FoodChooser()
    todo = TodoList()

    try:
        while True:
            display_header()
            print("1. Check Current Earnings")
            print("2. Time Management Tools")
            print("3. Food Recommendation")
            print("4. Todo List Manager")
            print("5. Exit System")


            while True:
                choice = input("\nEnter your choice (1-5): ")
                if choice in {'1', '2', '3', '4', '5'}:
                    break
                print("Invalid input! Please enter a number between 1-5")

            if choice == '1':
                print("\n" + "-" * 40)
                print(salary_tracker.calculate_earnings())
                input("\nPress Enter to continue...")

            elif choice == '2':
                print("\n" + "-" * 40)
                print("[ Time Management Toolkit ]")
                print(f"Days until weekend: {TimeManager.days_until_weekend()}")

                while True:
                    holiday_date = input("Enter next holiday date (YYYY-MM-DD): ")
                    result = TimeManager.days_until_holiday(holiday_date)
                    if isinstance(result, int):
                        print(f"Days until holiday: {result}")
                        break
                    print(f"Error: {result}. Please try again.")

                while True:
                    pay_day = input("Enter payday day (1-31): ")
                    if pay_day.isdigit() and 1 <= int(pay_day) <= 31:
                        print(f"Days until payday: {TimeManager.days_until_payday(int(pay_day))}")
                        break
                    print("Invalid input! Please enter a number between 1-31")

                input("\nPress Enter to continue...")

            elif choice == '3':
                print("\n" + "-" * 40)
                print("[ Food Recommendation System ]")
                print("Recommended:", fc.choose())

                if input("\nAdd custom item? (y/n): ").lower() == 'y':
                    fc.add_item(
                        input("Cuisine type (Western/Asian): ").title(),
                        input("Temperature (Cold/Hot): ").title(),
                        input("Spice level (Light/Spicy): ").title(),
                        input("Food name: ")
                    )
                    print("New item added successfully!")
                input("\nPress Enter to continue...")

            elif choice == '4':
                while True:
                    print("\n" + "-" * 40)
                    print("[ Todo List Manager ]")
                    print(todo.show_tasks())
                    action = input("\nChoose action (add/remove/complete/back): ").lower()

                    if action == 'back':
                        break

                    elif action == 'add':
                        task = input("Enter new task: ")
                        print(todo.add_task(task))

                    elif action == 'remove':
                        try:
                            task_num = int(input("Enter task number to remove: "))
                            print(todo.remove_task(task_num))
                        except ValueError:
                            print("Invalid input!")

                    elif action == 'complete':
                        try:
                            task_num = int(input("Enter task number to complete: "))
                            print(todo.complete_task(task_num))
                            print(todo.show_tasks())
                        except ValueError:
                            print("Please enter a valid number")
                    else:
                        print("Invalid action (valid: add/remove/complete/back)")

                    input("\nPress Enter to continue...")

            elif choice == '5':
                print("\nExiting system...")
                break

    except KeyboardInterrupt:
        print("\nSystem terminated by error.")


if __name__ == "__main__":
    main()