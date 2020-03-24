from collections import defaultdict


def checkMagazine(magazine, note):
    s1 = defaultdict(int)
    s2 = defaultdict(int)

    for word1 in magazine:
        s1[word1] += 1

    for word2 in note:
        s2[word2] += 1

    for word, count2 in s2.items():
        count1 = s1[word]
        if count2 > count1:
            return 'No'

    return 'Yes'


if __name__ == '__main__':
    m, n = map(int, raw_input().split())

    magazine = raw_input().rstrip().split()
    note = raw_input().rstrip().split()
    result = checkMagazine(magazine, note)
    print result
