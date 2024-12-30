minha_string = "qualqueR TeXto"
minha_outra_string = " jogador"

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.capitalize())
print(minha_string.isupper())
print(minha_string.islower())
print(minha_outra_string.strip())

print(minha_outra_string.replace(" ", "Player-"))

print(len(minha_outra_string))
print(minha_string[10])
print(minha_string[3:8])
print(minha_string.index("TeXto"))


print("####################")

x = "k" in minha_string
print(x)

marcas_de_carros = "\nmecedez, \nvolvo, \naudi."
print(marcas_de_carros)