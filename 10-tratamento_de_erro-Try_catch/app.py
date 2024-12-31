try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ValueError:
    print("digite um valor valido.")
except:
    print("Erro inesperado.")
finally:
    print("sempre executa!")