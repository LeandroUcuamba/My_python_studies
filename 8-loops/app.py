i = 1

while i < 10:
    print(i)
    i += 1

print("loop terminou.")
print(i)


print("\n\n#######################################\n\n")


atletas = ["Leandro", "Santos", "Ucuamba"]

for item in atletas:
    print(item)

print("\n\n#######################################\n\n")

for index in range(len(atletas)):
    print(atletas[index], index)