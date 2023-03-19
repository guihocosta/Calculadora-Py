def f_menu():
    print('Escolha a Operação:')
    print('1- Soma')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print()
    return


def f_soma():
    soma = 0
    qtd = int(input('Quantos algarismos você quer somar?: '))
    for i in range(qtd):
        n = float(input('Digite aqui o número: '))
        soma += n
    return soma


def f_sub():
    sub = 0
    qtd = int(input('Quantos algarismos você quer subtrair?: '))
    for i in range(qtd):
        n = float(input('Digite aqui o número: '))
        sub -= n
    return sub

def f_mult():
    mult = 1
    qtd = int(input('Quantos algarismos você quer multiplicar?: '))
    for i in range(qtd):
        n = float(input('Digite aqui o número: '))
        mult *= n
    return mult


def f_div():
    div = 1
    qtd = int(input('Quantos algarismos você quer dividir?: '))
    for i in range(qtd):
        n = float(input('Digite aqui o número: '))
        div /= n
    return div

def f_verifica(op)-> bool:
    if 0 < op < 5:
        return True
    else:
        return False

def f_seleciona(op):
    if op == 1:
        return f_soma()
    elif op == 2:
        return f_sub()
    elif op == 3:
        return f_mult()
    else:
        return f_div()
