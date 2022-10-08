class Despesa:
    def __init__(self, produto, divisao) -> None:
        self.produto = produto
        self.divisao = divisao

    @property
    #Valor total da despesa
    def valor(self):
        return sum(self.divisao.values())

    @property
    # Valor total dividido pelo número de Pessoas vinculadas
    def valor_individual(self):
        return self.valor / len(self.divisao)

    def __repr__(self) -> str:
        return f"{self.produto}: {self.valor}"