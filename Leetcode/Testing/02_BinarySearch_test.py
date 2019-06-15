def binary_search_rec(a, key, low, high):
    if low > high:
        return -1

    mid = low + ((high - low) // 2)
    if a[mid] == key:
        return mid
    elif key < a[mid]:
        return binary_search_rec(a, key, low, mid - 1)
    else:
        return binary_search_rec(a, key, mid + 1, high)


def binary_search(a, key):
    return binary_search_rec(a, key, 0, len(a) - 1)


def linear_search(a, key):
    for i in xrange(0, len(a)):
        if a[i] == key:
            return i
    return -1


def test_bin_search(arr, key, expected):
    arr.sort()
    i = linear_search(arr, key)
    j = binary_search(arr, key)

    assert i == j

    if expected == True:
        assert j >= 0
    else:
        assert j == -1

    print "Linear Search Key found at " + str(i),
    print ", Binary Search Key found at " + str(j)


def main():
    arr = [5, 3, 2, 9, 7]
    test_bin_search(arr, 5, True)
    test_bin_search(arr, 15, False)

    arr = create_random_int_array(100)
    test_bin_search(arr, arr[0], True)
    test_bin_search(arr, 1005, False)

    test_bin_search([], 100, False)
    test_bin_search([55], 50, False)
    test_bin_search([55], 55, True)

    print "********Complete*******"


main()



########
#
# Output
#
# Linear Search Key found at 2 , Binary Search Key found at 2
# Linear Search Key found at -1 , Binary Search Key found at -1
# Linear Search Key found at 86 , Binary Search Key found at 86
# Linear Search Key found at -1 , Binary Search Key found at -1
# Linear Search Key found at -1 , Binary Search Key found at -1
# Linear Search Key found at -1 , Binary Search Key found at -1
# Linear Search Key found at 0 , Binary Search Key found at 0
# ********Complete*******

