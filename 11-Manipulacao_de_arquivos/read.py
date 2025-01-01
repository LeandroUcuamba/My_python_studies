#open("caminha", "r")

#Mode

# r -> Leitura
# a -> Append / Incrementar
# w -> Escrita
# x -> Criar arquivo
# r+ -> Leitura + Escrita

arquivo = open("11-Manipulacao_de_arquivos/test.txt", "r")

print(arquivo.readable()) # Ver se arquivo pode ser lido.

print("\n#####################\n")

# print(arquivo.read()) # Ler todo arquivo.

print("\n#####################\n")

# print(arquivo.readline()) # Ler e retorna a primeira linha do arquivo "Java";

print("\n#####################\n")

lista = arquivo.readlines()
print(lista)


arquivo.close()