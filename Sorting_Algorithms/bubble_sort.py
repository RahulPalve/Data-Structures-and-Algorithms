def bubbleSort(arr):
    n = len(arr)
       
    for i in range(n-1):
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
arr = [4, 6, 7, 1 ,2]
 
bubbleSort(arr)

for i in range(len(arr)):
    print ("% d" % arr[i]),