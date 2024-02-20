class Carro:
    
    def __init__(self, marca, modelo, cor, combustivel) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        
        self.ligado = False
        self.velocidade = 0
        
    def ligar(self):
        if self.ligado == False:
            print(f"Ligando {self.modelo}...")
            self.ligado = True
        else:
            print("O carro ja esta ligado, nada acontece.")
        
    def desligar(self):
        if self.ligado:
            print(f"Desligando {self.modelo}...")
            self.ligado = False
        else:
            print("Carro já esta desligado, nada acontece.")

    def acelerar(self):
        if self.ligado:
            self.velocidade += 10
            print(f"{self.velocidade}km/h")
        else:
            print("Não é possivel acelerar corro desligado")
            
    def desacelerar(self):
        if self.ligado:
            if self.velocidade > 0:
                self.velocidade -= 10
                print(f"{self.velocidade}km/h")
            else:
                print("O carro já esta parado")
        else:
            print("Não é possivel desacelerar corro desligado")