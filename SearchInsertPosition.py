#este problema estaba muy facil ya que en la clase vimos acerca de la busqueda lineal
#aqui solo nos pide buscar un numero en un arreglo asi que solo se tiene que recorrer y ver cual numero es igual a nuestro target
#tambien nos pide que si nuestro target no esta pongamos donde puede ir el target sin afectar el ordend de nuestro arreglo
class Solution:
    def searchInsert(self, nums: int, target: int) -> int:        
        for i in range(len(nums)):
            #debemos recorrer nuestro arreglo para buscar el numero
            if nums[i] >= target:
                return i
            #si encontramos el numero hay que devolverlo
        return len(nums) 
        #si no encontramos nada significa que el numero es mayor que todos por lo tanto lo devolvemos al final
sol = Solution()
res = sol.searchInsert([1,3,5,6], 5)
print(res)