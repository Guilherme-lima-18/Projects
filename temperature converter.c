#include <stdio.h>

int main() {
    int num1;
    char operador;
    char dnv;
    
    while (1){
    	printf("Selecione uma das opcoes: \n 1- Celsius -> Fahrenheit \n 2- Fahrenheit -> Celsius \n >>> ");
    	scanf(" %c", &operador);
    	
    	printf("Escreva o primeiro valor a ser convertido: \n >>> ");
    	scanf("%d", &num1);
    	
    	switch (operador) {
    		case '1':
    			printf("%d C em Fahrenheit: %d F \n", num1, (num1 * 9/5) + 32);
    			break;
    		case '2':
    			printf("%d F em Celsius: %d C \n", num1, (num1 - 32) * 5/9);
    			break;
    		default:
    			printf("Opcao invalida! Escolha 1 ou 2 \n");
    			continue;
		}
		
		printf("Deseja converter novamente? (s/n): \n");
		scanf(" %c", &dnv);
		
		if (dnv == 'n'){
			printf("Obrigado por usar o programa!!! \n");
			break;
		}
    	
	}

    return 0;
}
