#include <stdio.h>

int main(){
	int num1, num2;
	char operador;
	
	printf("Digite o primeiro numero: ");
	scanf("%d", &num1);
	
	printf("Digite o segundo numero: ");
	scanf("%d", &num2);
	
	printf("Escolha uma das opções abaixo \n 1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão \n");
	scanf(" %c", &operador);
	
	switch(operador){
		case '1':
			printf("%d + %d = %d", num1, num2, num1 + num2);
			break;
		case '2':
			printf("%d - %d = %d", num1, num2, num1 - num2);
			break;
		case '3':
			printf("%d * %d = %d", num1, num2, num1 * num2);
			break;
		case '4':
			if (num2 != 0)
				printf("%d / %d = %d", num1, num2, num1 / num2);
			else {
				printf("Erro: divisao por zero! \n");
				return 1;
			}
			break;
		default:
			printf("Opracao invalida! \n");
			return 1;
			
	}
	
	return 0;
	
}
