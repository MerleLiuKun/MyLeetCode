class Solution:
    def get_max_profit_1(self, prices):
        if not prices:
            return 0

        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - profit[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    def get_max_profit_2(self, prices):
        if not prices:
            return 0

        max_profit = 0
        tmp_profit = 0
        for idx in range(1, len(prices)):
            tmp_profit = prices[idx] - prices[idx - 1]
            if tmp_profit > max_profit:
                max_profit = tmp_profit
            elif tmp_profit < 0:
                tmp_profit = 0

        return max_profit

    def get_max_profit_3(self, prices):
        last, max_profit = 0, 0

        for idx in range(1, len(prices)):
            last = max(0, last + prices[idx] - prices[idx - 1])
            max_profit = max(max_profit, last)
        return max_profit

