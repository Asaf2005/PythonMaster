def binarySearch(array, number, start, end):
    if start <= end:
        mid = (start + end) // 2
        print(mid)
        if array[mid] == number:
            return mid
        elif array[mid] > number:
            return binarySearch(array, number, start, mid-1)
        else:
            return binarySearch(array, number, mid+1, end)
    else:
        return -1

if __name__ == "__main__": #tests
    arr = [0,5,12,23,53]
    print(binarySearch(arr,5,0,len(arr)-1))