"""Course Schedule
https://leetcode.com/problems/course-schedule/
"""
import collections


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        sorted_courses = 0
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
            vertex = q.popleft()
            sorted_courses += 1
            for node in edges[vertex]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)

        return sorted_courses == numCourses


def test(num_courses, prereq):
    print(Solution().canFinish(num_courses, prereq))


test(2, [[1, 0]])
test(2, [[1, 0], [0, 1]])
