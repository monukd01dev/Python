l = [50,40,20,10,12,89,2,22,75,68,1]

def bubble_sort(arr):
    length = len(arr);
    #pass
    for j in range(length,1,-1) :
        for i in range(j-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr
bubble_sort(l)  
print(l)      
