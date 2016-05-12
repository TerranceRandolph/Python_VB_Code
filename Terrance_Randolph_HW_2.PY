"""
Homework 2

    Terrance Randolph.
"""
# previous Box script.

def Box(x, y):

    min_X = 30
    min_Y = 30
    max_X = 60
    max_Y = 50

    if (min_X < x < max_X) and (min_Y< y <max_Y):
        print('({},{}) point is inside of the Box').format(x,y)
        return True
    elif (x < min_X or x > max_X) or (y < min_Y or y > max_Y):
        print('({},{}) point is outside of the Box').format(x,y)
        return False
# write another elif showing which border the point fall on
    elif (min_X == x or x == max_X) or (max_Y == y or y == max_Y) :
        print('({},{}) point is on Box line').format(x,y)
        return False
    else:
        print('input NOT valid')
        return False

#########################
#### formula
#### D = sqrt(dx^2 + dy^2)

def calDistance(x1,y1,x2,y2):
	import math as M
	Distance = M.sqrt(M.pow((x2-x1),2)+ M.pow((y2-y1),2))
	return Distance

def polyLine():
    seg1=calDistance(25.0,36.0,32.0,48.0)
    seg2=calDistance(32.0,48.0,39.0,42.0)
    seg3=calDistance(39.0,42.0,45.0,46.0)
    seg4=calDistance(45.0,46.0,52.0,44.0)
    Len = seg1+seg2+seg3+seg4
    print('The total distance of all five points is {}\n').format(Len)

def Exit():
    if raw_input('Type "Exit" to quit: ') == 'Exit' or 'exit':
	    print('goodbye')
	    quit()
    else:
	    print('Must Type "Exit" to quit\close the program')


#################################

#pt = [25.0,36.0,32.0,48.0,39.0,42.0,45.0,46.0,52.0,44.0]
pt = [(25.0,36.0),(32.0,48.0),(39.0,42.0),(45.0,46.0),(52.0,44.0)]

for index, point in enumerate(pt, 0):
    print(index,point)
    print(' ')

    
polyLine()

print('point 1 relationship to the Box is {}\n').format(Box(25.0,36.0))

print('point 2 relationship to the Box is {}\n').format(Box(32.0,48.0))

print('point 3 relationship to the Box is {}\n').format(Box(39.0,42.0))

print('point 4 relationship to the Box is {}\n').format(Box(45.0,46.0))

print('point 5 relationship to the Box is {}\n').format(Box(52.0,44.0))

Exit()

