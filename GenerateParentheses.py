#este programa nos pide que en base al numero que le demos nos devuelva todas las combinaciones validas de parentesis con ese numero
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        #abrimos una una lista vacia para poder agragar los parentesis que le demos 
        def backtrack(current: str, open_count: int, close_count: int):
            # invetigue acerca del backtracking ya que se requiere para este problema
            #Backtracking es una técnica para construir soluciones paso a paso, probando todas las opciones posibles, pero retrocediendo (deshaciendo pasos) cuando una opción ya no puede llevar a una solución válida.
            if len(current) == 2 * n:
                res.append(current)
                return
            
            # Si aún podemos abrir más paréntesis, lo hacemos
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            #aqui probamos abriendo la cuenta con el parentesis( para probar las combinacines y si funciona se pasa a la siguiente prueba
            # Solo cerramos si hay más abiertos que cerrados
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res


sol = Solution()
Result = sol.generateParenthesis(3)
print(Result)