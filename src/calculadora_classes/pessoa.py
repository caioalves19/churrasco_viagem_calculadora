class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.eventos = set()

    def add_despesa(self, despesa, evento):
        # Cadastra uma Despesa a um Evento
        if evento.check_pessoas_cadastradas_no_evento(despesa.divisao.keys()):
            evento._despesas.add(despesa)
            return True
        return False

    def extrato_por_evento(self, evento):
        # Exibe extrato individual, mas considera que ela pagou todas as suas despesas individualmente
        evento.extrato_por_pessoa(self)
        return True

    def extrato_total(self):
        # Exibe extrato individual de todos os Eventos que participa, mas considera que ela já pagou todas as suas despesas
        total_geral = 0
        for evento in self.eventos:
            total_geral += evento.extrato_por_pessoa(self)[0]
        print(f"{'-'*40}\n{'TOTAL GERAL: ':20}{total_geral:>20.2f}")

    def __repr__(self) -> str:
        return self.nome