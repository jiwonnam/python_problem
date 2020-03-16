def sockMerchant(n, ar):
    count_arr = [0 for i in range(100)]
    count = 0

    for i in ar:
        if count_arr[i] == 0:
            count_arr[i] = 1
        else: # count_arr[i] == 1
            count_arr[i] = 0
            count += 1
    return count


n = int(raw_input())
print n
ar = map(int, raw_input().strip().split())
print ar

result = sockMerchant(n, ar)
print result

