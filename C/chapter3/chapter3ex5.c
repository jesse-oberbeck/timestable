#include <stdio.h>

int main(void)
{
	int i, sum = 0;
	while(i <= 100){
		sum += i;
		i++;
	}
	printf("%d\n", sum);
}
