"Programa em Python que controla uma pizzaria, é a versão mais procedimental"
"de um projeto que estou criando com paradigma funcional."
"Como limitações, não há ação caso o número de mesas vá a zero, se for selecionado"
"um código de produto fora da lista, o programa lançará uma exceção típica do Python"
"-list index out of range-, e a geração de produtos comprados por meio de vetor e lista"
"não chegou a ser testado."

"By: Douglas Holanda"

import sys

def main():
    pizzas = ["calabresa ", "portuguesa", "muçarela ", "marguerita", "napolitana", "caipira", "frango\t", "milho\t"]
    codigos = [1, 2, 3, 4, 5, 6, 7, 8]
    precosP = [12.89, 14.56, 16.99, 15.78, 13.45, 15.60, 12.89, 15.00]
    precosM = [17.89, 18.99, 18.47, 21.20, 22.60, 24.60, 17.89, 25.00]
    precosG = [24.50, 26.70, 34.20, 23.50, 25.00, 27.80, 24.50, 26.70]

    sucos = ["maracujá", "laranja", "limão\t", "morango", "goiaba\t", "acerola", "uva\t\t", "abacaxi"]
    refrigerantes = ["guaraná", "laranja", "cajuína", "coca-cola", "uva\t\t", "limão\t"]
    codigo1 = [1, 2, 3, 4, 5, 6, 7, 8]
    codigo2 = [1, 2, 3, 4, 5, 6]
    precoS = [6.00, 5.00, 5.00, 7.80, 6.00, 3.50, 4.00, 4.50]
    precoR = [9.00, 9.00, 10.50, 8.50, 8.00, 8.00]

    print("====================================================================\n")
    print("================Olá, bem-vindo(a) à pizzaria online=================\n")
    print("====================================================================\n")
    print("Temos um catálogo de pizzas e bebidas imperdível para você e tudo por um\n")
    print("preço que cabe no seu bolso, portanto, bom apetite e bom proveito!\n")
    print("==================Digite suas opções===============================\n")
    print("===================================================================\n")


    valor = True
    precop = 0.0
    precom = 0.0
    precog = 0.0
    precos = 0.0
    precor = 0.0
    precoPizza = 0.0
    precoBebida = 0.0
    quantPizzas = 0
    quantBebidas = 0
    quantItens = 0


    while valor:
        opcao = int(input("1-Cadastrar a mesa (após isso, daremos início ao processo de pedidos)\n2-encerrar o programa\n"))

        if opcao == 1:
            print("Você escolheu cadastrar uma mesa, temos 30 disponíveis.\n")

            mesasRest = 30
            somaMesas = 0

            mesa = int(input("Digite a quantidade de mesas que deseja cadastrar(-1 caso não queiras mais cadastrar):"))

            while mesa != -1:

                if mesa <= 30:
                    print(f"{mesa} cadastrada(s) com sucesso!\n")

                    mesasRest -= mesa
                    somaMesas += mesa

                    print(f"Agora resta(m) só {mesasRest}.\n")

                else:
                    print("Não temos essa quantidade de mesas disponíveis.\n")

                mesa = int(
                    input("Digite a quantidade de mesas que deseja cadastrar(-1 caso não queiras mais cadastrar):"))

            print(f"Cadastro de {somaMesas} mesa(s) realizado com sucesso!\n")

            acao = int(input("Pedir as pizzas(1 para iniciar e 2 para finalizar):"))

            while acao != 2:

                escolha = int(input("Escolha qual tamanho deseja:\n1-Pequena\n2-Média\n3-Grande\n"))

                if escolha == 1:
                    print("Sabor\t\t Código \t Preço(R$)\n")
                    for i in range(0, 8):
                        print(pizzas[i], "\t", codigos[i], "\t\t\t", precosP[i], "\t")

                    quant = int(input("Digite a quantidade que desejas:"))

                    i = 0

                    while i < quant:
                        piz = int(input(f"Digite o código da pizza {i + 1}:"))

                        piz -= 1
                        precop += precosP[piz]

                        try:
                            print(f"Pizza sabor {pizzas[piz]} tamanho pequena escolhida com sucesso.")

                        except IndexError:
                            print("Código inexistente!")

                        i += 1


                elif escolha == 2:
                    print("Sabor\t\t Código \t Preço(R$)\n")
                    for i in range(0, 8):
                        print(pizzas[i], "\t", codigos[i], "\t\t\t", precosM[i], "\t")

                    quant = int(input("Digite a quantidade que desejas:"))

                    j = 0

                    while j < quant:
                        piz = int(input(f"Digite o código da pizza {j + 1}:"))

                        piz -= 1
                        precom += precosM[piz]

                        try:
                            print(f"Pizza sabor {pizzas[piz]} tamanho média escolhida com sucesso.")

                        except IndexError:
                            print("Código inexistente!")

                        j += 1


                elif escolha == 3:
                    print("Sabor\t\t Código \t Preço(R$)\n")
                    for i in range(0, 8):
                        print(pizzas[i], "\t", codigos[i], "\t\t\t", precosG[i], "\t")

                    quant = int(input("Digite a quantidade que desejas:"))

                    k = 0

                    while k < quant:
                        piz = int(input(f"Digite o código da pizza {k + 1}:"))

                        piz -= 1
                        precog += precosG[piz]

                        try:
                            print(f"Pizza sabor {pizzas[piz]} tamanho grande escolhida com sucesso.")

                        except IndexError:
                            print("Código inexistente!")

                        k += 1

                precoPizza = precop + precom + precog

                print(f"Preço parcial : R$ {precoPizza:.2f}.\n")

                acao = int(input("Pedir as pizzas(1 para iniciar e 2 para finalizar):"))

                quantPizzas += quant


            action = int(input("Digite 1 para iniciar o pedido de bebidas e 2 para finalizar:"))

            while action != 2:

                escolha1 = int(input("Digite a opção de bebida:\n1-Sucos\n2-Refrigerantes\n"))

                if escolha1 == 1:
                    print("Sabor\t\t Código \t Preço(R$)\n")
                    for i in range(0, 8):
                        print(sucos[i], "\t", codigo1[i], "\t\t\t", precoS[i], "\t")

                    quant = int(input("Digite a quantidade que desejas:"))

                    i = 0

                    while i < quant:
                        suco = int(input(f"Digite o código do suco {i + 1}:"))

                        suco -= 1
                        precos += precoS[suco]

                        try:
                            print(f"Suco sabor {sucos[suco]} escolhido com sucesso.\n")

                        except IndexError:
                            print("Código inexistente!")

                        i += 1

                elif escolha1 == 2:
                    print("Sabor\t\t Código \t Preço(R$)\n")
                    for i in range(0, 6):
                        print(refrigerantes[i], "\t", codigo1[i], "\t\t\t", precoR[i], "\t")

                    quant = int(input("Digite a quantidade que desejas:"))

                    j = 0

                    while j < quant:
                        refri = int(input(f"Digite o código do refrigerante {j + 1}:"))

                        refri -= 1
                        precor += precoR[refri]

                        try:
                            print(f"Refrigerante sabor {refrigerantes[refri]} escolhido com sucesso.\n")

                        except IndexError:
                            print("Código inexistente.")

                        j += 1

                precoBebida = precos + precor

                print(f"Preço parcial : R$ {precoBebida:.2f}.\n")

                action = int(input("Digite 1 para iniciar o pedido de bebidas e 2 para finalizar:"))

                quantBebidas += quant

            print("=====================================================================================================================\n")

            print("Nice! Agora vamos aos cálculos de conta, lembrando que o fato de o grupo de\n"
                  "clientes assistir ao couvert dar direito de 10% de desconto, ademais, a\n"
                  "taxa de serviço da pizzaria cobra R$ 0.25 por pessoa nas mesas.\n")

            quantiPessoas = int(input("Qual a quantidade de pessoas no grupo de clientes?"))

            cobrancaPessoa = 0.0
            cobrancaPessoa = 0.25*quantiPessoas

            opcaoCouvert = input("O cliente ou grupo deseja assistir ao couvert?\ns-sim\nn-não\n")

            valorCouvert = 0.0
            contaFinal = 0.0
            contaDividida = 0.0

            if opcaoCouvert == 's':
                print("Cálculo de desconto de 10% sobre o valor final com sucesso.\n")

                valorCouvert = float(input("Digite, em reais, o valor do couvert: "))

                contaFinal = (precoPizza + precoBebida + cobrancaPessoa + valorCouvert)*0.9

                contaDividida = contaFinal / quantiPessoas

            elif opcaoCouvert == 'n':
                print("Compreendemos a opção.\n")

                valorCouvert += 0.0
                contaFinal = precoPizza + precoBebida + cobrancaPessoa + valorCouvert
                contaDividida = contaFinal/quantiPessoas

            else:
                print("Opção inexistente!\n")

            quantItens = quantPizzas + quantBebidas
            print("Realizando cálculos...\n")

            opcaoDividirConta = int(input("Deseja que o sistema calcule automaticamente a divisão da conta?\n1-Sim\n2-Não\n"))
            print("Ok, gerando comprovante de conta...\n")



            if opcaoDividirConta == 1:

                print("==================================================================\n")
                print(f"    |  Quantidade de mesas reservadas:    {somaMesas}          |\n")
                print(f"    |  Quantidade de itens           :    {quantItens}         |\n")
                print(f"    | {quantPizzas} pizza(s) && {quantBebidas} bebidas.        |\n")
                print(f"    |  Somatório do preço das pizzas : R$ {precoPizza :.2f}    |\n")
                print(f"    |  Somatório do preço das bebidas: R$ {precoBebida :.2f}   |\n")
                print(f"    |  Taxa de serviço por pessoa    : R$ {cobrancaPessoa :.2f}|\n")
                print(f"    |  Valor do couvert              : R$ {valorCouvert:.2f}   |\n")
                print(f"    |  Preço final                   : R$ {contaFinal :.2f}    |\n")
                print(f"    |  Preço final por pessoa        : R$ {contaDividida :.2f} |\n")

            elif opcaoDividirConta == 2:

                print("==================================================================\n")
                print(f"    |  Quantidade de mesas reservadas:    {mesa}               |\n")
                print(f"    |  Quantidade de itens           :    {quantItens}         |\n")
                print(f"    | {quantPizzas} pizza(s) && {quantBebidas} bebidas.        |\n")
                print(f"    |  Somatório do preço das pizzas : R$ {precoPizza :.2f}    |\n")
                print(f"    |  Somatório do preço das bebidas: R$ {precoBebida :.2f}   |\n")
                print(f"    |  Taxa de serviço por pessoa    : R$ {cobrancaPessoa :.2f}|\n")
                print(f"    |  Valor do couvert              : R$ {valorCouvert:.2f}   |\n")
                print(f"    |  Preço final                   : R$ {contaFinal :.2f}    |\n")

            else:
                print("Opção inexistente.\n")
            

        elif opcao == 2:
            print("Que bom tê-lo aqui, volte sempre e até logo!\n")
            sys.exit()
        else:
            print("Opção inexistente!\n")
            sys.exit()

if __name__:
    main()