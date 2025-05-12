from typing import List

class Solution:
    def twoMultH(self, nums: List[int], target: int) -> List[int]:
        mapa = {}  # valor -> índice

        for i, num in enumerate(nums):

            if num == 0:
                continue
           
            complemento = target / num

            if complemento in mapa:
                return [mapa[complemento], i]
        

            mapa[num] = i

solu = Solution()
nums = [2, 0, 9, 15]
target = 18
result = solu.twoMultH(nums, target)
print("indices encontrados", result)