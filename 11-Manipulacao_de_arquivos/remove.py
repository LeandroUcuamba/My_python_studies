import os

if os.path.exists("11-Manipulacao_de_arquivos/removeTest.txt"):
  os.remove("11-Manipulacao_de_arquivos/removeTest.txt")
else:
  print("Arquivo não existe!")
  