import time
import random

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num / exp > 0:
        count = [0] * 10
        for i in arr:
            count[(i//exp)%10] += 1
        for i in range(1,10):
            count[i] += count[i-1]
        output = [0] * len(arr)
        for i in reversed(range(len(arr))):
            output[count[(arr[i]//exp)%10]-1] = arr[i]
            count[(arr[i]//exp)%10] -= 1
        for i in range(len(arr)):
            arr[i] = output[i]
        exp *= 10
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def counting_sort(arr):
    k = max(arr) + 1
    count = [0] * k
    for i in arr:
        count[i] += 1
    for i in range(1, k):
        count[i] += count[i-1]
    output = [0] * len(arr)
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#Testam sortarea

def test_sort(v):
    x=sorted(v)
    if x==v:
        return "sortat"
    return "nesortat"

n=(int(input("n=")))
maxim=(int(input("max=")))

V=[random.randint(0,maxim) for i in range(n)]
time_start=time.time()
radix_sort(V)
time_stop=time.time()
print("Time for Radix Sort:{0}".format(time_stop-time_start))

V=[random.randint(0,maxim) for i in range(n)]
time_start=time.time()
merge_sort(V)
time_stop=time.time()
print("Time for Merge Sort:{0}".format(time_stop-time_start))

V=[random.randint(0,maxim) for i in range(n)]
time_start=time.time()
shell_sort(V)
time_stop=time.time()
print("Time for Shell Sort:{0}".format(time_stop-time_start))

V=[random.randint(0,maxim) for i in range(n)]
time_start=time.time()
counting_sort(V)
time_stop=time.time()
print("Time for Counting Sort:{0}".format(time_stop-time_start))

V=[random.randint(0,maxim) for i in range(n)]
time_start=time.time()
bubble_sort(V)
time_stop=time.time()
print("Time for Bubble Sort:{0}".format(time_stop-time_start))