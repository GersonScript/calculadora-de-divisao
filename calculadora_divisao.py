# Solicita ao usuário que informe o valor do dividendo
entrada1 = input("Informe o valor do dividendo: ")
# Solicita ao usuário que informe o valor do divisor
entrada2 = input("Informe o valor de divisor: ")

# Listas para armazenar o resultado geral e os restos
resultado_geral = []
resultado_restos = []

# Função para converter a entrada em número (inteiro ou decimal)


def converter_numero(entrada):
    try:
        # Tenta converter a entrada para float
        numero = float(entrada)
        # Se a entrada não contém um ponto decimal, retorna como inteiro
        if '.' not in entrada:
            return int(numero)
        return numero  # Retorna como float se tiver parte decimal
    except ValueError:
        return "Valor inválido"  # Retorna mensagem de erro se a conversão falhar

# Função para igualar as casas decimais do dividendo e do divisor


def igualar_casas_decimais(entrada1, entrada2):
    str1 = str(entrada1)  # Converte o dividendo para string
    str2 = str(entrada2)  # Converte o divisor para string

    # Conta as casas decimais do dividendo
    casas_decimais_1 = len(str1.split('.')[1]) if '.' in str1 else 0
    # Conta as casas decimais do divisor
    casas_decimais_2 = len(str2.split('.')[1]) if '.' in str2 else 0

    # Determina o maior número de casas decimais
    max_casas_decimais = max(casas_decimais_1, casas_decimais_2)

    # Cria um fator de multiplicação para igualar as casas decimais
    fator = 10 ** max_casas_decimais
    # Multiplica o dividendo e divisor pelo fator para igualar as casas
    # decimais
    entrada1 = int(entrada1 * fator)
    entrada2 = int(entrada2 * fator)

    return entrada1, entrada2  # Retorna os valores ajustados

# Função para o primeiro passo da divisão


def primeiroPasso(lista_dividendo, divisor):
    concatenado = ""  # Inicializa a string para concatenar dígitos
    # Concatena dígitos do dividendo até que seja maior ou igual ao divisor
    for digito in lista_dividendo:
        concatenado += digito
        if int(concatenado) >= divisor:
            break  # Para quando o número concatenado é suficiente
    return int(concatenado)  # Retorna o número concatenado como inteiro

# Função para contar as casas decimais antes do ponto


def contar_casas_decimais_antes(entrada):
    str_numero = str(entrada)  # Converte o número para string
    # Retorna o número de dígitos antes do ponto decimal
    if '.' in str_numero:
        return len(str_numero.split('.')[0])
    else:
        return len(str_numero)

# Função para contar as casas decimais após o ponto


def contar_casas_decimais_depois(valor):
    valor_str = str(valor)  # Converte o valor para string
    partes = valor_str.split('.')  # Separa a parte inteira da decimal
    # Conta as casas decimais e retorna
    if len(partes) > 1:
        casas_decimais = len(partes[1])
    else:
        casas_decimais = 0

    return casas_decimais


# Converte as entradas para números
entrada1 = converter_numero(entrada1)
entrada2 = converter_numero(entrada2)
# Conta as casas decimais do resultado da divisão
contagem_casas_decimais = contar_casas_decimais_depois(entrada1 / entrada2)

# Função principal que executa a lógica da divisão


def main():
    if isinstance(entrada1, float) or isinstance(entrada2, float):
        # Se qualquer entrada for decimal, iguala as casas decimais
        dividendo, divisor = igualar_casas_decimais(entrada1, entrada2)
        number = primeiroPasso(
            list(
                str(dividendo)),
            divisor)  # Obtém o primeiro número
        # Converte o dividendo em lista de dígitos
        lista_dividendo = list(str(dividendo))

        # Realiza a divisão
        quociente = number // divisor
        resto = number % divisor
        # Posição para cortar a lista de dígitos
        posicao_corte = len(str(number))
        # Obtém o restante do dividendo
        nova_lista_dividendo = lista_dividendo[posicao_corte:]
        resultado_geral.append(quociente)  # Adiciona o quociente ao resultado

        # Loop para calcular o quociente e o resto de cada dígito
        for digito in nova_lista_dividendo:
            sub_resto = str(resto) + digito  # Cria um novo resto
            number = int(sub_resto)  # Converte para inteiro
            quociente = number // divisor  # Calcula o quociente
            resto = number % divisor  # Calcula o resto
            # Adiciona o quociente ao resultado
            resultado_geral.append(quociente)

        # Se há mais de 4 casas decimais, faz um cálculo especial
        if contagem_casas_decimais > 4:
            if resto < divisor:
                novo_sub_resto = int(
                    str(resto) + "0")  # Adiciona zero ao resto
                # Adiciona ao resultado de restos
                resultado_restos.append(novo_sub_resto)
                # Adiciona vírgula para separar a parte decimal
                resultado_geral.append(",")
                for i in range(4):
                    novo_quociente = novo_sub_resto // divisor
                    novo_resto = novo_sub_resto % divisor
                    # Adiciona zero para a próxima iteração
                    novo_sub_resto = int(str(novo_resto) + "0")

                    # Adiciona ao resultado de restos
                    resultado_restos.append(novo_sub_resto)
                    # Adiciona ao resultado geral
                    resultado_geral.append(novo_quociente)
                resultado_restos.append(novo_resto)  # Adiciona o último resto

        else:
            # Se há 4 ou menos casas decimais
            if resto < divisor:
                novo_sub_resto = int(str(resto) + "0")
                resultado_restos.append(novo_sub_resto)
                resultado_geral.append(",")
                for i in range(contagem_casas_decimais):
                    novo_quociente = novo_sub_resto // divisor
                    novo_resto = novo_sub_resto % divisor
                    novo_sub_resto = int(str(novo_resto) + "0")

                    resultado_restos.append(novo_sub_resto)
                    resultado_geral.append(novo_quociente)
                resultado_restos.append(novo_resto)

        # Exibe o resultado da divisão
        print(f"\n{entrada1} / {entrada2}")
        print(f"{dividendo} / {divisor}")
        print(
            f"{resultado_restos[0]}     {''.join(map(str, resultado_geral))}")

        # Exibe os restos a partir do segundo elemento
        for item in resultado_restos[1:]:
            if isinstance(item, int):
                print(f"{item}")
            else:
                print(item)
    else:
        # Se as entradas são inteiras
        dividendo = entrada1
        divisor = entrada2
        number = primeiroPasso(list(str(dividendo)), divisor)
        lista_dividendo = list(str(dividendo))

        quociente = number // divisor
        resto = number % divisor
        posicao_corte = len(str(number))
        nova_lista_dividendo = lista_dividendo[posicao_corte:]
        resultado_geral.append(quociente)

        # Loop para calcular quocientes e restos para o caso de inteiro
        for digito in nova_lista_dividendo:
            sub_resto = str(resto) + digito
            number = int(sub_resto)
            quociente = number // divisor
            resto = number % divisor
            resultado_geral.append(quociente)
            resultado_restos.append(sub_resto)

        if contagem_casas_decimais > 4:
            if resto < divisor:
                novo_sub_resto = int(str(resto) + "0")
                resultado_restos.append(novo_sub_resto)
                resultado_geral.append(",")
                for i in range(4):
                    novo_quociente = novo_sub_resto // divisor
                    novo_resto = novo_sub_resto % divisor
                    novo_sub_resto = int(str(novo_resto) + "0")

                    resultado_restos.append(novo_sub_resto)
                    resultado_geral.append(novo_quociente)
                resultado_restos.append(novo_resto)
        else:
            novo_sub_resto = int(str(resto) + "0")
            resultado_restos.append(novo_sub_resto)
            resultado_geral.append(",")
            for i in range(contagem_casas_decimais):
                novo_quociente = novo_sub_resto // divisor
                novo_resto = novo_sub_resto % divisor
                novo_sub_resto = int(str(novo_resto) + "0")

                resultado_restos.append(novo_sub_resto)
                resultado_geral.append(novo_quociente)
            resultado_restos.append(novo_resto)

        # Exibe o resultado da divisão
        print(f"\n{entrada1} / {entrada2}")
        print(f"{dividendo} / {divisor}")
        print(
            f"{resultado_restos[0]}     {''.join(map(str, resultado_geral))}")

        # Exibe os restos a partir do segundo elemento
        for item in resultado_restos[1:]:
            if isinstance(item, int):
                print(f"{item}")
            else:
                print(item)


# Executa a função principal
main()
