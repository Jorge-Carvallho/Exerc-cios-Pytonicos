"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""
# resposta 1
# def remove_adjacent(nums):
#     resultado = []
#     for i in range(len(nums)):                           # gera uma sequência de números de 0 até len(nums) que são indice validos para a lista
#         if i == 0 or nums[i] != nums[i-1]:                #verifica se o elemento do indice é maior que zero e menor que o último assim iderando sobre todos os itns 
#             resultado. append(nums[i])                     # adiciona a lista resultado caso a condição seja verdadeira com indice ==0 ou se não iguais entre as 2 tuplas ou listas
    
#     return resultado


# resposta 2
def remove_adjacent(nums):
    if not nums:
        return []# verifica se a lista está vazia se tiver retorna True que neste caso a retorna a lista vazia assim[]
    
    resultado = []
    
    for current,next_one in zip(nums, nums[1:]):
        if current != next_one:
                resultado.append(current)# faz a comparação e adiciona a valor da lista a current
    if nums:
        resultado.append(nums[-1])
        return resultado








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
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])