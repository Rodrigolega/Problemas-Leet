class Solution:
    def twoMult(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] * nums[j] == target:
                    return [i, j]
        return None

sol = Solution()

arreglo = [2, 7, 11, 15]
target = 14

resultado = sol.twoMult(arreglo, target)

if resultado:
    print(f"Índices encontrados: {resultado}")
else:
    print("No se encontró una pareja que Multiplique el target.")