#un prefijo es lo comun de las palabras que le pasemos
class Solution:
    def longestCommonPrefix(self, strs:str) -> str:
        #si no hay palabras en nuestra lista que le pasemos que salte el proceso ya que pues no hay nada que hacer
        if not strs:
            return ""
        #primero debemos agarrar nuestra primera palabra para poder decidir cual es nuestro prefijo
        prefix = strs[0]
        #de aqui se va a ir comparando esta palabra con las demas para ver cuales tienen el mismo prefijo
        for word in strs[1:]:
            #con 1: hacemos nuestra sublista para hacer las otras comparaciones para descubrir nuestro prefijp
            # recorremos el arreglo para poder comparar nuestras palabras
            while not word.startswith(prefix):
                #esta es una funcion de python que nos devuelve verdadero o falso si el prefijo es igual
                prefix = prefix[:-1]
                #aqui hacemos las comparaciones con la segunda palabra elegida por el recorrido cada vez mas recortada, si esta palabra no tiene nada igual despues de muchos recortes se salta
                if prefix == "":
                    return ""
                #si nuestro prefijo es igual se agrega a la ista y se devuelve
        return prefix

sol = Solution()
res = sol.longestCommonPrefix(["flower","flow","flight"])
print(res)