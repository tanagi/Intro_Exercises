apr = 0.04
account = float(raw_input('How much money do you have in your savings account?: '))
after_first_year = account + (apr * account)
print 'After 1st year, your savings account will have $%.2f.' % after_first_year
after_second_year = after_first_year + (apr * after_first_year)
print 'After 2nd year, your savings account will have $%.2f.' % after_second_year
after_third_year = after_second_year + (apr * after_second_year)
print 'After 3rd year, your savings account will have $%.2f.' % after_third_year
