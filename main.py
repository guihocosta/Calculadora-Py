import mod


def main():
    resp = input('Deseja iniciar a Calculadora? S/N: ')
    while resp.upper() == 'S':
        mod.f_menu()
        op = int(input('Digite aqui: '))
        if mod.f_verifica(op):
            print(f'A resposta é: {mod.f_seleciona(op)}')
        else:
            print('Digite um valor válido, por favor')
        resp = input('Deseja continuar? S/N: ')

    return 0


if __name__ == "__main__":
    main()
