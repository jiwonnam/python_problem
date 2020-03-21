def minimumBribes(q):
    is_too_chaotic = False
    count = 0
    minus = []
    # diff_array = []
    for i in range(len(q)):
        diff = q[i] - (i + 1)
        # diff_array.append(diff)
        if diff <= 0:
            minus.append(q[i])
        else:
            if diff > 2:
                is_too_chaotic = True
                break
            else:
                count += diff
    '''print q
    print diff_array
    print minus'''

    if is_too_chaotic:
        print "Too chaotic"
    else:
        for i in range(len(minus)-1, 0, -1):
            if minus[i-1] > minus[i]:
                count += 1
                temp = minus[i-1]
                minus[i-1] = minus[i]
                minus[i] = temp
        print count

def test_minimumBribes():
    # test case 0
    q = [1]
    true_answer = 0
    answer = minimumBribes(q)
    assert true_answer == answer

    # test case 1
    q = [2, 3, 4, 5, 1]
    true_answer = 4
    answer = minimumBribes(q)
    assert true_answer == answer

    # test case 2
    q = [3, 2, 4, 5, 1]
    true_answer = 5
    answer = minimumBribes(q)
    assert true_answer == answer

    # test case 3
    q = [2, 1]
    true_answer = 1
    answer = minimumBribes(q)
    assert true_answer == answer

    # test case 4
    q = [3, 2, 1]
    true_answer = 3
    answer = minimumBribes(q)
    assert true_answer == answer


if __name__ == '__main__':
    # test_minimumBribes()

    t = int(raw_input())
    for t_itr in range(t):
        n = int(raw_input())
        q = map(int, raw_input().strip().split())
        minimumBribes(q)
