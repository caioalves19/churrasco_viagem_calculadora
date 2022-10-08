from src.calculadora_classes.evento import Evento
from src.calculadora_classes.pessoa import Pessoa
from src.calculadora_classes.despesa import Despesa
from src.calculadora_classes.produto import Produto

churrasco = Evento("Churrasco")
viagem = Evento("Viagem")

carne = Produto("Carne")
carvao = Produto("Carvão")

caio = Pessoa("Caio")
rafa = Pessoa("Rafael")
lezao = Pessoa("Lezão")


churrasco.add_pessoa(caio)
churrasco.add_pessoa(lezao)
churrasco.add_pessoa(rafa)

viagem.add_pessoa(caio)
viagem.add_pessoa(lezao)

caio.add_despesa(Despesa(carne, {caio: 30}), viagem)
caio.add_despesa(Despesa(carvao, {caio: 15, lezao: 10}), viagem)

caio.add_despesa(Despesa(carne, {caio: 30, lezao: 0}), churrasco)
caio.add_despesa(Despesa(carne, {caio: 100}), churrasco)
caio.add_despesa(Despesa(carvao, {caio: 0, lezao: 10, rafa: 0}), churrasco)

viagem.fechar_conta()
churrasco.fechar_conta()