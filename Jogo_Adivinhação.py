import random

print("\n=== JOGO DE ADIVINHAÇÃO ===")

def jogo():
    numero = random.randint(1, 100)
    while True:
        try:
            tentativas = int(input("Digite um número de 1 a 100: "))

            if tentativas < 1 or tentativas > 100:
                print("Número inválido!")
                continue
            
            if tentativas > numero:
                print("Número é menor. Tente novamente!")
            elif tentativas < numero:
                print("Número maior. Tente noamente!")
            else:
                print(f"Parabéns, você acertou!")
                while True:
                    continuar = input("Quer continuar? (s/n)")
                    if continuar == "s":
                        jogo()
                    elif continuar == "n":
                        break
                    else:
                        print("Escreve direito seu merdinha")
                        continue
                break
            
        except ValueError:
            print("Entrada inválida. Favor digitar um número inteiro!")
            continue

if __name__ == "__main__":                
    jogo()