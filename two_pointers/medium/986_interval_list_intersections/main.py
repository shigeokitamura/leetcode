# https://leetcode.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if len(firstList) == 0 or len(secondList) == 0:
            return []

        first_max = firstList[-1][1]
        second_max = secondList[-1][1]
        ans_max = max(first_max, second_max)

        a = b = False
        i = a_i = b_i = 0
        ans = []
        pointer = 0
        intersect = False

        while i <= ans_max:
            if firstList[a_i][0] <= i <= firstList[a_i][1]:
                a = True
            else:
                a = False
                if firstList[a_i][1] < i:
                    if a_i < len(firstList):
                        a_i += 1

            if secondList[b_i][0] <= i <= secondList[b_i][1]:
                b = True
            else:
                b = False
                if secondList[b_i][1] < i:
                    if b_i < len(secondList):
                        b_i += 1

            print(i, a, b)

            if intersect == False:
                if a == True and b == True:
                    pointer = i
                    intersect = True
            else:
                if a == False or b == False:
                    if intersect:
                        ans.append([pointer, i-1])
                        intersect = False

            i += 1

        return ans


if __name__ == "__main__":
    s = Solution()

    print(s.intervalIntersection(
        [[0,2],[5,10],[13,23],[24,25]],
        [[1,5],[8,12],[15,24],[25,26]]
    )) # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(s.intervalIntersection(
        [[1,3],[5,9]],
        []
    )) # []
