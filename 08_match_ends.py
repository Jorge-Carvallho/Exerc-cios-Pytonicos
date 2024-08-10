"""
08. match_ends =     matemática final

Dada uma lista de strings, retorne a contagem do número de
strings onde o comprimento da cadeia é 2 ou mais e o primeiro
e o último caracteres da cadeia são os mesmos.

PS: Python não possui o operador ++, porém += funciona.
"""

#resposta 1
# def match_ends(words):
#     count = 0
#     for word in words:
#         if len(word)>= 2 and word[0] == word[-1]:
#             count  += 1
#     return count

print('-------------------------------------------------------\n')

# resposta 2
def match_ends(words):
    return sum(1 for word in words if len(word) >= 2 and word[0] == word[-1])

# sum(1 <-- como se fosse a variavel count que faz a contagem casso atenda os parametros)
# para cada palavra in palavras onde se palavra form maior ou igual a 2 e se palavra no indice 0 for igual a palavra no ultimo indicem o sum retorna a quantidade contada, ou sejam sum 1 é como se fosse count += 1














# def match_ends(words):
#     count = 0
#     for word in words:
#         if len(word)>= 2 and word[0] == word[-1]:
#             count += 1
        
#     return count
        
    
    














# def match_ends( words):
#     count = 0
#     for word in words:
#         if len(word) >= 2 and word[0] == word[-1:]:
#             count += 1
        

#     return count
    
    
    
  
















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
    test(match_ends, ['aba', 'xyz', 'aa', 'x', 'bbb'], 3)
    test(match_ends, ['', 'x', 'xy', 'xyx', 'xx'], 2)
    test(match_ends, ['aaa', 'be', 'abc', 'hello'], 1)
