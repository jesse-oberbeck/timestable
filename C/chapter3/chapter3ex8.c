#include <stdio.h>

int main(void)
{
	int number = 1;
	int secondnumber = 7;
	while(secondnumber > 0){
		while(number <= secondnumber){
			printf("%d ",number);
			number++;
		}
		secondnumber--;
		number = 1;
		puts("");
	}
		
		
	
}
