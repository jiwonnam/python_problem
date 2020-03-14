import math
import sys


def euclidean_distance(point, center):
    sum = 0
    for d in range(len(point)):
        sum += (point[d] - center[d]) ** 2

    return math.sqrt(sum)

# #test
# p1 = [1, 5]
# c1 = [1, 3]
# result = distance(p1, c1)
# if 2 == result:
#     print "yes"
# else:
#     print "not true"
#
# exit(1)


with open('input.txt', 'r') as f:
    points = []
    line_count = 0
    for s in f:
        line_count += 1
        if line_count == 1:  # header
            k, m = s.strip().split(" ")
        else:
            temp = s.strip().split(" ")
            temp_list = []
            for d in range(len(temp)):
                temp_list.append(float(temp[d]))
            points.append(temp_list)

    centers = [points[0]]  # first point is the first center
    while len(centers) < int(k):
        max_dist = 0
        max_point = None
        for point in points:
            min_dist = sys.maxsize
            for center in centers:
                dist = euclidean_distance(point, center)
                if dist < min_dist:
                    min_dist = dist

            if min_dist > max_dist:
                max_dist = min_dist
                max_point = point

        centers.append(max_point)

    for center in centers:
        for d in range(len(center)):
            print center[d],
        print ""
