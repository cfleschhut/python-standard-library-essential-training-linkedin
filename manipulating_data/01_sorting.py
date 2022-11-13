testScores = [82, 67, 94, 73, 79, 86, 58, 91, 89, 71, 88, 77, 84]


def sort_list(nums, order="asc"):
    return sorted(nums, reverse=(True if order == "desc" else False))


print(testScores)

print(sort_list(testScores))
print(sort_list(testScores, order="desc"))
