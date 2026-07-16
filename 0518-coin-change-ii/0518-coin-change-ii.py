class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        arr=[0]*(amount+1)
        arr[0]=1
        for coin in coins:
            for i in range(coin,amount+1):
                arr[i]+=arr[i-coin]
        return arr[-1]