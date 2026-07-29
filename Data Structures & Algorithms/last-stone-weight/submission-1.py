class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def smash (stones):
            stones.sort()
            if not stones: return 0
            if len(stones) == 1: return stones[0]


            x = stones.pop()
            y = stones.pop()

            if x > y:
                stones.append(x - y)
                stones.sort()

            return smash(stones)

        return smash(stones)