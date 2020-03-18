
def hourglassSum(arr):
    for j in range(4):
        for i in range(4):
            temp_sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            #print(sum)
            if i==0 and j==0:
                max_sum = temp_sum
            if temp_sum > max_sum:
                max_sum = temp_sum
            #print(max_sum)

    return max_sum


arr = []
for _ in xrange(6):
    arr.append(map(int, raw_input().rstrip().split()))
result = hourglassSum(arr)
print result
