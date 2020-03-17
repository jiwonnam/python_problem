def repeatedString(s, n):
    count = 0
    count_temp = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count += 1
        if i == n%len(s)-1:
            count_temp = count
    result = n/len(s)*count + count_temp
    return result

s = raw_input()
n = int(raw_input())
result = repeatedString(s, n)
print(result)

