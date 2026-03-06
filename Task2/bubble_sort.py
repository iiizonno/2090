def bubble_sort(arr: list[int]) -> None:
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            break
            
