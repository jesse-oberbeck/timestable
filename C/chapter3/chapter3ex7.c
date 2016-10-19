#include <stdio.h>

int main(void)
{
	int number = 0;
	for(number = 1; number <= 7; number++){
		for(int secondnumber = number; secondnumber > 0; secondnumber--)
			printf("%d", secondnumber);
		puts("");
	}
}
