def heap(arr, n, i):
    largest = i  # largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    if left < n and arr[i] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        heap(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # maxheap
    for i in range(n // 2 - 1, -1, -1):
        heap(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heap(arr, i, 0)

if __name__ == "__main__":

    arr = list(map(int, input("Please enter the numbers separated by space: ").split()))
    heap_sort(arr)
    
    print(arr)

