from src.calculadora_classes.evento import Evento
from src.calculadora_classes.pessoa import Pessoa
from src.calculadora_classes.despesa import Despesa
from src.calculadora_classes.produto import Produto

churrasco = Evento('Churrasco')
viagem = Evento('Viagem')
lezao = Pessoa('Lezão')
caio = Pessoa('Caio')
carne = Produto('Carne')
carvao = Produto('Carvão')

churrasco.add_pessoa(caio)
churrasco.add_pessoa(lezao)

caio.add_despesa(Despesa(carne, {caio: 100, lezao: 0}), churrasco)
caio.add_despesa(Despesa(carne, {caio: 0, lezao: 80}), churrasco)
caio.add_despesa(Despesa(carne, {caio: 50}), churrasco)

churrasco.fechar_conta()