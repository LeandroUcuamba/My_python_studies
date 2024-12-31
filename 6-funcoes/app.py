def fazer_hamburguer(nome):
    print(f" O {nome} pediu para fazer um sanduiche")

fazer_hamburguer("Leandro")
fazer_hamburguer("Ucuamba")


print("\n\n#######################################\n\n")

def soma_numeros(numero1, numero2):
    return numero1 + numero2

resultado = soma_numeros(15,20)

print(f"O resultado é: {resultado}")


print("\n\n#######################################\n\n")

def achar_maior_numero(lista_num):
    lista_num.sort()
    lista_num.reverse()
    achar_maior_numero = lista_num[0]
    return achar_maior_numero

resultadoMaiorNumero = achar_maior_numero([34,5,37,87,45,22,11,7,9])
print(resultadoMaiorNumero)