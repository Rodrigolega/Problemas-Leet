#este codigo fue sencillo de resolver lo complicado fue hacer todo lo que pide leet code que es que tiene que ser en un rango determinado de 32-bit si se sale de eso debemos retornar 0
class Solution:
   #lo primero que se me vino a la mente fue la funcion de poner al reves los strings con -1 pero obvio no funciona con un numero entero asi qeu lo debemos de convertir a string primero
    def reverse(self, x: int) -> int:
    #si nos dan un numero negativo debemos hacerlo positivo primero porque el simbolo negativo lo requiere al principio, asi que lo quitamos y despues lo ponemos si es que tiene
        pos = str(abs(x))
        #aqui mismo lo convertimos a string
        rev = pos[::-1] 
        #aqui volteamos ese string 
        num = int(rev)
        #aqui lo transformamos otra vez a entero 
        if x < 0:
            num = -num
        #aqui vemo si el numero era negativo y le devolvemos su valor negativo
        if num < -2**31 or num > 2**31 - 1:
            return 0
        #aqui checamos el rango, si se pasa de ese rango devolveos 0
        else:
            return num
        
sol = Solution()
resul = sol.reverse(-123)
print(resul)