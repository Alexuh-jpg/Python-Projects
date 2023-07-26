#divide and conquer alglorithim
#breaks down problem into multiple subproblems recursivly until they become simple to solve
#solutions are combined to solve original problem
#O(n*log(n)) running time
#optimal running time for comparision based algorithims

#1. split array in half
#2. call merge sort on each half to sort them recurivly
#3 Merge both sorted halves into one sorted array

def merge_sort(arr):
    if len(arr) > 1:
        #special notaion to get the slice of the arr
        left_arr = arr[:len(arr)//2]#arr[start] to mid point
        right_arr = arr[len(arr)//2:]#mid point to arr[end]

        #recursion
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] =right_arr[j]
                j += 1
            k+=1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
 

arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
merge_sort(arr)
print(arr)