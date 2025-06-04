#leet code nos pide que usemos listas enlazada, una lista enlazada tiene nodos, estos nodos son los valores de las listas
#mientras tu estas en un nodo siempre se ve al siguiente nodo, esto sirve para eliminar o insertar facilmente datos

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#esto nos lo da leet code, quiere que tenga el valor del nodo el que vamos a guardar y el siguiente numero que esta en la lista

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        #aqui se reciben dos listas enlazadas ordenada, y da como resultado una lista tambien ordenada
        dummy = ListNode()
        current = dummy
        #aqui se crea un dummy, esto para ir agregando los valores a nuestra lista nueva, current ees donde esta el dummy y que numero se agregara

        while list1 and list2:
          #este ciclo while sirve para aclarar que solo compararemos datos mientras tengamos
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
                #aqui se comparan los datos de las listas, si el de la lista es menor que el de la lista 2 este sigue y se usa 
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
                #si el primer valor no es menor que el segundo se ejecuta el else, osea que vamos a guardar el segundo valor en nuestra lista creada para qeu asi este ordenada
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
#como son listas enlazadas no podemos solo imprimir los valores, tenemos que imprimir nodo por nodo asi que se transforma las listas normales que pasemos a listas enlazadas
        # Función para convertir lista normal a lista enlazada
def to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next
    #esta funcion crea una lista enlazada apartir de una lista normal para poder imprimirla

# Función para imprimir la lista enlazada
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Crear las listas enlazadas a partir de listas normales
l1 = to_linked_list([1, 3, 5])
l2 = to_linked_list([2, 4, 6])

sol = Solution()
merged = sol.mergeTwoLists(l1, l2)

print("Lista fusionada:")
print_linked_list(merged)

