import math

a = int(raw_input('Enter an interger to be assigned to variable a: '))
b = int(raw_input('Enter an interger to be assigned to variable b: '))
print 'The sum of ' + str(a) + ' and ' + str(b) + ' is: %i' % (a + b)
print 'The difference when ' + str(b) + ' is subtracted from ' + str(a) + ' is: %i' % (b - a)
print 'The product of ' + str(a) + ' and ' + str(b) + ' is: %i' % (a * b)
print 'The quotient when ' + str(a) + ' is divided by ' + str(b) + ' is: %i' % (a // b)
print 'The remainder when ' + str(a) + ' is divided by ' + str(b) + ' is: %i' % (a % b)
print 'The result of ' + str(a) + '**' + str(b) + ' is: %i' % (a ** b)
print 'The result of log base 10 of ' + str(a) + ' is: %f' % math.log10(a)
