#File for functions used throughout game

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
