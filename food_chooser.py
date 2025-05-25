"""
Food Recommendation Module

Manages food selection through preferences (cuisine/temperature/spice).
Supports adding menu and random suggestion.
"""

import random

class FoodChooser:
    def __init__(self):
        self.menu = {
            'Western': {
                'Cold': {'Light': ['Prawn Salad', 'Ham Sandwich'],
                         'Spicy': ['Salmon Tartare']},
                'Hot': {'Light': ['Chicken Soup', 'Mashed Potatoes'],
                        'Spicy': ['Buffalo Wings', 'Pepperoni Pizza']}
            },
            'Asian': {
                'Cold': {'Light': ['Sushi', 'Spring Rolls'],
                         'Spicy': ['Iced Noodle']},
                'Hot': {'Light': ['Wonton Noodle', 'Dumplings'],
                        'Spicy': ['Hot Pot', 'Dry-Fried Chili Chicken']}
            }
        }
    # You can add any food you like!
    def add_item(self, cuisine, temp, spice, item):
        self.menu[cuisine][temp][spice].append(item)

    def choose(self):
        cuisine = input("Cuisine (Western/Asian): ").title()
        temp = input("Temperature (Cold/Hot): ").title()
        spice = input("Spice (Light/Spicy): ").title()

        try:
            options = self.menu[cuisine][temp][spice]
            return random.choice(options) if options else "No options available"
        except KeyError:
            return "Invalid selection"