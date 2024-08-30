class nodo:
    def __init__(self,valor,siguiente):
        self.valor = valor
        self.siguiente = siguiente

def mostrar(nodo):
    while nodo != None:
        print(nodo.valor, end=" -> ")
        nodo = nodo.siguiente
    print('None')

nodo5=nodo(600,None)
nodo4=nodo(400,nodo5)
nodo3=nodo(300,nodo4)
nodo2=nodo(200,nodo3)
nodo1=nodo(100, nodo2)

mostrar(nodo1)

nodo_cambio_dato=nodo1.siguiente.siguiente
nodo_cambio_dato.valor=333

mostrar(nodo1)

nodo_nuevo= nodo(700, None)
nodo1.siguiente.siguiente.siguiente.siguiente.siguiente= nodo_nuevo

mostrar(nodo1)

nodo1= nodo(50, nodo1)
mostrar(nodo1)

