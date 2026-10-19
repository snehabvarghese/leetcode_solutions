from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG = float('-inf')

        # cash[t]: maximum profit with t completed transactions,
        #          and no open position.
        # hold[t]: maximum profit with a normal stock position open.
        # short[t]: maximum profit with a short position open.
        cash = [NEG] * (k + 1)
        hold = [NEG] * (k + 1)
        short = [NEG] * (k + 1)

        cash[0] = 0

        for price in prices:
            # Copy previous-day states so we cannot open and close
            # a transaction on the same day.
            new_cash = cash[:]
            new_hold = hold[:]
            new_short = short[:]

            for t in range(k + 1):
                # Open a normal position or a short position
                if cash[t] != NEG:
                    new_hold[t] = max(new_hold[t], cash[t] - price)
                    new_short[t] = max(new_short[t], cash[t] + price)

                # Close a transaction, if one has already been opened
                if t > 0:
                    new_cash[t] = max(
                        new_cash[t],
                        hold[t - 1] + price,
                        short[t - 1] - price
                    )

            cash, hold, short = new_cash, new_hold, new_short

        return max(cash)