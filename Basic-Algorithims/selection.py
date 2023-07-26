#Quadratic running time O(n^2)
#Find the minimum, go through the arr, move it to the front

def selection_sort(arr):
    #0-5
    for index in range(0, len(arr) - 1):
        cur_min_idx = index
        #iterartte the rest of the array after index
        for current_num in range(index + 1, len(arr)):
            #if this number is smaller than the initiallized
            if arr[current_num] < arr[cur_min_idx]:
                cur_min_idx = current_num

        #the current minimum after one iterartion is moved to the index
        #special notation for swapping
        arr[index], arr[cur_min_idx] = arr[cur_min_idx], arr[index]


arr = [2,6,5,1,3,4]
selection_sort(arr)
print(arr)