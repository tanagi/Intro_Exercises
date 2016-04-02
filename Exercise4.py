length = float(raw_input('What is the length of the field in feet? '))
width = float(raw_input('What is the width of the field in feet? '))
acres = (length*width)/43560
print 'The area of the field is %.2f acres' % acres
