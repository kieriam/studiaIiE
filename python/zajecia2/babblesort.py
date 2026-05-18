NIU = [1,0,3,6]

#NIU[0],NIU[1] = NIU[1],NIU[0]

def bubbleRos(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if (lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


niu_rosnaco = bubbleRos(NIU)
print(niu_rosnaco)