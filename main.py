def somar():
    print("Bem-vindo à minha primeira calculadora\nPara somar digite um número, aperte enter, digite o segundo e aperte enter")
    try:
        x = int(input())
        y = int(input())
        print(x + y)
    except ValueError:
        print("Você digitou um valor inválido")
def subitrair():
    print("subtrair para o burro")
    try:
        x = float(input())
        y = float(input())
        print(x - y)
    except ValueError:
        print("valor inválido cabeção")
def multiplicar():
    print("multiplicação para o chato")
    try:
        x = float(input())
        y = float(input())
        print(x * y)
    except ValueError:
        print("errou otário")
def dividir():
    print("divide aí cabeção")
    try:
        x = float(input())
        y = float(input())
        print(x / y)
    except ValueError:
        print("serve nem pra isso mano")
    except ZeroDivisionError:
        print("Seu imbecil, não dá pra dividir por 0... culpa do governo que não ensinou")
def exponenciação():
    print("exponencial? sério isso? só não vai fazer cagada")
    try:
        x = float(input())
        y = float(input())
        print(x ** y)
    except ValueError:
        print("viu, deu erro, falei que não era boa ideia")
try:
    print("o que você deseja calcular?\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - dividisão\n5 - exponenciação")
    opcao=int(input())
    if opcao==1:
        somar()
    elif opcao==2:
        subitrair()
    elif opcao==3:
        multiplicar()
    elif opcao==4:
        dividir()
    elif opcao==5:
        exponenciação()
    elif opcao==999:
        print("chupa otário, consegui")
    elif opcao==666:
        print("Me chamou?\n           -Capetinha")
    else:
        print("Opção inválida")
except ValueError:
    print("Valor inválido")