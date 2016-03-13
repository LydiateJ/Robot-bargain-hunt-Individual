from test_sort import bubble_sort

list1 = [1, 2]
list2 = []
list3 = [2, 4, 3, 6, 959, 12, 5, 8, 5, 3]

def assert_function(a):
    if bubble_sort(a) == sorted(a, reverse=True):
        return True

if (assert_function(list1) and assert_function(list2) and
        assert_function(list3)):
    pass
else:
    raise ValueError('The function no longer operates correctly')
