def merge_intervals(intervals):
    if len(intervals) == 0:
        return []

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[j][0] < intervals[i][0]:
                temp = intervals[i]
                intervals[i] = intervals[j]
                intervals[j] = temp

    result = []

    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):

        current_start = intervals[i][0]
        current_end = intervals[i][1]

        if current_start <= end:
            if current_end > start:
                start = current_start
            if current_end > end:
                end = current_end
        else:
            result.append([start, end])
            start = current_start
            end = current_end

    result.append([start, end])

    return result


def test_cases():

    test1 = [[1, 3], [2, 6], [8, 10], [15, 18]]

    test2 = [[1, 4], [4, 5]]

    test3 = [[1, 4], [0, 2], [3, 5]]

    test4 = []

    test5 = [[1, 10], [2, 3], [4, 5], [6, 7]]

    test6 = [[5, 7], [1, 3], [2, 4], [8, 10]]

    test7 = [[1, 2]]

    test8 = [[1, 5], [2, 4], [3, 6], [7, 9]]

    test9 = [[10, 12], [1, 3], [2, 8], [9, 11]]

    test10 = [[1, 1], [1, 1], [1, 1]]

    print("Test 1:", merge_intervals(test1))
    print("Test 2:", merge_intervals(test2))
    print("Test 3:", merge_intervals(test3))
    print("Test 4:", merge_intervals(test4))
    print("Test 5:", merge_intervals(test5))
    print("Test 6:", merge_intervals(test6))
    print("Test 7:", merge_intervals(test7))
    print("Test 8:", merge_intervals(test8))
    print("Test 9:", merge_intervals(test9))
    print("Test 10:", merge_intervals(test10))


test_cases()