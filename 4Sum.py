#este codigo nos pide que en base a cuatro arreglos bub=squemos que combinaciones nos dan nuestro target
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
#lo primero que se me ocurrio es resolverlo como el problema de two sum, comparando los numero pero no por fuerza bruta si no algo mas optimizado
#este codigo elige numeros y es por eso que necesitamos agarrar cuatro numeros, i,j,left y right
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
        #necesitamos numero diferentes asi que ocupamos comparar los numero que tenemos, si el numero agarrado es igual al anterior este se tiene que saltar para evitar comparar los dos numeros
                left = j + 1
                right = n - 1
        #aqui creamos nuestras otras dos variables para guardar los demas numeros
                while left < right:
                    suma = nums[i] + nums[j] + nums[left] + nums[right]
        #necesitamos hacer otra comparacion entre left y right para no comparar el mismo numeo
        #luego debemos hacer la suma de estos numero y guardarlos en otra variable de suma
        #en resumen hacemos comparaciones primero para elegir nuestros numeros y que no se repitan, luego debemos sumarlos para despues ver si nos dio nuestro objetivo
                    if suma == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    #aqui tenemos que agregar a nuestra lista del principio los numeros que den nuestro target para despues mostrarlos
                    #probamos diferentes combunaciones moviendolos con +1 y -1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    #estos ciclos while son para no comparar los mismos numeros y movernos a un numero diferente 
                    elif suma < target:
                        left += 1
                    else:
                        right -= 1
                    #apesar de que ya encontramos nuestro target en algunas ocaciones puede que haya otra combinacion usando ese mismo target que encontramos, es por eso que nos tenemos que seguir moviendo aveces con el mismo numero para encontrar todas las combinaciones

        return res

sol = Solution()
Result = sol.fourSum([1,0,-1,0,-2,2], 0)
print(Result)