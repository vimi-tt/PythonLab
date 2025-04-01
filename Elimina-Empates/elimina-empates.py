def elimina_empates(lista):    
    contagem = {}
    
    indices_repetidos = []

    for i,num in enumerate(lista):
        if num in contagem:
            contagem[num] += 1
            indices_repetidos.append(i)
        else:
            contagem[num] = 1
    
    if indices_repetidos:
        for i in indices_repetidos:
            lista[i] += 1

    return lista

sequencia = [1,2,5,5,5]
nova_sequencia = elimina_empates(sequencia)

print(f"{nova_sequencia}")