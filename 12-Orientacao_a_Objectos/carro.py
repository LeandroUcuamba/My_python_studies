class Carro:
    def __init__(self, marca, modelo, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False

    def ligar(self):
        if self.ligado:
            print("Carro já está ligado!")
        else:
            self.ligado = True
            print("Carro ligado!")

    def desligar(self):
        print("Carro desligado!")