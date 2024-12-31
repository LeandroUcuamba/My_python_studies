familia = ["Leandro", "Roberta", "Andre", "Maria", "Santos"]


print(familia[3])
print(familia[-3])
print(familia[2:])
print(familia[2:4])



familia[3] = "Sandra"

familia.extend(["Ketson", "Dumilson"])
print(familia)

familia.append("spock")
print(familia)

familia.insert(2, "Tiago")
print(familia)

familia.pop()
print(familia)

familia.remove("Ketson")
print(familia)

#familia.clear()


print("############################################################################")

print(familia.count("Leandro"))


print("############################################################################")

idade_familia = [34,36,13,11,2]
print(idade_familia)
idade_familia.sort()
print(idade_familia)
idade_familia.reverse()
print(idade_familia)