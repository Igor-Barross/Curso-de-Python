# - COLETA DE DADOS
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# - TROCA DE TIPO DOS DADOS PARA INTEIRO
primeiro_int = int(primeiro_valor)
segundo_int = int(segundo_valor)

# - VERIFICAÇÃO DE MAIOR OU MAIOR VALOR
if primeiro_int > segundo_int:
    print(f"primeiro_valor='{primeiro_int}' é maior que o segundo_valor='{segundo_int}'")
    
elif segundo_int > primeiro_int:
    print(f"segundo_valor='{segundo_int}' é maior que o primeiro_valor='{primeiro_int}'")
    
else:
    print('Ambos são iguais')
    