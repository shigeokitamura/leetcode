# https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant_queue = []
        dire_queue = []

        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                radiant_queue.append(i)
            else:
                dire_queue.append(i)

        while len(radiant_queue) != 0 and len(dire_queue) != 0:
            radiant = radiant_queue.pop(0)
            dire = dire_queue.pop(0)
            n += 1

            if radiant < dire:
                radiant_queue.append(n)
            else:
                dire_queue.append(n)

        if len(radiant_queue) > 0:
            return "Radiant"
        return "Dire"


if __name__ == "__main__":
    s = Solution()

    print(s.predictPartyVictory("RD")) # "Radiant"
    print(s.predictPartyVictory("RDD")) # "Dire"
