class Solution:
    def finalPrices(self, prices: List[int], use_stack: bool = True) -> List[int]:
        """
        Combined solution for Final Prices:
        1. Brute Force Approach: O(n^2)
        2. Monotonic Stack Approach: O(n)

        :param prices: List[int] - The list of item prices.
        :param use_stack: bool - If True, use the Monotonic Stack approach; otherwise, use Brute Force.
        :return: List[int] - Updated list of final prices after applying discounts.
        """
        
        # M - Match with Patterns
        # - Brute Force uses nested loops to find the first smaller/equal element.
        # - Monotonic Stack efficiently processes the array in linear time.

        # Brute Force Approach
        if not use_stack:
            for i in range(len(prices) - 1):
                j = i + 1
                while j < len(prices) and prices[i] < prices[j]:
                    j += 1
                if j < len(prices) and prices[i] >= prices[j]:
                    prices[i] -= prices[j]
            return prices

        # Monotonic Stack Approach
        stack = []
        for i in range(len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                index = stack.pop()
                prices[index] -= prices[i]
            stack.append(i)
        return prices
