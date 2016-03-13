def insertionSort(x):
    '''Insetion sort algorithm

    Takes a list of integers and sorts them using the Insertion Sort algorithm.'''
    for i in range(1, len(x)):
        currentValue = x[i]
        position = i

        while position > 0 and x[position - 1] > currentValue:
            x[position] = x[position - 1]
            position = position - 1

        x[position] = currentValue
    print(x)

myList = [1, 55, 4, 6, 76, 12, 34, 100, 54, 54, 54]
insertionSort(myList)


