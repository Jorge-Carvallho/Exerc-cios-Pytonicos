"""
05. verbing = vernalização

Dada uma string, se seu tamanho for pelo menos 3,
adicione 'ing' no seu fim, a menos que a string
já termine com 'ing', nesse caso adicione 'ly'.

Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.

"""

def verbing(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + ('ly')
    else:
        return s + ('ing')
    
    #  foi usado metódo endswith para o surfixo(verificação dos caracteres finais da string) 
    #  o método startwith poderia fazer a verificação com caracteres iniciais em uma string ou frase
# se a string s for menor que 3 , retornarar apenas a string,
#caso a string já tenha ing ao final da palavra , será adicionando o ly 
#caso a palavra não tenha ing ao final e seja maior que 3 caracteres será adiconado o ing












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
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
    test(verbing, 'testandoing','testandoingly')
    test(verbing, 'testado','testadoing')
