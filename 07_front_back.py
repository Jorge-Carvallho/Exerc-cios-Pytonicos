"""
07. front_back

Considere dividir uma string em duas metades.
Caso o comprimento seja par, a metade da frente e de trás tem o mesmo tamanho.
Caso o comprimento seja impar, o caracter extra fica na metade da frente.

Exemplo: 'abcde', a metade da frente é 'abc' e a de trás é 'de'.

Finalmente, dadas duas strings a e b, retorne uma string na forma:
a-frente + b-frente + a-trás + b-trás
"""


def front_back(a, b):
    def dividir_string(s):
        lenght = len(s)                        # comprimento
        half = lenght // 2                     # metade // faz a divisão e retorna o valor inteiro
        if lenght % 2 == 0:                    # se indice for dividido por 2 e o resto da divisão for igual a 0(número par)
            front = s[:half]
            back = s[half:]
        else:
           front = s[:half + 1]             # pega o resultado da metade mais 1 e responde ex: 11 / 2 = 5 -> 5 : 5 +1 frente 
           back = s[half + 1:]              # metade mais 1 primeiro : depois o restante  
        return front, back
    a_front, a_back = dividir_string(a)
    b_front, b_back = dividir_string(b)
    resultado = a_front + b_front + a_back + b_back
    
    return resultado 
    





# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(front_back, ('abcd', 'xy'), 'abxcdy')
    test(front_back, ('abcde', 'xyz'), 'abcxydez')
    test(front_back, ('Kitten', 'Donut'), 'KitDontenut')
