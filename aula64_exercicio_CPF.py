import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \
#     .replace('-', '') \                   < metodo não casual, apenas para substuições simples
#     .replace(' ', '')

entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(
    r'[^0-9]',       # argumento da função para ignorar qualquer coisa que seja um numero
    '',
    entrada
)

# validação de entrada para saber se os digitos estão repetidos
entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


# lista para conter os numeros do CPF sem '.' e '-' 
nove_digitos = cpf_enviado_usuario[:9]

# laço para revomer os '.' e '-' e colocar os numeros na variavel nove_digitos
# for i in cpf_enviado_usuario:
#     if i != '.' and i != '-':
#         digitos_cpf.append(i)

contador_regressivo_1 = 10

resultado_digito_1 = 0
# logica para se obter resultado da multiplicação e soma do primeiro digito
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
    if contador_regressivo_1 < 2:
        break

# conta para obter o resultado do primeiro digito
digito_1 = (resultado_digito_1 * 10) % 11

# opereção ternaria para validar o primeiro digito do CPF
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
# logica para se obter resultado da multiplicação e soma do segundo digito
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
    if contador_regressivo_2 < 2:
        break

# conta para obter o resultado do segundo digito
digito_2 = (resultado_digito_2 * 10) % 11

# operação ternaria para validar o segundo digito do CPF    
digito_2 = digito_2 if resultado_digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuario:
    print(f'o CPF:  {cpf_enviado_usuario} é valido!')
else:
    print(f'o CPF:  {cpf_enviado_usuario} não é valido!')





