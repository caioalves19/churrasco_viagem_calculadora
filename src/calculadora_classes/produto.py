class Produto:
    def __init__(self, nome) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return self.nome