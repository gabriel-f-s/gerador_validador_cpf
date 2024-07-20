import random

# Função para realizar o cálculo que faz  e também confere um CPF válido:


def _realiza_calculo_cpf(nove_digitos_cpf: str):
    contagem_regressiva_dez = 10
    lista_numeros_cpf_multiplicados = []

    for numero in nove_digitos_cpf:
        calculo = int(numero) * contagem_regressiva_dez
        contagem_regressiva_dez -= 1
        lista_numeros_cpf_multiplicados.append(calculo)

    soma_resultado = sum(lista_numeros_cpf_multiplicados)
    resultado_primeiro_digito = (soma_resultado * 10) % 11

    dez_digitos_cpf = nove_digitos_cpf + str(resultado_primeiro_digito)

    contagem_regressiva_onze = 11
    lista_numeros_cpf_multiplicados.clear()

    for numero in dez_digitos_cpf:
        calculo = int(numero) * contagem_regressiva_onze
        contagem_regressiva_onze -= 1
        lista_numeros_cpf_multiplicados.append(calculo)

    soma_resultado = sum(lista_numeros_cpf_multiplicados)
    resultado_segundo_digito = (soma_resultado * 10) % 11

    return resultado_primeiro_digito, resultado_segundo_digito

# Função que gera um CPF válido:


def gerador_cpf(sigla_estado) -> str:
    sigla_estado.upper()
    nono_digito = int()

    # O bloco de código if abaixo seleciona o nono dígito do CPF de acordo com o estado:
    if (sigla_estado == 'DF') or (sigla_estado == 'GO') or (sigla_estado == 'MS') \
            or (sigla_estado == 'TO'):
        nono_digito = 1
    elif (sigla_estado == 'PA') or (sigla_estado == 'AM') or (sigla_estado == 'AC') \
            or (sigla_estado == 'AP') or (sigla_estado == 'RO') or (sigla_estado == 'RR'):
        nono_digito = 2
    elif (sigla_estado == 'CE') or (sigla_estado == 'MA') or (sigla_estado == 'PI'):
        nono_digito = 3
    elif (sigla_estado == 'PE') or (sigla_estado == 'RN') or (sigla_estado == 'PB') \
            or (sigla_estado == 'AL'):
        nono_digito = 4
    elif (sigla_estado == 'BA') or (sigla_estado == 'SE'):
        nono_digito = 5
    elif (sigla_estado == 'MG'):
        nono_digito = 6
    elif (sigla_estado == 'RJ') or (sigla_estado == 'ES'):
        nono_digito = 7
    elif (sigla_estado == 'SP'):
        nono_digito = 8
    elif (sigla_estado == 'PN') or (sigla_estado == 'SC'):
        nono_digito = 9
    elif (sigla_estado == 'RS'):
        nono_digito = 0
    else:
        print('Digite apenas a sigla, ex: MG')

    lista_numeros_cpf = []

    # No for abaixo, irá selecionar 8 números aleatórios para completar o CPF e o
    # nono digíto do estado.

    for numero in range(1, 10):
        if numero == 9:
            lista_numeros_cpf.append(nono_digito)
            break
        lista_numeros_cpf.append(int(random.random() * 10))

    numeros_cpf = ''

    # No for abaixo, é convertida a lista em string

    for numero in lista_numeros_cpf:
        numeros_cpf += str(numero)

    resultado_primeiro_digito, resultado_segundo_digito = _realiza_calculo_cpf(
        nove_digitos_cpf=numeros_cpf)

    cpf_completo = numeros_cpf + \
        str(resultado_primeiro_digito) + str(resultado_segundo_digito)
    return cpf_completo

# Função para validar um CPF:


def validar_cpf(cpf: str) -> None:
    cpf_formatado = ''

    for numero in cpf:
        if (numero == '.') or (numero == '-'):
            continue
        cpf_formatado += numero
    nove_digitos_cpf = cpf_formatado[:9]
    ultimos_digitos_cpf = cpf_formatado[9:]

    resultado_primeiro_digito, resultado_segundo_digito = _realiza_calculo_cpf(
        nove_digitos_cpf=nove_digitos_cpf,)

    if str(resultado_primeiro_digito) == ultimos_digitos_cpf[0] and \
            str(resultado_segundo_digito) == ultimos_digitos_cpf[1]:
        print('CPF Válido.')
    else:
        print('CPF Inválido.')

# Função para formatar o CPF:


def formatar_cpf(cpf: str) -> str:
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado
