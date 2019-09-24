class Solution:
    # 暴力循环
    def get_max_profit_1(self, prices):
        if not prices:
            return 0
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    # 寻谷和峰
    def get_max_profit_2(self, prices):
        if not prices:
            return 0

        minuium_price = float("inf")
        max_profit = 0

        for idx in range(len(prices)):
            if prices[idx] < minuium_price:
                minuium_price = prices[idx]
            elif prices[idx] - minuium_price > max_profit:
                max_profit = prices[idx] - minuium_price

        return max_profit

    # 动态规划
    def get_max_profit_3(self, prices):
        if not prices:
            return 0

        max_profit = 0
        tmp_profit = 0
        for idx in range(1, len(prices)):
            tmp_profit += prices[idx] - prices[idx - 1]
            if tmp_profit > max_profit:
                max_profit = tmp_profit
            elif tmp_profit < 0:
                tmp_profit = 0

        return max_profit

    # 动态规划精简版 的另一个版本
    def get_max_profit_4(self, prices):
        if not prices:
            return 0

        tmp_profit, max_profit = 0, 0
        for idx in range(1, len(prices)):
            tmp_profit = max(0, tmp_profit + prices[idx] - prices[idx - 1])
            max_profit = max(max_profit, tmp_profit)
        return max_profit
