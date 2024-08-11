"""
10. sort_last

Dada uma lista de tuplas não vazias, retorne uma lista ordenada em ordem
crescente com base no último elemento de cada tupla.

Exemplo: [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
Irá retornar: [(2, 2), (1, 3), (3, 4, 5), (1, 7)]

Dica: Use uma custom key= function para extrair o ultimo elemento de cada tupla.
"""

# # resposta 1
# def ultimo_elemento(tupla):
#     return tupla[-1]
# def sort_last(tuples):
#     return sorted(tuples,key=ultimo_elemento)
# sorted() uma função embutida que recebe uma lista e retorna uma nova lista com os elementos ordenados
# sorted( responsavel por ordenação e irar retorna uma lista ordenada, com parametro aparti de -1 ou seja, do ultimo para o primeiro )
  


#resposta 2
# def sort_last(tuples):
    
#     return sorted(tuples,key=lambda x: x[-1])
# sorted() uma função embutida que recebe uma lista e retorna uma nova lista com os elementos ordenados
#  A função sorted( permite que você use argumentos opcoinais chamado key: key é uma rgumento apontando para a função lambda que neste caso esta informando que o sorted seguira ordenação aaprti do -1 ou mesmo que o último
# Função lambda é uma função anônima que neste caso parametro x com valor x para referenciar x de lista e valor x aparti de -1 ou ( último)


#resrposta 3
from operator import itemgetter

def sort_last(tuples):
    return sorted(tuples,key=itemgetter(-1))
#
# itemgetter é uma função fornecida pelo módulo operator ele é usado pra criar função que pode pegar um ou mais itens de uma sequência (como lista ou tuplas) com base em indices
# itemgetter neste caso é como se fosse key=itegetter(-1) é o mesmo que lambda x: x[-1] ou def x(x) return x[-1]
















# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(sort_last, [(1, 3), (3, 2), (2, 1)],
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last, [(2, 3), (1, 2), (3, 1)],
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last, [(1, 7), (1, 3), (3, 4, 5), (2, 2)],
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])