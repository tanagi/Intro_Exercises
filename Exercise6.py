meal_cost = float(raw_input('What is the cost of the meal?: '))
tax = meal_cost * 0.0825
tip_for_meal = meal_cost * 0.18
print 'Cost of Meal: $%.2f' % meal_cost
print 'Tax: $%.2f' % tax
print 'Tip: $%.2f' % tip_for_meal
print 'Grand Total: $%.2f' % (meal_cost+tax+tip_for_meal)
