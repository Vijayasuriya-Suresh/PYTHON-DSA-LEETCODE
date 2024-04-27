class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = []

        for i in accounts:
            max_wealth.append(sum(i))

        return max(max_wealth)


