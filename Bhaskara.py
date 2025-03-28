import math as mt

def main():
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    soma = A + B + C
    média = soma/3
    delta = B**2 - 4 * A * C
    x1 = (-B +(delta))/2 * A
    x2 = (-B -(delta))/2 * A

    if delta >= 0:
        print(f"A raíz 1 é: {x1}")
        print(f"A raíz 2 é: {x2}")

    else:
        print("Escreve de novo!!!")
        return main()
    
    print(f"A média é: {média}")
    print(f" A soma é: {soma}")

main()