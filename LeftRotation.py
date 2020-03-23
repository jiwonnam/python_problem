def rotLeft(a, d):
    n_arr = ['' for i in range(len(a))]
    for i in range(len(a)):
        if i - d < 0:
            index = i - d + len(a)
        else:
            index = i - d
        n_arr[index] = a[i]
    return n_arr


if __name__ == '__main__':
    nd = raw_input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = raw_input().rstrip().split()

    result = rotLeft(a, d)
    print (' '.join(result))  # print list including str without comma
