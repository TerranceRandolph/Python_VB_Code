
print('_____ Type your numbers seperated by commas_____')
print('         _____ Example 25,35,65_____            ')
def Mean():
    print("let's find the mean in your number list!!")
    print('')
    
    # The loop takes every interation from the user input
    # and convertes to an intenger, and sotre it
    # in the variable as a list
    
    b = [int(i) for i in input('What are your numbers?: ')]
    k = sum(b)
    s = len(b)
    d = k / s
    print('The Mean Number is {}').format(d)


def Max():
    print("let's find the maxuimum number in your list!!")
    print('')
    b = [int(i) for i in input('What are your numbers?: ')]
    c = max(b)
    print('The Maximum Number is {}').format(c)

def Exit():
    if raw_input('Type "Exit" to quit') == 'Exit' or 'exit':
	    print('goodbye')
	    quit()
    else:
	    print('Must Type "Exit" to quit\close the program')


Mean()
Max()
Exit()
# The code is not sanatized, however the documented code
# is using the given list of numbers.

'''

def Mean():
    b = [23, 2, 34, 25, 98, 12, 24, 9, 21, 19]
    k = sum(b)
    s = len(b)
    d = k / s
    print('The Mean Number is {}').format(d)


def Max():
    b = [23, 2, 34, 25, 98, 12, 24, 9, 21, 19]
    c = max(b)
    print('The Maximum Number is {}').format(c)

Mean()
Max()

'''

