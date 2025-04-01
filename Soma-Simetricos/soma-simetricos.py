def soma_simetricos (lista, indice):
    if indice < 0 or indice >= len(lista):
        raise ValueError("Fora do escopo")
    
    indice_simetricos = len(lista) - 1 - indice

    return lista[indice] + lista[indice_simetricos]

lista = [1,2,3,4,5,6,7,8,9,10]
indice = 2
resultado = soma_simetricos(lista, indice)
print(f"Resultado: {resultado}")