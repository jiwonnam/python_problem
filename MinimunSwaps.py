
'''def minimumSwaps(arr, n):
    count = 0
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
            count += 1
    return count'''

def minimumSwaps(arr):
    sort = []
    count = 0
    time = 0
    for i in range(len(arr)):
        if i+1 == arr[i]:
            continue
        else:
            sort.append(i)

    for j in sort:
        if j+1 == arr[j]:
            continue
        else:
            while 1:
                # print arr[j], arr[arr[j]-1]
                temp = arr[arr[j]-1]
                arr[arr[j]-1] = arr[j]
                arr[j] = temp
                count += 1
                # print arr, count
                if arr[j] == j+1:
                    break
    return count


if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().rstrip().split())
    res = minimumSwaps(arr)
    print res

