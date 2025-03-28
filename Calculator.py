import math as m

def somar(a, b):
    return a + b

def subitrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a, b):
    if a < 0:
        return "Erro, Raiz quadrada de número negativo"
    return m.sqrt(a)

def main():
    while True:
        print("\nCalcular em Python")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potenciação")
        print("6. Raiz Quadrada")
        print("7. Sair")

        escolha = input("Escolha a operação (1-7): ")

        if escolha == '7':
            print("Saindo...")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        elif escolha == '6':
            a = float(input("Digite o número: "))
        else:
            print("Opção inválida, tente novamente.")
            continue

        if escolha == '1':
            print("Resultado: ", somar(a, b))
        elif escolha == '2':
            print("Resultado: ", subitrair(a, b))
        elif escolha == '3':
            print("Resultado: ", multiplicar(a, b))
        elif escolha == '4':
            print("Resultado: ", dividir(a, b))
        elif escolha == '5':
            print("Resultado: ", potencia(a, b))
        elif escolha == '6':
            print("Resultado: ", raiz(a, b))

if __name__ == "__main__":
    main()
