# Calculadora de Eventos

## Descrição

Para me ajudar nos estudos de Orientação a Objetos, desenvolvi essa aplicação em Python para calcular as despesas entre as pessoas de um evento, como um churrasco por exemplo. 

Ao criar uma despesa, é possível vincular uma ou mais pessoas a ela e dizer quanto cada um pagou. No final, ao fechar a conta do evento, ele calcula quanto cada um ainda precisa pagar ou receber. 

## Requisitos

O código foi escrito apenas com Python 3.10.6

## Funcionamento

O projeto possui quatro classes: Evento, Pessoas, Despesas e Produtos.


Para criar uma Pessoa, basta passar o nome:

```caio = Pessoa("Caio")```

A Pessoa pode adicionar uma Despesa a um determinado evento. Também possui extratos total e por evento que participou.

```caio.adicionar_despesa(Despesa(), Evento)```

As Despesas são compostas por um Produto e por Pessoas, bem como o valor que cada pessoa pagou. O Produto precisa apenas de um nome para ser criado. Apenas um Pessoa pode adicionar uma Despesa:

```carne = Produto("Carne"))```
```caio.adicionar_despesa(Despesa(carne, {caio: 10, rafael: 20}), churrasco)```

É possível acessar o valor total da Despesa (no exemplo acima, seria 30) e também o valor individual (no exemplo, seria 15, pois apenas caio e rafael estão vinculados à despesa). Se houver mais pessoas no Evento, o valor dessa Despesa em específico não entrará na conta delas. 

O Evento manterá relacionado as Pessoas participantes e suas Despesas.

Para criá-lo, basta passar o nome do evento:

```churrasco = Evento("Churrasco")```

O Evento possui algumas funcionalidades, como adicionar Pessoa e alguns tipos de extratos: total, por pessoa e por produto. Esses são calculados sem considerar se alguém deve algum valor.

A única função que calcula o valor a pagar e a receber de cada integrante é o seguinte:

```churrasco.fechar_conta()```

Exemplo da saída do fechar_conta():

~~~
************* FECHAMENTO DE CONTA - CHURRASCO **************
NOME                        PAGO                     A PAGAR
Caio                      130.00                      -11.67
Lezão                      10.00                        8.33
Rafael                      0.00                        3.33
************************************************************
TOTAL:                    140.00
~~~
As Despesas deste exemplo foram as seguintes:
1. ```caio.add_despesa(Despesa(carne, {caio: 30, lezao: 0}), churrasco)```
2. ```caio.add_despesa(Despesa(carne, {caio: 100}), churrasco)```
3. ```caio.add_despesa(Despesa(carvao, {caio: 0, lezao: 10, rafa: 0}), churrasco)```

Caio, por exemplo, está vinculado às três Despesas. Na 1, o total (30) foi dividido por 2 (15). Na segunda, a despesa foi apenas dele, então soma-se 100 (115). Na terceira, foi dividida entre três, então soma-se 3,33 (118,33). Entretanto, ele desembolsou 130, por isso o fechar_conta() exibiu -11,67 (Caio precisa receber esse valor), que virá de Lezão e Rafael.

[⬆ Voltar ao topo](#churrasco_viagem_calculadora#calculadora-de-eventos)<br>