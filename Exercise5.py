OneLiterorLess = int(raw_input('How many one liter of less containers?: '))
MoreThanOneLiter = int(raw_input('How many more than one liter containers?: '))
TotalRefund = float(OneLiterorLess * 0.10) + float(MoreThanOneLiter * 0.25)
print 'Your total refund is $%.2f' % TotalRefund
