#File for functions used throughout game
import random
import math

def sort_objects(x):
    '''Order objects by value

    Takes list of objects, each with a value attribute and orders'''
    for i in range(len(x) - 1):
        for i in range(len(x) - 1):
            if x[i].value < (x[i + 1].value):
                tmp = x[i + 1]
                x[i + 1] = x[i]
                x[i] = tmp
    return x

def calculate_distance(x1, y1, x2, y2):
    '''Calculate distance between two coordinates

    Takes 2 sets of coordinates, and calculates the distance between using
    Pythagoras's theorem'''
    width = math.sqrt((x2 - x1)**2)
    height = math.sqrt((y2 - y1)**2)
    return math.sqrt(width**2 + height**2)

def random_move():
    '''Generates a movement in a random direction

    Moves the player sprite by one tile in a random direction'''
    #True equates to x, False equates to y
    #direction = random.choice([True, False])
    #value = random.choice([-1, 1])
    return (direction, value)


    
def search_objects(x, v):
    '''Search list for specific value

    Function takes a sorted list of integers (x) and finds a specific value (v),
    using a binary search'''
    found = False
    first = 0
    last = len(x) - 1
    while ((not found) and first <= last):
        mid = (first + last) // 2
        if x[mid] == v:
            found = True
        else:
            if v < x[mid]:
                last = mid - 1
            else:
                first = mid + 1
        return found
            

def gen_coordinates(xlower, xupper, ylower, yupper):
    '''Generates a random x and y coordinate

    Takes 4 integers, two lower and two upper ranges, returns tuple'''
    return (random.randrange(xlower, xupper), random.randrange(ylower, yupper))


def disperse(rows, columns, density, upper_range, my_list):
    '''Function returns array of locations

    Takes probabilities and densities'''
    if [rows + 1, columns] in my_list or \
            [rows - 1, columns] in my_list or \
            [rows, columns + 1] in my_list or \
            [rows, columns - 1] in my_list or \
            [rows + 1, columns + 1] in my_list or \
            [rows + 1, columns - 1] in my_list or \
            [rows - 1, columns + 1] in my_list or \
            [rows - 1, columns - 1] in my_list:
                if random.randrange(upper_range) < density:
                    my_list.append([rows, columns])
    elif (random.randrange(1000) > 1000 - density):
        my_list.append([rows, columns])

    return my_list
