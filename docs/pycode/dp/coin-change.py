class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rs = [amount + 1] * (amount + 1)
        rs[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i - c] + 1)

        if rs[amount] == amount + 1:
            return -1
        return rs[amount]


tm = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([], 11, -1),
]

if __name__ == "__main__":

    sol1 = Solution()

    for idx, nin in enumerate(tm):
        resout = sol1.coinChange(nin[0], nin[1])
        print(nin, resout, resout == nin[-1])