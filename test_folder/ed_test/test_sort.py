#Python sorting algorithm (bubble sort)
my_list = [3, 4, 5, 4, 7, 7, 8, 8, 8, 9 , 77, 2, 6, 2, 8, 9, 6, 3]
def bubble_sort(x):
    for i in range(len(x) - 1):
        for i in range(len(x) - 1):
            if x[i] < x[i + 1]:
                tmp = x[i + 1]
                x[i + 1] = x[i]
                x[i] = tmp
            i += 1
        i += 1
    return x
print(bubble_sort(my_list))
