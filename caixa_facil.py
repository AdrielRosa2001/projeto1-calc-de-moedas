def calcular_troco():
    valor_inicial = float(input("Escreva o valor do troco inicial: "))
    valor_final = float(input("Escreva o valor do final do dia: "))
    retirada = float(input("Escreva as retiradas do dia: "))
    vendas_do_dia = valor_final - valor_inicial
    valor_final_do_caixa = valor_final - retirada
    
    print("Vendido em especie:", vendas_do_dia)
    print("")

def calculadora_de_moedas():
    total_no_caixa = 0.00
    while True:
        try:
            print("------------CALCULADORA DE MOEDAS-----------")
            notas_de_200 = int(input("Notas de 200 reais: "))
            notas_de_100 = int(input("Notas de 100 reais: "))
            notas_de_50 = int(input("Notas de 50 reais: "))
            notas_de_20 = int(input("Notas de 20 reais: "))
            notas_de_10 = int(input("Notas de 10 reais: "))
            notas_de_5 = int(input("Notas de 5 reais: "))
            notas_de_2 = int(input("Notas de 2 reais: "))
            moedas_de_1 = int(input("Moedas de 1 real: "))
            moedas_de_50 = int(input("Moedas de 50 centavos: "))
            moedas_de_25 = int(input("Moedas de 25 centavos: "))
            moedas_de_10 = int(input("Moedas de 10 centavos: "))
            moedas_de_05 = int(input("Moedas de 5 centavos: "))
            moedas_de_01 = int(input("Moedas de 1 centavo: "))
            break
        except:
            print("Valor digitado invalido!\nDigite um numero inteiro!")
    total_no_caixa = total_no_caixa + (notas_de_200 * 200.00)
    total_no_caixa = total_no_caixa + (notas_de_100 * 100.00)
    total_no_caixa = total_no_caixa + (notas_de_50 * 50.00)
    total_no_caixa = total_no_caixa + (notas_de_20 * 20.00)
    total_no_caixa = total_no_caixa + (notas_de_10 * 10.00)
    total_no_caixa = total_no_caixa + (notas_de_5 * 5.00)
    total_no_caixa = total_no_caixa + (notas_de_2 * 2.00)
    total_no_caixa = total_no_caixa + (moedas_de_1 * 1.00)
    total_no_caixa = total_no_caixa + (moedas_de_50 * 0.50)
    total_no_caixa = total_no_caixa + (moedas_de_25 * 0.25)
    total_no_caixa = total_no_caixa + (moedas_de_10 * 0.10)
    total_no_caixa = total_no_caixa + (moedas_de_05 * 0.05)
    total_no_caixa = total_no_caixa + (moedas_de_01 * 0.01)
    print("=============================================")
    print("Total no caixa: "+"R$ "+str(total_no_caixa))
    print("=============================================")
    saida = input("Pressione ENTER para ir ao menu inicial: ")

    
colors = bcolors()

while True:
    print("=============================================")
    print("=================CAIXA FACIL=================")
    print("=============================================")
    print("1 - Calcular o troco.")
    print("2 - Calculadora de moedas:\n\n")
    print("3 - Sair")
    print("=============================================")
    try:
        escolha = int(input("Escolha uma opção: "))
    except:
        escolha = 4

    if escolha == 1:
        calcular_troco()
    elif escolha == 2:
        calculadora_de_moedas()
    elif escolha == 3:
        break
    else:
        print("Opção invalida! Escolha uma opção valida!")