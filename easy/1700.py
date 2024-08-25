"""Number of Students Unable to Eat Lunch
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch
"""


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        rem = len(students)
        i, j, traversed = 0, 0, 0
        while rem > 0 and traversed < len(students):
            while students[i] == -1:
                i = (i + 1) % len(students)
                traversed += 1
            while sandwiches[j] == -1:
                j = (j + 1) % len(sandwiches)
            if students[i] == sandwiches[j]:
                students[i], sandwiches[j] = -1, -1
                traversed = 0
                rem -= 1
                j = (j + 1) % len(sandwiches)
            i = (i + 1) % len(students)
            traversed += 1
        return rem


def test(students: list[int], sandwiches: list[int]):
    print(Solution().countStudents(students, sandwiches))


test([1, 1, 0, 0], [0, 1, 0, 1])
test([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])
