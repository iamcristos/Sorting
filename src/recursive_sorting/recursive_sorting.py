import math
# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    # elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    # TO-DO
    merged_arr = []
    while(len(arrA) and len(arrB)):
        if(arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
        else:
            merged_arr.append(arrB.pop(0))
    while(len(arrA)):
        merged_arr.append(arrA.pop(0))
    while(len(arrB)):
        merged_arr.append(arrB.pop(0))
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr) < 2):
        return arr
    middle = math.floor(len(arr)/2)
    left = arr[:middle]
    right = arr[middle:]
    arrA = merge_sort(left)
    arrB = merge_sort(right)
    return merge(arrA,arrB)


print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
