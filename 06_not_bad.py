"""
06. not_bad

Dada uma string, encontre a primeira aparição das
substrings 'not' e 'bad'. Se 'bad' aparecer depois
de 'not', troque todo o trecho entre 'not' e 'bad'
por 'good' e retorne a string resultante.

Exemplo: 'The dinner is not that bad!' retorna 'The dinner is good!'
"""
# resposta 1
# import re

# def not_bad(s):
#     padrao = r'not.*?bad'
#     nova_string = re.sub(padrao,'good',s, count=1)
#     return nova_string

# usando expressões padrão é passsado no import re e verificado chamando a string r de comparação
# é feita a verificação e substituição caso padrão:substituido opr ; good / s string ou frase passada
# e count é o número máximo de vezes que subistituirar padrão por 'good' neste caso acontecerar  apenas uma vez
print('--------------------------------\n')



#resposta 2
def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')

    if not_index != -1 and bad_index != -1:
        if bad_index > not_index:
            return s[:not_index] + 'good' + s[bad_index+3:]

    return s
        
# O método find, s no caso seria a frase completa, atribuo o método para a verificação na frase e dentro no método -->
# ele compara se existe a palavra 'not' e retorna o indice caso exista, caso não exista ele retorna -1 como parametro
# Na frase 'This dinner is not that bad!' a palavra not se inicia no indice 12, a primeira verificação existe com ---------> if not_index != -1 and bad_index != -1: e  também se bad existe na frase com segunda verificação ---> and bad_index != -1: ou seja se eles são diferentes de -1 eles existem(são verdadeiros)
# posterior verifico se o index de not é maior que o indice de bad, caso o indice de bad seja menor que o de not ou seja ->
#  if bad_index > not_index: se o indice de bad for maior que indice de  not, ele aparece na mensagem primeiro que bad então  não faz nenhuma mudança




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
    test(not_bad, 'This movie is not so bad', 'This movie is good')
    test(not_bad, 'This dinner is not that bad!', 'This dinner is good!')
    test(not_bad, 'This tea is not hot', 'This tea is not hot')
    test(not_bad, "It's bad yet not", "It's bad yet not")
    test(not_bad, 'This dinner is bad that not', 'This dinner is bad that not')
