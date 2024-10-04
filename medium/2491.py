"""Divide Players Into Teams of Equal Skill
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill
"""


class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        i, j = 0, len(skill) - 1
        total = skill[i] + skill[j]
        output = skill[i] * skill[j]
        i += 1
        j -= 1
        while i < j:
            if skill[i] + skill[j] != total:
                return -1
            output += skill[i] * skill[j]
            i += 1
            j -= 1
        return output


def test(skill: list[int]):
    print(Solution().dividePlayers(skill))


test([3, 2, 5, 1, 3, 4])
test([3, 4])
test([1, 1, 2, 3])
