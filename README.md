# Calculadora de Eventos

## Descrição

Para me ajudar nos estudos de Orientação a Objetos, desenvolvi essa aplicação em Python para calcular as despesas entre as pessoas de um evento, como um churrasco por exemplo. 

Ao criar uma despesa, é possível vincular uma ou mais pessoas a ela e dizer quanto cada um pagou. No final, ao fechar a conta do evento, ele calcula quanto cada um ainda precisa pagar ou receber. 

## Requisitos

O código foi escrito apenas com Python 3.10.6

## Funcionamento

O projeto possui quatro classes: Evento, Pessoas, Despesas e Produtos.

O Evento manterá relacionado as Pessoas participantes e suas Despesas.

Para criá-lo, basta passar o nome do evento:

'''churrasco = Evento("Churrasco")'''

As Despesas são compostas por um Produto e por Pessoas, bem como o valor que cada pessoa