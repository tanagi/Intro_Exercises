widgets = 75
gizmos = 112
number_of_widgets = int(raw_input('How many widgets?: '))
number_of_gizmos = int(raw_input('How many gizmos?: '))
print 'Each widget weights 75 grams.'
print 'Each gizmo weighs 112 grams.'
total_weight = ((widgets*number_of_widgets)+(gizmos*number_of_gizmos))
print 'Total weight of your order is %i grams' % total_weight
