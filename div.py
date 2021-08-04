print("divide aí cabeção")
try:
    x = float(input())
    y = float(input())
    print(x / y)
except ValueError:
    print("serve nem pra isso mano")
except ZeroDivisionError:
    print("Seu imbecil, não dá pra dividir por 0... culpa do governo que não ensinou")