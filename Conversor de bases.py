def conversor():
    # Dicionário que mapeia a opção escolhida para cada base
    opcoes = {"1": 10, "2": 2, "3": 8, "4": 16, "5": 5}

    # exibe o menu interativo para o usuário
    print("Bases: [1] Decimal [2] Binário [3] Octal [4] Hexadecimal [5] Base 5")
    op = input("Escolha a base (1-5): ")
    val = input("Digite o número: ")

    # bloco try/except para capturar erros caso o usuário digite um valor inválido
    try:
        # converte o valor de entrada (string) para um número Decimal inteiro usando a base escolhida
        dec = int(val, opcoes[op])

        print("\nResultados:")

        # converte o decimal para Binário (base 2), removendo os dois primeiros caracteres ('0b')
        print(f"Binário (2): {bin(dec)[2:]}")

        # algoritmo matemático para converter Decimal para Base 5 (Quinário)
        b5 = ""
        n = dec
        while n > 0:
            b5 = str(n % 5) + b5
            n //= 5
        # imprime o resultado da Base 5 (ou '0' caso o número digitado seja zero)
        print(f"Base 5 (5):  {b5 if b5 else '0'}")

        # converte o decimal para Octal (base 8), removendo o prefixo ('0o')
        print(f"Octal (8):   {oct(dec)[2:]}")

        # exibe o valor original já convertido em Decimal (base 10)
        print(f"Decimal (10):{dec}")

        # converte para Hexadecimal (base 16), remove o prefixo ('0x') e deixa as letras maiúsculas
        print(f"Hex (16):    {hex(dec)[2:].upper()}")

    except ValueError:
        # mensagem exibida caso ocorra algum erro de digitação (ex: letra em base numérica)
        print("Erro: Entrada inválida!")


# chamada da função principal para executar o programa
conversor()
