N = int(input())
num_lis = sorted(list(map(int, input().split())))
M = int(input())
compare = list(map(int, input().split()))


def binarySearch(arr, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return 1

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    # Element is not present in the array
    else:
        return 0


for i in compare:
    l = 0
    r = (N - 1)
    while True:
        binarySearch()
