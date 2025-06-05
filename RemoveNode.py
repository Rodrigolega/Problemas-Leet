# Este programa nos pide usar listas enlazadas, como las que vimos en clase.
# Una lista enlazada requiere tener dos punteros: uno en el nodo actual y otro al siguiente nodo (next).
# Esto, como vimos en clase, nos ayuda a eliminar datos de forma más sencilla que con arreglos normales.
# Lo que se me ocurre es recorrer todo el arreglo de forma rápida para saber su tamaño,
# y luego ya buscar cuál nodo queremos eliminar desde el final.
# El problema es que el código recibe la cabeza de la lista (head), o sea que debemos eliminar contando desde el final.
# Por eso usamos dos punteros: para encontrar el nodo a eliminar sin tener que calcular el tamaño exacto primero.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Esta clase nos la da LeetCode. Sirve para representar nodos en una lista enlazada.
# Cada nodo tiene un valor y una referencia al siguiente (next).

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Debemos crear un nodo "ancla" (dum) para ubicarnos al inicio de la lista.
        # Esto es útil por si el nodo a eliminar es el primero (head).
        dum = ListNode(0)
        dum.next = head
        # dum sirve como ancla al inicio. Gracias a este nodo podemos eliminar el head fácilmente si es necesario.
        # Los punteros que se moverán para recorrer la lista son fast y slow.
        fast = dum
        slow = dum

        for _ in range(n + 1):
            fast = fast.next
        # Hacemos que fast avance n + 1 pasos para que quede una distancia de n nodos entre fast y slow.

        # Movemos ambos punteros hasta que fast llegue al final.
        while fast:
            fast = fast.next
            slow = slow.next

        # slow.next es el nodo a eliminar, así que lo "saltamos".
        slow.next = slow.next.next

        # Retornamos la lista desde dum.next (porque dum solo era el nodo ancla).
        return dum.next
        # dum solo nos regresa al inicio de la lista para no perder la referencia al principio.
        # fast se adelanta n + 1 pasos para crear una distancia con slow.
        # luego ambos (fast y slow) se mueven juntos hasta que fast llega al final.
        # en ese momento, slow queda justo antes del nodo que queremos borrar.
        # con slow.next = slow.next.next eliminamos ese nodo.
        # al final, devolvemos dum.next que es la cabeza de la lista modificada.

def build_linked_list(values):
    dummy = ListNode(0)  # Creamos un nodo ancla que nos ayuda a construir la lista sin complicaciones.
    current = dummy      # Usamos current para movernos y agregar nodos al final de la lista.

    for val in values:   # Recorremos cada valor del arreglo dado.
        current.next = ListNode(val)  # Creamos un nuevo nodo con el valor actual y lo enlazamos al nodo current.
        current = current.next        # Movemos 'current' al nodo recién creado para poder seguir agregando.

    return dummy.next  # Regresamos la cabeza real de la lista enlazada, que está después del nodo ancla.



def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


sol = Solution()
head = build_linked_list([1, 2, 3, 4, 5])
merged = sol.removeNthFromEnd(head, 2)
print_linked_list(merged)  
