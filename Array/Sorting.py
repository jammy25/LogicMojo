def mergeSortFinal(arr, aux, low, high):

    def merge(arr, aux, low, mid, high):
        
        i = low
        k = low
        j = mid + 1

        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                aux[k] = arr[i]
                k += 1
                i += 1
            else:
                aux[k] = arr[j]
                k += 1
                j += 1
        while i <= mid:
            aux[k] = arr[i]
            k += 1
            i += 1
        # while j <= high:
        #     aux[k] = arr[j]
        #     k += 1
        #     j += 1
        
        for i in range(low, high + 1):
            arr[i] = aux[i]

    def mergeSort(arr, aux, low, high):
        
        if high <= low:
            return
        mid = (low + high)//2

        mergeSort(arr, aux, low, mid)
        mergeSort(arr, aux, mid + 1, high)
        merge(arr, aux, low, mid, high)
    return mergeSort(arr, aux, low, high)

    
arr = [8,4,3,12,25,6,13,10]
aux = arr.copy()
mergeSortFinal(arr, aux, 0, len(arr) - 1)
print(arr)