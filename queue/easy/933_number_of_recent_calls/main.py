# https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

class RecentCounter:

    def __init__(self) -> None:
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue[0] < t - 3000:
            self.queue.pop(0)

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

if __name__ == "__main__":
    obj = RecentCounter()

    print([
        obj.ping(1),
        obj.ping(100),
        obj.ping(3001),
        obj.ping(3002),
    ])
