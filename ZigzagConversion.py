#leet code aqui nos pide que le devolvamos cuantos renglones tiene una palabra en formato de zig zag
#se me complico un tanto la logica pero logre hacer un codigo basico a este problema pero no funciona para todos los casos
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        Rows = [""] * numRows
        actualRow = 0
        direction = 1
        #primero debemos de crear las variables, estas son muy importantes ya que el problema del zig zag requiere moverse mucho entre los renglones
        #necesitamos saber en que direccion y en que renglon esta nuestro programa

        for letter in s:
        #aqui iniciamos un ciclo for ya que tenemos que recorrer la palabra para saber pues cuantos renglones tiene
            Rows[actualRow] += letter
            #aqui agregamos las letras con forme vayan saliendo en nuestros renglones, si en nuestro renglon actual tenemos una letra se va a agregar a esa lista de rows
            if actualRow == numRows -1:
                direction = -1
            elif actualRow == 0:
                direction= 1
            #aqui vemos si tenemos que ir para arriba o para abajo, si nuestro renglon actual esta por debajo del numero de nuestros renglones esta ira hacia abajo, y lo mismo con el 1
            actualRow += direction
        
        resultado = ""
        for fila in Rows:
            resultado += fila
        return resultado
        #al final necesitamos juntar todos nuestros diferentes renglones, para eso es este otro ciclo for
        #tenemos una lista vacia de resultados y en nuestro ciclo de renglones ya tenemos el resultado guardado asi que aqui solo juntamos esas listas para que nos de el resultado completo


Sol = Solution()
result = Sol.convert("PAHNAPLSIIGYIR", 3)
print(result)
            