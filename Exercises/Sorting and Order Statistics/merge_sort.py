def merge_sort(array: list):
    print('array : ',array)
    if len(array) > 1:
        mid = len(array)//2

        L = array[:mid]
        print('L : ',L)
        R = array[mid:]
        print('R : ',R)
        merge_sort(L)

        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i]<R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j += 1
            k += 1

            

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


array = [3 ,2,8,5,4]

merge_sort(array)

print(array)