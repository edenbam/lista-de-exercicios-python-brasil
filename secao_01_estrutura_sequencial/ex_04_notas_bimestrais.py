"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> from secao_01_estrutura_sequencial import ex_04_notas_bimestrais
    >>> numeros =['7', '8','9','10']
    >>> ex_04_notas_bimestrais.input = lambda k: numeros.pop()
    >>> ex_04_notas_bimestrais.calcular_media()
    A média anual é 8.5

"""


def calcular_media():
    """Escreva aqui em baixo a sua solução"""
    nota_1 = int(input('Digite a 1 nota: '))
    nota_2 = int(input('Digite a 2 nota: '))
    nota_3 = int(input('Digite a 3 nota: '))
    nota_4 = int(input('Digite a 4 nota: '))
    media = (nota_1 + nota_2 + nota_3 + nota_4)/4
    print(f'A média anual é {media}')
