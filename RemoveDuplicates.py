#este problema nos pide eliminar duplicados de un arreglo pero sin afectar el orden del arreglo
#este arreglo nos tiene que dar el resultado de cuantos numeros fueron eliminados y el arreglo restante

class Solution:
    def removeDuplicates(self, nums:int) -> int:
        if not nums:
            return 0
        #si en la lista de nums no hay numero devolvemos 0
        i = 0
        #hay que iniciar un contador para recorrer el arreglo y ver cuales son iguales
        # Recorremos el arreglo desde la segunda posición (índice 1)
        for j in range(1, len(nums)):
            # Si el número actual es diferente al último número único guardado
            if nums[j] != nums[i]:
                # Avanzamos 'i' porque encontramos un nuevo número único
                i += 1
                # Guardamos ese nuevo número en la posición 'i'
                nums[i] = nums[j]
                #aqui se mueven los datos en el mismo arreglo y se agregan a su nueva posicion
                #si hay un numero repetido el algoritmo lo salta y si hay un numero diferente lo sobrescribe para tener solo los diferentes
        return i + 1  
nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)
print(k)  
print(nums[:k])  
