from ordered_set import OrderedSet


class Evento:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._pessoas = set()
        self._despesas = OrderedSet()

    @property
    def total_despesas(self):
        total = 0
        for despesa in self._despesas:
            total += despesa.valor
        return total

    def add_pessoa(self, pessoa):
        self._pessoas.add(pessoa)
        pessoa.eventos.add(self)

    def check_pessoas_cadastradas_no_evento(self, pessoas):
        if not pessoas:
            print("Lista de divisão vazia. Despesa não cadastrada!")
            return False
        pessoas_nao_cadastradas = []
        for pessoa in pessoas:
            if not pessoa in self._pessoas:
                pessoas_nao_cadastradas.append(pessoa.nome)

        if not pessoas_nao_cadastradas:
            return True
        print(
            f"As seguintes pessoas não estão no Evento {self.nome}: {pessoas_nao_cadastradas}"
        )
        return False

    def extrato_por_pessoa(self, pessoa):
        if self.check_pessoas_cadastradas_no_evento([pessoa]):
            titulo = f" Extrato {pessoa} - {self.nome} ".center(40, "*")
            itens = ""

            total = 0
            total_pago = 0
            for despesa in self._despesas:
                if pessoa in despesa.divisao:
                    total_pago += despesa.divisao[pessoa]
                    total += despesa.valor_individual
                    itens += (
                        f"\n{despesa.produto.nome:20}{despesa.valor_individual:>20.2f}"
                    )

            itens += (
                f"\n{'*'*40}\n{'TOTAL ' + self.nome.upper() + ':':20}{total:>20.2f}"
            )

            print(f"\n{titulo}{itens}")
            return total, total_pago

    def extrato_por_produto(self, produto):
        total_por_produto = 0
        for despesa in self._despesas:
            if produto == despesa.produto:
                total_por_produto += despesa.valor

        titulo = f" Extrato {produto} - {self.nome} ".center(40, "*")
        item = f"\n{'TOTAL:':20}{total_por_produto:>20.2f}"

        print(f"\n{titulo}{item}")
        return total_por_produto

    def extrato_total(self):
        titulo = f" EXTRATO FINAL - {self.nome} ".upper().center(40, "*")
        itens = ""
        total = 0
        for despesa in self._despesas:
            total += despesa.valor
            itens += f"\n{despesa.produto.nome:20}{despesa.valor:>20.2f}"

        itens += f"\n{'*'*40}\n{'TOTAL:':20}{total:>20.2f}"

        print(f"\n{titulo}{itens}")
        return total

    def fechar_conta(self):
        if self._pessoas:
            titulo = f" Fechamento de conta - {self.nome} ".upper().center(60, "*")
            titulo += f"\n{'NOME':20}{'PAGO':^20}{'A PAGAR':>20}"
            itens = ""
            pessoas_inativas = []
            for pessoa in self._pessoas:
                total_individual, total_individual_pago = self.extrato_por_pessoa(pessoa)
                if total_individual == 0:
                    pessoas_inativas.append(pessoa)
                itens += f"\n{pessoa.nome:20}{total_individual_pago:>12.2f}{total_individual-total_individual_pago:>28.2f}"

            for pessoa_inativa in pessoas_inativas:
                self._pessoas.remove(pessoa)

            itens += f"\n{'*'*60}\n{'TOTAL:':20}{self.total_despesas:>12.2f}"
            itens += (
                f"\n{'MÉDIA INDIVIDUAL:':20}{self.total_despesas/len(self._pessoas):>12.2f}"
            )
            print(f"\n{titulo}{itens}")
            return True
        print("O evento não possui pessoas nem despesas")

    def __repr__(self) -> str:
        return self.nome

    def __str__(self) -> str:
        return f"Evento: {self.nome} - Participantes: {self._pessoas} - Valor Total: {self.total_despesas:.2f}"


class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.eventos = set()

    def add_despesa(self, despesa, evento):
        if evento.check_pessoas_cadastradas_no_evento(despesa.divisao.keys()):
            evento._despesas.add(despesa)
            return True
        return False

    def extrato_por_evento(self, evento):
        evento.extrato_por_pessoa(self)
        return True

    def extrato_total(self):
        total_geral = 0
        for evento in self.eventos:
            total_geral += evento.extrato_por_pessoa(self)[0]
        print(f"{'-'*40}\n{'TOTAL GERAL: ':20}{total_geral:>20.2f}")

    # def eventos(self):
    #     eventos = []
    #     for evento in self.eventos:
    #         eventos.append(evento.nome)
    #     return eventos

    def __repr__(self) -> str:
        return self.nome


class Despesa:
    def __init__(self, produto, divisao) -> None:
        self.produto = produto
        self.divisao = divisao

    @property
    def valor(self):
        return sum(self.divisao.values())

    @property
    def valor_individual(self):
        return sum(self.divisao.values()) / len(self.divisao)

    def __repr__(self) -> str:
        return f"{self.produto}: {self.valor}"


class Produto:
    def __init__(self, nome) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return self.nome


churrasco = Evento("Churrasco")
# viagem = Evento("Viagem")

# carne = Produto("Carne")
# carvao = Produto("Carvão")

# caio = Pessoa("Caio")
# rafa = Pessoa("Rafael")
# lezao = Pessoa("Lezão")


# churrasco.add_pessoa(caio)
# churrasco.add_pessoa(lezao)
# churrasco.add_pessoa(rafa)

# viagem.add_pessoa(caio)
# viagem.add_pessoa(lezao)

# caio.add_despesa(Despesa(carne, {caio: 30}), viagem)
# caio.add_despesa(Despesa(carvao, {caio: 15, lezao: 10}), viagem)

# caio.add_despesa(Despesa(carne, {caio: 30, lezao: 0}), churrasco)
# caio.add_despesa(Despesa(carne, {caio: 100}), churrasco)
# caio.add_despesa(Despesa(carvao, {caio: 0, lezao: 10, rafa: 0}), churrasco)

# viagem.fechar_conta()
churrasco.fechar_conta()
