#Simple sorting algorithim
#Simple implementation
#Quadratic running time O(n^2)
#sorted|unsorted

def insertion_sort(arr):
    #1-6
    for index in range(1, len(arr)):
        current = index
        #left num is greater than curr
        while arr[current-1] > arr[current] and current > 0:
            #special notation for swapping
            arr[current - 1], arr[current] = arr[current], arr[current - 1]
            #goes to the start of the arr[0]
            current -= 1
        



arr = [2,6,5,1,3,4]
insertion_sort(arr)
print(arr)