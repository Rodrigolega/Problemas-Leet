"como primer problema en leet nos encotramos una sume de dos numeros, por lo que entendi ocupamos un arreglo y en ese arreglo encontrar dos numeros que nos resulten en nuestro taget"
"yo la verdad tuve que investigar porque no recordaba como escribirlo pero se que tiene que hacer"

class Solution:
    def twoSum(self, nums, target):
        "este ciclo for nos ayudara a recorrer nuestro arreglo, se le pone len(nums) para que independientemente del arreglo se pueda hacer sin importar su tamano"
        for i in range(len(nums)):
            "se inicia otro ciclo para ver cuales son mis numeros que sumados me dan el target, este suma todos los numeros hasta que me de el target"
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

# Crear una inst ancia de la clase
sol = Solution()

# Datos de entrada
arreglo = [2, 7, 11, 15]
target = 9

# Ejecutar el método
resultado = sol.twoSum(arreglo, target)

if resultado:
    print(f"Índices encontrados: {resultado}")
else:
    print("No se encontró una pareja que sume el target.")