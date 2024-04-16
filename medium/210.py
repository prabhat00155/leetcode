"""Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
"""
import collections


class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
    ) -> list[int]:
        sorted_courses = []
        indegree = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        q = collections.deque()

        for c1, c2 in prerequisites:
            indegree[c1] += 1
            edges[c2].append(c1)

        for k, v in enumerate(indegree):
            if v == 0:
                q.append(k)

        while q:
            node = q.popleft()
            sorted_courses.append(node)
            for c in edges[node]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)

        return sorted_courses if len(sorted_courses) == numCourses else []


def test(num_courses, prereq):
    print(Solution().findOrder(num_courses, prereq))


test(2, [[1, 0]])
test(2, [[1, 0], [0, 1]])
test(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
test(1, [])
