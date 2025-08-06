class Cliente:
    def __init__(self, id, nome, cargo):
        self.id = id
        self.nome = nome
        self.cargo = cargo

    def to_dict(self):
        return {'id': self.id, 'nome': self.nome, 'cargo': self.cargo}
            
