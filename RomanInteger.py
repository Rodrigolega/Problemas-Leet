class Solution:
        # esta calse llama como valor a una s, esta s es la instancia que nosotros le pasamos al final osea nuestro numero romanp, de aqui en adelante usara ese numero para nuestro programa
    def romanToInt(self, s: str) -> int:
        # Aqui debemos usar un diccionario para guarda el valor de nuestras respectivas letras romanas, asignando el valor a cada una de ellas
        Roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # necesitamos una variable para guardar los valores que arroje nuestro proograma
        total = 0

        # este ciclo for recorre nuestro numero elegido y ve el valor de s osea que longitud tiene nuestro numero romano
        for i in range(len(s)):
            #aqui recorremos nuestra s y la separamos y le damos un valor de 0,1,2 o mas, aqui ya podemos ver en nuestro diccionario cuanto vale cada una de las letras de nuestra s que separamos
            valorRomano = Roman[s[i]]

            # al momento de ya tener los valores debemos saber si se resta o si se suma, en los numeros romanos si el numero menor va antes que el mayor se resta y se suma si es al reves
            # primero debemos verificar que nuestra comparacion se puede hacer, i+1 representa que la operacion puede continuar ya que si hay un numero a la derecha o no porque se sale
            # la siguiente fila nos compara el valor anterior con el que sigue en nuestro diccionario, si nuestro primer numero se compara con el siguiente y es mas grande el programa decide si se resta o se suma
            # agarramos la iteracion 1 o 0 o las que haya y las vamos comparando entre si, si el numero ya no tiene mas valores ahi se detiene 
            if i + 1 < len(s) and valorRomano < Roman[s[i + 1]]:
                total -= valorRomano
            else:
                total += valorRomano

        return total
    
sol = Solution()
print(sol.romanToInt("LVIII"))
#por ultimo se crea el objeto para poder llamar a la calse romantoint

