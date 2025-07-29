class Cachorro:

    def __init__(self, raca, idade):
        self.raca = raca
        self.idade = idade
    
    def latir(self):
        print("AU AU")

    def correr_atras_moto(self):
        while True:
            cachorro = input("Cachorro é caramelo? s/n :")
            if cachorro == 's':
                print("corre atrás da moto")
            else:
                print("corre da moto")
                break
cachorro = Cachorro("husky", 8)

cachorro.latir()
cachorro.correr_atras_moto()